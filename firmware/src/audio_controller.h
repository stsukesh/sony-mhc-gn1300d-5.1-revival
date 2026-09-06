#pragma once
#include <Arduino.h>
#include <SPI.h>
#include <Preferences.h>
#include "pin_definitions.h"
#include "config.h"

enum InputSource {
    INPUT_BLUETOOTH = 0,
    INPUT_AUX = 1,
    INPUT_USB = 2,
    INPUT_NONE = 3
};

class AudioController {
public:
    AudioController();
    void begin();
    
    void setVolume(uint8_t level);
    uint8_t getVolume() const;
    
    void mute();
    void unmute();
    bool isMuted() const;
    
    void setInput(InputSource src);
    InputSource getInput() const;
    
    void muteAmps();
    void unmuteAmps();
    
    void triggerBtPairing();
    
    void saveSettings();
    void loadSettings();

private:
    void writePot(uint8_t address, uint8_t value);
    
    uint8_t _volume;
    uint8_t _savedVolume;
    bool _muted;
    InputSource _currentInput;
    Preferences _prefs;
};
