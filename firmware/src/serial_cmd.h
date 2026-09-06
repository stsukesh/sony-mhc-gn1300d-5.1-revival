#pragma once
#include <Arduino.h>
#include "audio_controller.h"
#include "protection.h"

class SerialCommandHandler {
public:
    SerialCommandHandler(AudioController& audio, ProtectionManager& protection);
    void begin();
    void update();

private:
    AudioController& _audio;
    ProtectionManager& _protection;
    String _buffer;
    
    void processCommand(String cmd);
};
