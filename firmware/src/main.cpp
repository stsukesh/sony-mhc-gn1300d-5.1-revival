#include <Arduino.h>
#include "config.h"
#include "pin_definitions.h"
#include "audio_controller.h"
#include "display_manager.h"
#include "input_handler.h"
#include "protection.h"
#include "wifi_manager.h"
#include "web_server.h"
#include "serial_cmd.h"

AudioController audioCtrl;
DisplayManager display(PIN_OLED_DC, PIN_OLED_CS, PIN_OLED_RST);
InputHandler inputHnd;
ProtectionManager protection;
WiFiManager wifiMgr;
WebServerManager webSrv(audioCtrl, protection, wifiMgr);
SerialCommandHandler serialCmd(audioCtrl, protection);

void setup() {
    Serial.begin(115200);
    Serial.println();
    Serial.printf("Starting %s v%s\n", SYSTEM_NAME, SYSTEM_VERSION);
    
    // SPI Init
    SPI.begin(PIN_SPI_SCK, PIN_SPI_MISO, PIN_SPI_MOSI);
    
    // Modules Init
    protection.begin();  // Important: initializes safe state & watchdog
    display.begin();
    display.showBootScreen();
    
    audioCtrl.begin();
    inputHnd.begin();
    wifiMgr.begin();
    webSrv.begin();
    serialCmd.begin();
    
    // Register Callbacks
    inputHnd.onVolumeChange([](int8_t delta) {
        int16_t v = audioCtrl.getVolume() + delta;
        if(v < 0) v = 0;
        if(v > 255) v = 255;
        audioCtrl.setVolume(v);
        webSrv.pushStateUpdate();
    });
    
    inputHnd.onInputChange([](InputSource src) {
        if(src == INPUT_NONE) {
            // Cycle logic
            int curr = audioCtrl.getInput();
            curr = (curr + 1) % 3;
            audioCtrl.setInput(static_cast<InputSource>(curr));
        } else {
            audioCtrl.setInput(src);
        }
        webSrv.pushStateUpdate();
    });
    
    inputHnd.onMuteToggle([]() {
        if(audioCtrl.isMuted()) audioCtrl.unmute();
        else audioCtrl.mute();
        webSrv.pushStateUpdate();
    });
    
    inputHnd.onPowerToggle([]() {
        SystemStatus sys = protection.getStatus();
        if(sys.relayEngaged) protection.stopPowerSequence();
        else protection.startPowerSequence();
        webSrv.pushStateUpdate();
    });
    
    inputHnd.onBtPair([]() {
        audioCtrl.triggerBtPairing();
    });
    
    // Start amp power
    protection.startPowerSequence();
    Serial.println("System Ready");
}

void loop() {
    // Non-blocking loop
    inputHnd.update();
    protection.update();
    wifiMgr.update();
    serialCmd.update();
    
    // Update Display based on state
    display.updateVolume(audioCtrl.getVolume());
    display.updateInput(audioCtrl.getInput());
    
    SystemStatus sys = protection.getStatus();
    display.updateTemperature(sys.temperature);
    
    if(sys.lastError.length() > 0) {
        display.showError(sys.lastError.c_str());
    }
    
    display.refresh();
}
