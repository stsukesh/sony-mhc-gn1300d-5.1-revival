#include "serial_cmd.h"
#include "config.h"

SerialCommandHandler::SerialCommandHandler(AudioController& audio, ProtectionManager& protection)
    : _audio(audio), _protection(protection) {}

void SerialCommandHandler::begin() {
    // Serial is assumed to be started in main.cpp
    _buffer.reserve(64);
}

void SerialCommandHandler::update() {
    while (Serial.available() > 0) {
        char c = Serial.read();
        if (c == '\n' || c == '\r') {
            if (_buffer.length() > 0) {
                processCommand(_buffer);
                _buffer = "";
            }
        } else {
            _buffer += c;
        }
    }
}

void SerialCommandHandler::processCommand(String cmd) {
    cmd.trim();
    cmd.toUpperCase();
    
    if (cmd.startsWith("VOL ")) {
        int v = cmd.substring(4).toInt();
        if (v >= 0 && v <= 255) {
            _audio.setVolume(v);
            Serial.println("OK:VOLUME_SET");
        } else {
            Serial.println("ERR:INVALID_VOLUME");
        }
    } else if (cmd == "VOL+") {
        int v = _audio.getVolume() + 5;
        if(v > 255) v = 255;
        _audio.setVolume(v);
        Serial.println("OK:VOLUME_UP");
    } else if (cmd == "VOL-") {
        int v = _audio.getVolume() - 5;
        if(v < 0) v = 0;
        _audio.setVolume(v);
        Serial.println("OK:VOLUME_DOWN");
    } else if (cmd == "VOL?") {
        Serial.printf("OK:%d\n", _audio.getVolume());
    } else if (cmd == "MUTE") {
        if(_audio.isMuted()) _audio.unmute();
        else _audio.mute();
        Serial.println("OK:MUTE_TOGGLED");
    } else if (cmd == "POWER") {
        SystemStatus sys = _protection.getStatus();
        if(sys.relayEngaged) _protection.stopPowerSequence();
        else _protection.startPowerSequence();
        Serial.println("OK:POWER_TOGGLED");
    } else if (cmd == "REBOOT") {
        Serial.println("OK:REBOOTING");
        delay(100);
        ESP.restart();
    } else if (cmd == "HELP") {
        Serial.println("Commands: VOL <0-255>, VOL+, VOL-, VOL?, MUTE, POWER, REBOOT");
    } else {
        Serial.println("ERR:UNKNOWN_COMMAND");
    }
}
