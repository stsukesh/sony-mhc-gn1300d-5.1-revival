#pragma once
#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "audio_controller.h"

class DisplayManager {
public:
    DisplayManager(int8_t dc, int8_t cs, int8_t rst);
    void begin();
    
    void updateVolume(uint8_t level);
    void updateInput(InputSource src);
    void updateBtStatus(bool connected);
    void updateTemperature(float tempC);
    void showError(const char* msg);
    void showBootScreen();
    void refresh();
    void clearError();

private:
    Adafruit_SSD1306 _display;
    
    uint8_t _volume;
    InputSource _input;
    bool _btConnected;
    float _tempC;
    String _errorMsg;
    bool _showingError;
    uint32_t _errorStartTime;
    bool _dirty;
    
    void drawMainScreen();
};
