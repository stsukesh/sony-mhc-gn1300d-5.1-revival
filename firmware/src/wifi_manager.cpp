#include "wifi_manager.h"
#include "config.h"
#include <Preferences.h>

WiFiManager::WiFiManager() : _staConfigured(false), _lastReconnectAttempt(0) {}

void WiFiManager::begin() {
    WiFi.mode(WIFI_AP_STA);
    WiFi.softAP(WIFI_AP_SSID, WIFI_AP_PASS);
    
    Serial.print("AP IP address: ");
    Serial.println(WiFi.softAPIP());
    
    loadCredentials();
    
    if (_staConfigured) {
        WiFi.begin(_staSsid.c_str(), _staPass.c_str());
    }
}

void WiFiManager::update() {
    if (_staConfigured && WiFi.status() != WL_CONNECTED) {
        uint32_t now = millis();
        if (now - _lastReconnectAttempt > 10000) {
            _lastReconnectAttempt = now;
            WiFi.disconnect();
            WiFi.begin(_staSsid.c_str(), _staPass.c_str());
        }
    }
}

bool WiFiManager::isConnected() {
    return WiFi.status() == WL_CONNECTED;
}

String WiFiManager::getIP() {
    if (isConnected()) {
        return WiFi.localIP().toString();
    }
    return WiFi.softAPIP().toString();
}

String WiFiManager::getSSID() {
    if (isConnected()) {
        return WiFi.SSID();
    }
    return String(WIFI_AP_SSID);
}

void WiFiManager::saveCredentials(const char* ssid, const char* pass) {
    Preferences prefs;
    prefs.begin(NVS_NAMESPACE, false);
    prefs.putString("wifi_ssid", ssid);
    prefs.putString("wifi_pass", pass);
    prefs.end();
    
    _staSsid = ssid;
    _staPass = pass;
    _staConfigured = true;
    
    WiFi.disconnect();
    WiFi.begin(_staSsid.c_str(), _staPass.c_str());
}

void WiFiManager::loadCredentials() {
    Preferences prefs;
    prefs.begin(NVS_NAMESPACE, true);
    _staSsid = prefs.getString("wifi_ssid", "");
    _staPass = prefs.getString("wifi_pass", "");
    prefs.end();
    
    if (_staSsid.length() > 0) {
        _staConfigured = true;
    }
}
