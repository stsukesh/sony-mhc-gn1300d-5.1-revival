#include "input_handler.h"
#include "pin_definitions.h"

volatile int8_t InputHandler::_encoderDelta = 0;
volatile uint32_t InputHandler::_lastEncTime = 0;

void IRAM_ATTR InputHandler::isrEncoder() {
    uint32_t now = millis();
    if (now - _lastEncTime > 5) {
        bool a = digitalRead(PIN_ENC_A);
        bool b = digitalRead(PIN_ENC_B);
        if (a == b) {
            _encoderDelta++; // clockwise
        } else {
            _encoderDelta--; // counter-clockwise
        }
        _lastEncTime = now;
    }
}

InputHandler::InputHandler() : _irrecv(PIN_IR_RECV), _lastBtnState(HIGH), _btnPressTime(0), _btnLongPressed(false), _btnPressCount(0), _lastBtnReleaseTime(0) {}

void InputHandler::begin() {
    pinMode(PIN_ENC_A, INPUT_PULLUP);
    pinMode(PIN_ENC_B, INPUT_PULLUP);
    pinMode(PIN_ENC_SW, INPUT_PULLUP);
    
    attachInterrupt(digitalPinToInterrupt(PIN_ENC_A), isrEncoder, CHANGE);
    
    _irrecv.enableIRIn();
}

void InputHandler::update() {
    handleEncoder();
    handleButton();
    handleIR();
}

void InputHandler::handleEncoder() {
    if (_encoderDelta != 0) {
        noInterrupts();
        int8_t delta = _encoderDelta;
        _encoderDelta = 0;
        interrupts();
        
        if (_volCb) {
            _volCb(delta * 5); // 5 steps per detent
        }
    }
}

void InputHandler::handleButton() {
    bool btnState = digitalRead(PIN_ENC_SW);
    uint32_t now = millis();

    if (btnState == LOW && _lastBtnState == HIGH) { // Pressed
        _btnPressTime = now;
        _btnLongPressed = false;
    } else if (btnState == HIGH && _lastBtnState == LOW) { // Released
        uint32_t pressDuration = now - _btnPressTime;
        if (pressDuration > 50 && pressDuration < 500 && !_btnLongPressed) {
            _btnPressCount++;
            _lastBtnReleaseTime = now;
        }
    } else if (btnState == LOW && _lastBtnState == LOW) { // Held
        if (now - _btnPressTime > 2000 && !_btnLongPressed) {
            _btnLongPressed = true;
            if (_btPairCb) _btPairCb();
        }
    }

    if (_btnPressCount > 0 && (now - _lastBtnReleaseTime > 500)) {
        if (_btnPressCount == 1) {
            // Short press: Cycle input
            if (_inputCb) _inputCb(INPUT_NONE); // Signal to main to cycle
        } else if (_btnPressCount == 2) {
            // Double press: Toggle mute
            if (_muteCb) _muteCb();
        }
        _btnPressCount = 0;
    }

    _lastBtnState = btnState;
}

void InputHandler::handleIR() {
    if (_irrecv.decode(&_results)) {
        if (_results.value != 0xFFFFFFFF) { // Ignore repeat codes
            Serial.printf("IR Code: 0x%08X\n", _results.value); // Learn mode info
            
            switch (_results.value) {
                case IR_VOL_UP:
                    if (_volCb) _volCb(5);
                    break;
                case IR_VOL_DOWN:
                    if (_volCb) _volCb(-5);
                    break;
                case IR_MUTE:
                    if (_muteCb) _muteCb();
                    break;
                case IR_INPUT_BT:
                    if (_inputCb) _inputCb(INPUT_BLUETOOTH);
                    break;
                case IR_INPUT_AUX:
                    if (_inputCb) _inputCb(INPUT_AUX);
                    break;
                case IR_INPUT_USB:
                    if (_inputCb) _inputCb(INPUT_USB);
                    break;
                case IR_POWER:
                    if (_powerCb) _powerCb();
                    break;
            }
        }
        _irrecv.resume();
    }
}
