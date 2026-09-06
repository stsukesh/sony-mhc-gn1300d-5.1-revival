#include "display_manager.h"
#include "config.h"

DisplayManager::DisplayManager(int8_t dc, int8_t cs, int8_t rst) 
    : _display(128, 64, &SPI, dc, rst, cs), _volume(0), _input(INPUT_NONE), _btConnected(false), _tempC(0), _showingError(false), _dirty(true) {}

void DisplayManager::begin() {
    if(!_display.begin(SSD1306_SWITCHCAPVCC)) {
        Serial.println(F("SSD1306 allocation failed"));
    }
    _display.clearDisplay();
    _display.display();
}

void DisplayManager::showBootScreen() {
    _display.clearDisplay();
    _display.setTextSize(2);
    _display.setTextColor(SSD1306_WHITE);
    _display.setCursor(10, 20);
    _display.println(F("SONY 5.1"));
    _display.setTextSize(1);
    _display.setCursor(30, 40);
    _display.println(F("REVIVAL"));
    _display.setCursor(90, 50);
    _display.println(F(SYSTEM_VERSION));
    _display.display();
    delay(2000);
    _dirty = true;
}

void DisplayManager::updateVolume(uint8_t level) {
    if (_volume != level) {
        _volume = level;
        _dirty = true;
    }
}

void DisplayManager::updateInput(InputSource src) {
    if (_input != src) {
        _input = src;
        _dirty = true;
    }
}

void DisplayManager::updateBtStatus(bool connected) {
    if (_btConnected != connected) {
        _btConnected = connected;
        _dirty = true;
    }
}

void DisplayManager::updateTemperature(float tempC) {
    if (abs(_tempC - tempC) > 1.0) {
        _tempC = tempC;
        _dirty = true;
    }
}

void DisplayManager::showError(const char* msg) {
    _errorMsg = String(msg);
    _showingError = true;
    _errorStartTime = millis();
    _dirty = true;
}

void DisplayManager::clearError() {
    _showingError = false;
    _dirty = true;
}

void DisplayManager::refresh() {
    if (_showingError && millis() - _errorStartTime > 3000) {
        _showingError = false;
        _dirty = true;
    }

    if (!_dirty) return;
    
    _display.clearDisplay();
    
    if (_showingError) {
        _display.setTextSize(2);
        _display.setTextColor(SSD1306_WHITE);
        _display.setCursor(0, 20);
        _display.println(F("ERROR:"));
        _display.setTextSize(1);
        _display.println(_errorMsg);
    } else {
        drawMainScreen();
    }
    
    _display.display();
    _dirty = false;
}

void DisplayManager::drawMainScreen() {
    _display.setTextSize(1);
    _display.setTextColor(SSD1306_WHITE);
    
    // Line 1
    _display.setCursor(0, 0);
    _display.print(SYSTEM_NAME);
    _display.setCursor(100, 0);
    _display.print(F("BT:"));
    _display.print(_btConnected ? "O" : "X");
    
    // Line 2
    _display.setCursor(0, 16);
    _display.print(F("INPUT: "));
    switch(_input) {
        case INPUT_BLUETOOTH: _display.print(F("BLUETOOTH")); break;
        case INPUT_AUX: _display.print(F("AUX")); break;
        case INPUT_USB: _display.print(F("USB")); break;
        case INPUT_NONE: _display.print(F("NONE")); break;
    }
    
    // Line 3-4 (Volume Bar)
    _display.setCursor(0, 32);
    _display.print(F("VOL: "));
    uint8_t percent = (_volume * 100) / 255;
    _display.print(percent);
    _display.print(F("%"));
    _display.drawRect(0, 42, 128, 8, SSD1306_WHITE);
    _display.fillRect(0, 42, (_volume * 128) / 255, 8, SSD1306_WHITE);
    
    // Line 5
    _display.setCursor(0, 56);
    _display.print(F("P PLAYING  TEMP:"));
    _display.print((int)_tempC);
    _display.print(F("C"));
}
