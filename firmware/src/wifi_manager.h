#pragma once
#include <Arduino.h>
#include <WiFi.h>

class WiFiManager {
public:
    WiFiManager();
    void begin();
    void update();
    
    bool isConnected();
    String getIP();
    String getSSID();
    
    void saveCredentials(const char* ssid, const char* pass);

private:
    void loadCredentials();
    
    String _staSsid;
    String _staPass;
    bool _staConfigured;
    uint32_t _lastReconnectAttempt;
};
