#pragma once
#include <Arduino.h>

struct SystemStatus {
    bool ampFault[3];
    float temperature;
    bool dcOffsetDetected;
    bool relayEngaged;
    bool ampsMuted;
    uint32_t uptimeSeconds;
    String lastError;
};

class ProtectionManager {
public:
    ProtectionManager();
    void begin();
    void update();
    
    void startPowerSequence();
    void stopPowerSequence();
    void emergencyShutdown(const char* reason);
    
    SystemStatus getStatus();

private:
    bool checkFaults();
    bool checkDCOffset();
    bool checkTemperature();
    
    enum State {
        STATE_SAFE,
        STATE_STARTING,
        STATE_RUNNING,
        STATE_FAULT
    };
    
    State _state;
    uint32_t _stateStartTime;
    uint32_t _lastCheckTime;
    uint8_t _retryCount;
    
    SystemStatus _status;
    
    void configureWatchdog();
    void feedWatchdog();
};
