#pragma once
#include <Arduino.h>
#include <IRrecv.h>
#include <IRremoteESP8266.h>
#include <IRutils.h>
#include "audio_controller.h"

// IR Codes (NEC)
#define IR_VOL_UP 0xFF906F
#define IR_VOL_DOWN 0xFFE01F
#define IR_MUTE 0xFFA25D
#define IR_INPUT_BT 0xFF6897
#define IR_INPUT_AUX 0xFF9867
#define IR_INPUT_USB 0xFFB04F
#define IR_POWER 0xFF02FD

typedef void (*VolumeChangeCallback)(int8_t);
typedef void (*InputChangeCallback)(InputSource);
typedef void (*MuteToggleCallback)();
typedef void (*BtPairCallback)();
typedef void (*PowerToggleCallback)();

class InputHandler {
public:
    InputHandler();
    void begin();
    void update();

    void onVolumeChange(VolumeChangeCallback cb) { _volCb = cb; }
    void onInputChange(InputChangeCallback cb) { _inputCb = cb; }
    void onMuteToggle(MuteToggleCallback cb) { _muteCb = cb; }
    void onBtPair(BtPairCallback cb) { _btPairCb = cb; }
    void onPowerToggle(PowerToggleCallback cb) { _powerCb = cb; }

    static void IRAM_ATTR isrEncoder();

private:
    void handleEncoder();
    void handleButton();
    void handleIR();

    IRrecv _irrecv;
    decode_results _results;

    VolumeChangeCallback _volCb = nullptr;
    InputChangeCallback _inputCb = nullptr;
    MuteToggleCallback _muteCb = nullptr;
    BtPairCallback _btPairCb = nullptr;
    PowerToggleCallback _powerCb = nullptr;

    static volatile int8_t _encoderDelta;
    static volatile uint32_t _lastEncTime;
    
    bool _lastBtnState;
    uint32_t _btnPressTime;
    bool _btnLongPressed;
    uint8_t _btnPressCount;
    uint32_t _lastBtnReleaseTime;
};
