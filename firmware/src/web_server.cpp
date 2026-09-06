#include "web_server.h"
#include "config.h"
#include <SPIFFS.h>

WebServerManager::WebServerManager(AudioController& audio, ProtectionManager& protection, WiFiManager& wifi)
    : _server(80), _ws("/ws"), _audio(audio), _protection(protection), _wifi(wifi) {}

void WebServerManager::begin() {
    if (!SPIFFS.begin(true)) {
        Serial.println("SPIFFS Mount Failed");
    }

    _ws.onEvent([this](AsyncWebSocket *server, AsyncWebSocketClient *client, AwsEventType type, void *arg, uint8_t *data, size_t len){
        this->onWsEvent(server, client, type, arg, data, len);
    });
    _server.addHandler(&_ws);
    
    setupRoutes();
    
    _server.begin();
}

void WebServerManager::setupRoutes() {
    _server.serveStatic("/", SPIFFS, "/").setDefaultFile("index.html");
    
    _server.on("/api/status", HTTP_GET, [this](AsyncWebServerRequest *request){
        AsyncResponseStream *response = request->beginResponseStream("application/json");
        DynamicJsonDocument doc(512);
        doc["volume"] = _audio.getVolume();
        doc["input"] = _audio.getInput();
        doc["muted"] = _audio.isMuted();
        
        SystemStatus sys = _protection.getStatus();
        doc["temp"] = sys.temperature;
        doc["uptime"] = sys.uptimeSeconds;
        doc["relayEngaged"] = sys.relayEngaged;
        doc["faults"] = sys.ampFault[0] || sys.ampFault[1] || sys.ampFault[2];
        
        serializeJson(doc, *response);
        request->send(response);
    });
    
    AsyncCallbackJsonWebHandler* volHandler = new AsyncCallbackJsonWebHandler("/api/volume", [this](AsyncWebServerRequest *request, JsonVariant &json) {
        JsonObject jsonObj = json.as<JsonObject>();
        if(jsonObj.containsKey("level")) {
            _audio.setVolume(jsonObj["level"].as<uint8_t>());
            pushStateUpdate();
            request->send(200, "application/json", "{\"status\":\"ok\"}");
        } else {
            request->send(400);
        }
    });
    _server.addHandler(volHandler);
    
    // Add simple POST routes
    _server.on("/api/mute", HTTP_POST, [this](AsyncWebServerRequest *request){
        if(_audio.isMuted()) _audio.unmute();
        else _audio.mute();
        pushStateUpdate();
        request->send(200, "application/json", "{\"status\":\"ok\"}");
    });
    
    _server.on("/api/power", HTTP_POST, [this](AsyncWebServerRequest *request){
        SystemStatus sys = _protection.getStatus();
        if(sys.relayEngaged) _protection.stopPowerSequence();
        else _protection.startPowerSequence();
        pushStateUpdate();
        request->send(200, "application/json", "{\"status\":\"ok\"}");
    });

    _server.on("/api/reboot", HTTP_POST, [](AsyncWebServerRequest *request){
        request->send(200, "application/json", "{\"status\":\"rebooting\"}");
        delay(500);
        ESP.restart();
    });
}

void WebServerManager::pushStateUpdate() {
    if(_ws.count() > 0) {
        DynamicJsonDocument doc(256);
        doc["volume"] = _audio.getVolume();
        doc["input"] = _audio.getInput();
        doc["muted"] = _audio.isMuted();
        
        SystemStatus sys = _protection.getStatus();
        doc["temp"] = sys.temperature;
        doc["relayEngaged"] = sys.relayEngaged;
        
        String json;
        serializeJson(doc, json);
        _ws.textAll(json);
    }
}

void WebServerManager::onWsEvent(AsyncWebSocket *server, AsyncWebSocketClient *client, AwsEventType type, void *arg, uint8_t *data, size_t len) {
    if(type == WS_EVT_CONNECT) {
        pushStateUpdate(); // Send initial state
    }
}
