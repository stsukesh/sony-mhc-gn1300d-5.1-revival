#pragma once
#include <Arduino.h>
#include <ESPAsyncWebServer.h>
#include <AsyncJson.h>
#include <ArduinoJson.h>
#include "audio_controller.h"
#include "protection.h"
#include "wifi_manager.h"

class WebServerManager {
public:
    WebServerManager(AudioController& audio, ProtectionManager& protection, WiFiManager& wifi);
    void begin();
    void pushStateUpdate();

private:
    AsyncWebServer _server;
    AsyncWebSocket _ws;
    
    AudioController& _audio;
    ProtectionManager& _protection;
    WiFiManager& _wifi;
    
    void setupRoutes();
    void onWsEvent(AsyncWebSocket *server, AsyncWebSocketClient *client, AwsEventType type, void *arg, uint8_t *data, size_t len);
};
