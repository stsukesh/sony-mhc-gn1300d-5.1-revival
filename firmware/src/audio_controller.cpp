#include "audio_controller.h"

AudioController::AudioController() : _volume(DEFAULT_VOLUME), _savedVolume(DEFAULT_VOLUME), _muted(false), _currentInput(static_cast<InputSource>(DEFAULT_INPUT)) {}

void AudioController::begin() {
    pinMode(PIN_VOL_CS, OUTPUT);
    digitalWrite(PIN_VOL_CS, HIGH);
    
    pinMode(PIN_MUX_A, OUTPUT);
    pinMode(PIN_MUX_B, OUTPUT);
    
    pinMode(PIN_MUTE_ALL, OUTPUT);
    digitalWrite(PIN_MUTE_ALL, LOW); // Start muted
    
    pinMode(PIN_BT_KEY, OUTPUT);
    digitalWrite(PIN_BT_KEY, HIGH);
    
    loadSettings();
    setVolume(_volume);
    setInput(_currentInput);
}

void AudioController::setVolume(uint8_t level) {
    _volume = level;
    if (!_muted) {
        writePot(0x00, _volume);
        writePot(0x01, _volume);
    }
}

uint8_t AudioController::getVolume() const {
    return _volume;
}

void AudioController::mute() {
    if (!_muted) {
        _savedVolume = _volume;
        _muted = true;
        writePot(0x00, 0);
        writePot(0x01, 0);
    }
}

void AudioController::unmute() {
    if (_muted) {
        _muted = false;
        setVolume(_savedVolume);
    }
}

bool AudioController::isMuted() const {
    return _muted;
}

void AudioController::setInput(InputSource src) {
    _currentInput = src;
    digitalWrite(PIN_MUX_A, (src & 0x01) ? HIGH : LOW);
    digitalWrite(PIN_MUX_B, (src & 0x02) ? HIGH : LOW);
}

InputSource AudioController::getInput() const {
    return _currentInput;
}

void AudioController::muteAmps() {
    digitalWrite(PIN_MUTE_ALL, LOW);
}

void AudioController::unmuteAmps() {
    digitalWrite(PIN_MUTE_ALL, HIGH);
}

void AudioController::triggerBtPairing() {
    digitalWrite(PIN_BT_KEY, LOW);
    delay(3000);
    digitalWrite(PIN_BT_KEY, HIGH);
}

void AudioController::writePot(uint8_t address, uint8_t value) {
    SPI.beginTransaction(SPISettings(SPI_SPEED_MCP4252, MSBFIRST, SPI_MODE0));
    digitalWrite(PIN_VOL_CS, LOW);
    uint8_t cmd = (address << 4) | 0b0000;
    SPI.transfer(cmd);
    SPI.transfer(value);
    digitalWrite(PIN_VOL_CS, HIGH);
    SPI.endTransaction();
}

void AudioController::saveSettings() {
    _prefs.begin(NVS_NAMESPACE, false);
    _prefs.putUChar("vol", _volume);
    _prefs.putUChar("inp", static_cast<uint8_t>(_currentInput));
    _prefs.putBool("mute", _muted);
    _prefs.end();
}

void AudioController::loadSettings() {
    _prefs.begin(NVS_NAMESPACE, true);
    _volume = _prefs.getUChar("vol", DEFAULT_VOLUME);
    _currentInput = static_cast<InputSource>(_prefs.getUChar("inp", DEFAULT_INPUT));
    _muted = _prefs.getBool("mute", false);
    _prefs.end();
    if(_muted) {
        _savedVolume = _volume;
    }
}
