# SONY® 5.1 REVIVAL SYSTEM — OEM SERVICE MANUAL
## MODEL IDENTIFICATION: SONY-5.1-REV-2026
### RETROFIT FOR SONY MHC-GN1300D / HCD-GN1300D ENCLOSURES
**DOCUMENT NO.: SM-SONY51REV-8001-A**  
**REVISION: 1.0 (PRODUCTION RELEASE)**  
**DATE: SEPTEMBER 2026**

```
================================================================================
                               SERVICE MANUAL
         6-CHANNEL CLASS-D HOME THEATER AMPLIFIER & DSP HUB
               FEATURING ESP32 SYSTEM CONTROLLER,
        NE5532 ACTIVE CROSSOVER, AND 5-LAYER FAIL-SAFE PROTECTION
================================================================================
```

---

## TABLE OF CONTENTS

1. [SERVICE SAFETY PRECAUTIONS & WARNINGS](#1-service-safety-precautions--warnings)
2. [GENERAL SPECIFICATIONS](#2-general-specifications)
3. [DISASSEMBLY & MECHANICAL ACCESS](#3-disassembly--mechanical-access)
4. [THEORY OF OPERATION & CIRCUIT BLOCK DIAGRAM](#4-theory-of-operation--circuit-block-diagram)
5. [TEST POINTS & VOLTAGE REFERENCE TABLE](#5-test-points--voltage-reference-table)
6. [OSCILLOSCOPE WAVEFORMS & SIGNAL TRACING](#6-oscilloscope-waveforms--signal-tracing)
7. [DIAGNOSTIC TEST MODES & FIRMWARE CLI](#7-diagnostic-test-modes--firmware-cli)
8. [SYSTEMATIC TROUBLESHOOTING FLOWCHARTS](#8-systematic-troubleshooting-flowcharts)
   - 8.1 [Condition A: Dead Unit / No Power / No OLED](#81-condition-a-dead-unit--no-power--no-oled)
   - 8.2 [Condition B: Unit Enters Protection Lockout / Emergency Shutdown](#82-condition-b-unit-enters-protection-lockout--emergency-shutdown)
   - 8.3 [Condition C: No Sound from One or All Channels](#83-condition-c-no-sound-from-one-or-all-channels)
   - 8.4 [Condition D: Audio Distorted, Muffled, or Rattling](#84-condition-d-audio-distorted-muffled-or-rattling)
   - 8.5 [Condition E: Bluetooth Pairing / Wi-Fi / OLED Failure](#85-condition-e-bluetooth-pairing--wi-fi--oled-failure)
9. [FAIL-SAFE PROTECTION SYSTEM CALIBRATION](#9-fail-safe-protection-system-calibration)
10. [CRITICAL COMPONENT REPLACEMENT & SOLDERING GUIDE](#10-critical-component-replacement--soldering-guide)
11. [COMPLETE PARTS LIST & OEM CROSS-REFERENCE](#11-complete-parts-list--oem-cross-reference)

---

## 1. SERVICE SAFETY PRECAUTIONS & WARNINGS

### ⚠️ CRITICAL SAFETY NOTICE (COMPONENTS MARKED WITH ⚠️)
Components identified with the mark ⚠️ or special shaded symbols in this manual are critical to safe operation. Replace these components only with specified parts matching identical voltage, current, dielectric, and flame-retardant ratings.

```
       ┌────────────────────────────────────────────────────────┐
       │                       WARNING                          │
       │  HAZARDOUS VOLTAGES (230V AC) PRESENT ON PRIMARY SIDE  │
       │   STORED DC ENERGY IN BULK CAPACITORS (9400µF / 35V)   │
       │      DISCHARGE CAPACITORS BEFORE SERVICING PCB         │
       └────────────────────────────────────────────────────────┘
```

1. **AC Mains Isolation:** Always disconnect the 230V AC line cord from the mains wall outlet before removing the top chassis cover or desoldering components.
2. **Capacitor Discharge Procedure:** After disconnecting AC power, connect a $100\Omega / 10\text{W}$ wirewound power resistor across bulk capacitors $C_1$ and $C_2$ for at least 15 seconds. Measure DC voltage across $C_1/C_2$ with a multimeter; verify voltage is $< 1.0\text{V DC}$ before proceeding with service. **DO NOT SHORT CAPACITORS WITH A SCREWDRIVER** (risks copper vapor explosion and trace destruction).
3. **Electrostatic Discharge (ESD) Protection:** The ESP32 MCU, Qualcomm QCC3008 Bluetooth module, MCP4252 digital pot, and CD4052 multiplexer are sensitive CMOS devices. Wear an earthed antistatic wrist strap with a $1\text{M}\Omega$ safety resistor when handling the circuit board.
4. **Leakage Current Cold Check:** Before returning repaired unit to customer:
   - Unplug AC cord.
   - Turn power switch $SW_1$ ON.
   - Measure resistance between AC plug blades (L and N tied together) and exposed chassis ground metalwork.
   - Resistance must read **$> 10\text{ M}\Omega$**. Any reading $< 5\text{ M}\Omega$ indicates insulation breakdown.
5. **Polyfuse Replacement:** Never bridge or bypass polyfuses $PF_1$ through $PF_6$ with jumper wire. Doing so removes the voice-coil thermal protection layer and will destroy the original Sony speaker cabinets during an overcurrent event.

---

## 2. GENERAL SPECIFICATIONS

### AMPLIFIER SECTION
* **Topology:** High-Efficiency Class-D (Bridge-Tied Load / BTL) via 3× Texas Instruments TPA3116D2.
* **Continuous Clean Power Output (at 24V DC, 1kHz, 1% THD+N):**
  - **Front Left / Front Right (SS-GN1300D):** $50\text{W} + 50\text{W}$ into $6\,\Omega$
  - **Center Channel (SS-CT1300D):** $35\text{W}$ into $6\,\Omega$
  - **Surround Left / Surround Right (SS-RSX1300D):** $35\text{W} + 35\text{W}$ into $6\,\Omega$
  - **Subwoofer Channel (SS-WGV1300D):** $50\text{W}$ into $8\,\Omega$
* **Total Continuous System Output:** **255W RMS** combined clean audio output across 6 channels.
* **PWM Switching Frequency:** $400\text{ kHz}$ (synchronized, AM avoidance enabled).
* **Signal-to-Noise Ratio (SNR):** $> 98\text{ dB}$ (A-weighted, rated power).
* **Total Harmonic Distortion (THD+N):** $< 0.1\%$ at $1\text{kHz}, 25\text{W}$ output.

### ACTIVE CROSSOVER SECTION
* **Architecture:** 2nd-order Sallen-Key Active Filter ($Q = 0.50$ critically damped, -12 dB/octave roll-off).
* **Op-Amps:** 3× Texas Instruments NE5532 Low-Noise Dual Operational Amplifiers.
* **Front Channels High-Pass:** $f_c = 79.6\text{ Hz}$
* **Surround Channels High-Pass:** $f_c = 99.5\text{ Hz}$
* **Center Channel High-Pass:** $f_c = 99.5\text{ Hz}$
* **Subwoofer Channel Low-Pass:** $f_c = 79.6\text{ Hz}$
* **Virtual Ground Reference:** $12.0\text{V DC} \pm 0.1\text{V}$ (generated via TLE2426).

### POWER SUPPLY SECTION
* **Mains Input:** $220\text{--}240\text{V AC}, 50/60\text{ Hz}$.
* **Transformer:** 200VA Toroidal Transformer, Secondary $18.0\text{V AC RMS}$.
* **Main Amplifier Rail ($V_{CC\_24V}$):** $+24.0\text{V DC}$ nominal unloaded; $+20.9\text{V DC}$ loaded at 5.8A continuous.
* **Auxiliary Digital Rails:** $+5.0\text{V DC} \pm 0.1\text{V}$ (LM2596-5.0 Buck) and $+3.3\text{V DC} \pm 0.05\text{V}$ (AMS1117-3.3 LDO).
* **Mains Protection:** 3A 250V 5×20mm fast-blow ceramic fuse ($F_1$) + 14D431K Metal Oxide Varistor ($RV_1$).

### SYSTEM CONTROLLER & USER INTERFACE
* **Processor:** Espressif ESP32-WROOM-32 (240MHz dual-core Xtensa LX6).
* **Display:** 2.42-inch $128 \times 64$ White SPI OLED (SSD1309 driver).
* **Local Controls:** Incremental rotary encoder with push switch + Vishay TSOP1738 38kHz IR receiver.
* **Wireless:** Wi-Fi $802.11\text{ b/g/n}$ (SoftAP `Sony5.1-Revival` + Web Server) + Qualcomm QCC3008 Bluetooth 5.0 (aptX, aptX-LL, SBC, AAC).
* **Hardware Serial CLI:** 115200 baud, 8-N-1 on 6-pin diagnostic header.

---

## 3. DISASSEMBLY & MECHANICAL ACCESS

Follow these steps sequentially to prevent PCB flexing or thermal pad tearing:

```
[STEP 1: AC DISCONNECT] ──▶ [STEP 2: TOP COVER] ──▶ [STEP 3: HEATSINK CLAMPS]
                                                            │
[STEP 6: MAIN PCB REMOVAL] ◀── [STEP 5: TERMINAL HARNESS] ◀─┘
```

### STEP 1: SAFETY DISCHARGE
1. Disconnect the AC power cord from mains.
2. Remove the 4 chassis ground screws from the rear apron.
3. Discharge bulk capacitors $C_1/C_2$ using the $100\Omega/10\text{W}$ resistor as described in Section 1.

### STEP 2: TOP COVER REMOVAL
1. Remove 4 screws (M3×6mm, Phillips black) on the left and right chassis flanges.
2. Remove 3 screws (M3×6mm) along the top rear rim.
3. Slide the top cover rearward 20mm, lift clear, and set aside.

### STEP 3: HEATSINK & THERMAL INTERFACE UNMOUNTING
1. The 3× TPA3116D2 ICs are mounted beneath a common black anodized extruded aluminium heatsink ($150 \times 50 \times 25\text{ mm}$).
2. Loosen the 2 central spring-loaded retention bar screws evenly (alternate 1 turn each to prevent uneven shear force on the IC packages).
3. Lift the heatsink vertically.
4. **Inspection:** Examine the pink silicone thermal interface pads (0.5mm thickness). If dried, torn, or contaminated with dust, replace with high-conductivity thermal pads ($> 3.0\text{ W/m}\cdot\text{K}$) before reassembly.

### STEP 4: FRONT PANEL & DISPLAY ACCESS
1. Disconnect the 7-pin rainbow ribbon cable from OLED header $J_{OLED}$ on the main PCB.
2. Disconnect the 5-pin encoder cable from $J_{ENC}$.
3. Remove 4 front panel plastic snap-fit tabs to free the front bezel.

### STEP 5: SPEAKER & MAINS TERMINAL DISCONNECTION
1. Loosen the terminal screws on $J_{AC}$ (Live, Neutral, Earth) and pull wires clear.
2. Loosen screws on $J_{SPK1}$ through $J_{SPK6}$ (FL, FR, SL, SR, Center, Sub).
3. Mark speaker wires with masking tape to avoid phase inversion during reinstallation.

### STEP 6: MAIN PCB REMOVAL
1. Remove 6 corner and perimeter mounting screws (M3×8mm brass standoffs).
2. Lift the PCB forward and out of the chassis.

---

## 4. THEORY OF OPERATION & CIRCUIT BLOCK DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 SYSTEM SIGNAL FLOW DIAGRAM                                  │
│                                                                                             │
│  [ Bluetooth: QCC3008 ] ──┐                                                                 │
│  [ AUX 3.5mm: J_AUX   ] ──┼──▶ [ CD4052 Mux ] ──▶ [ MCP4252 ] ──▶ [ NE5532 Active Crossover]│
│  [ USB Audio: J_USB   ] ──┘    (U_MUX: GPIO26/27)  (U_VOL: SPI)   │                         │
│                                                                   ├─ Front HPF 80Hz ────────┼─┐
│                                                                   ├─ Surr HPF 100Hz ────────┼─┼─┐
│                                                                   ├─ Center (L+R)/2 100Hz ──┼─┼─┼─┐
│                                                                   └─ Sub (L+R) LPF 80Hz ────┼─┼─┼─┼─┐
│                                                                                             │ │ │ │ │
│  ┌──────────────────────────────────────────────────────────────┐                           │ │ │ │ │
│  │                     ESP32 SYSTEM BRAIN                       │                           ▼ ▼ ▼ ▼ ▼
│  │                                                              │                         ┌────────────┐
│  │  - SSD1309 OLED (SPI: GPIO18,23,4,5)                         │                         │ 3x TPA3116 │
│  │  - Rotary Encoder (GPIO15,16,17)                             │                         │ Class-D    │
│  │  - TSOP1738 IR (GPIO14)                                      │                         │ Output     │
│  │  - Wi-Fi & WebServer (192.168.4.1)                           │                         │ Stages     │
│  │  - UART Diagnostic Port (115200)                             │                         └─────┬──────┘
│  │  - Hardware Watchdog (10s)                                   │                               │
│  └──────┬───────────────────────────────┬───────────────────────┘                               │
│         │ MUTE_ALL (GPIO13)             │ RELAY_CTRL (GPIO12)                                   ▼
│         │ (10k Pull-down to GND)        │                                                 [ 10A Relay ]
│         ▼                               ▼                                                 (Rail Switch)
│  [ Amp /MUTE Pins ]             [ 2N2222 Driver ──▶ Relay K1 ]                                  │
│                                                                                                 ▼
│  [ Fault Telemetry: GPIO32,33,34 ] ◀────────────────────────────────────────────── [ 6x Polyfuses ]
│  [ DC Offset Sense: GPIO36 ]       ◀────────────────────────────────────────────── [ 2A PTC Bank  ]
│  [ NTC Thermal:     GPIO35 ]       ◀──────────────────────────────────────────────              │
│                                                                                                 ▼
│                                                                                           [ SPEAKERS ]
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Power Supply Block
1. 230V AC passes through fuse $F_1$, varistor $RV_1$, and switch $SW_1$ into toroidal transformer $T_1$.
2. Secondary delivers $18.0\text{V AC}$ to bridge rectifier $BR_1$ (KBU810).
3. Rectified pulsating DC is filtered by $C_1/C_2$ ($9400\,\mu\text{F}$), yielding $V_{CC\_24V\_RAW} = +24.0\text{V DC}$.
4. Rail switch relay $K_1$ controls the delivery of raw power to the amplifier $V_{CC\_24V}$ rail.
5. Buck converter $U_{BUCK}$ (LM2596-5.0) steps $24\text{V}$ down to $+5.0\text{V DC}$ at 85% efficiency for relays and preamps.
6. LDO regulator $U_{LDO}$ (AMS1117-3.3) drops $5.0\text{V}$ to $+3.3\text{V DC}$ for the ESP32, OLED, and digital ICs.
7. Virtual ground splitter $U_{VGND}$ (TLE2426) creates an exact half-rail voltage $\text{VGND\_12V} = 12.0\text{V DC}$ to bias op-amp AC signals.

### 4.2 Pre-Amplifier, Multiplexing & Volume Control
1. Stereo audio from QCC3008, AUX, or USB passes through DC-blocking capacitors ($C_{AC\_IN1 \dots 6}$) and enters dual 4:1 multiplexer $U_{MUX}$ (CD4052).
2. The ESP32 drives `MUX_A` (GPIO26) and `MUX_B` (GPIO27) to select the source.
3. Selected audio passes to digital potentiometer $U_{VOL}$ (MCP4252).
4. Volume adjustments made via the web page, rotary encoder, or IR remote send 16-bit SPI packets to adjust the pot's internal wiper resistance in 256 steps.

### 4.3 Active Crossover & Bass Management
1. **Front Channels:** Filtered by $U_{OP1A}$ (Left) and $U_{OP1B}$ (Right) configured as 2nd-order Sallen-Key high-pass filters ($R = 20\text{k}\Omega$, $C = 100\text{nF}$, $f_c = 79.6\text{ Hz}$). Low bass is removed to prevent distortion in the 200mm woofers.
2. **Surround Channels:** Filtered by $U_{OP3A}$ and $U_{OP3B}$ high-pass filters ($R = 16\text{k}\Omega$, $C = 100\text{nF}$, $f_c = 99.5\text{ Hz}$).
3. **Center Channel:** Summing amplifier $U_{OP2A}$ computes $\frac{\text{Left} + \text{Right}}{2}$, band-passed above $100\text{Hz}$.
4. **Subwoofer Channel:** Summing amplifier $U_{OP2B}$ sums $\text{Left} + \text{Right}$ and feeds a 2nd-order Sallen-Key low-pass filter ($R = 20\text{k}\Omega$, $C = 100\text{nF}$, $f_c = 79.6\text{ Hz}$), routing all sub-80Hz acoustic energy strictly to the 250mm passive subwoofer.

### 4.4 Class-D Power Output Stage
1. Three TPA3116D2 ICs operate in BTL configuration.
2. High-side and low-side power MOSFETs switch at 400kHz.
3. Bootstrap capacitors ($C_{BS1 \dots 12} = 100\text{nF}$) supply the floating gate drive voltage.
4. The high-frequency PWM carrier is reconstructed into a pure audio analog wave via 12× $22\,\mu\text{H}$ inductors and 12× $680\text{nF}$ film capacitors.

### 4.5 Safety & Protection Logic
1. **Mute Control:** Driven by ESP32 pin `MUTE_ALL` (GPIO13). Pulling LOW asserts instant hardware mute.
2. **Relay Control:** Driven by pin `RELAY_CTRL` (GPIO12) via transistor $Q_1$.
3. **DC Offset Sensing:** Speaker terminal voltage is tapped through $100\text{k}\Omega / 10\text{k}\Omega$ dividers into GPIO36 (`DC_OFFSET_ADC`). Any sustained DC voltage $> 500\text{ms}$ initiates emergency shutdown.
4. **Thermal Monitoring:** Heatsink NTC thermistor read via GPIO35 (`NTC_ADC`). Throttles audio at 60°C; cuts power at 80°C.
5. **Hardware Faults:** Amplifier open-drain `/FAULT` pins monitored on GPIO32, GPIO33, and GPIO34.

---

## 5. TEST POINTS & VOLTAGE REFERENCE TABLE

Measure all voltages with a calibrated DMM (Fluke 87V or equivalent) with the black negative probe clipped to system ground (**GND**):

| Test Point | Net Name | Schematic Sheet | Standby Mode | Running (Normal) | Fault / Trip State | Permissible Tolerance |
|---|---|---|---|---|---|---|
| **TP1** | `AC_LIVE` | `power_supply` | 230V AC | 230V AC | 230V AC | $\pm 10\%$ AC RMS |
| **TP2** | `VCC_24V_RAW` | `power_supply` | +24.1V DC | +21.0V to +24.0V | +24.1V DC | $+20.0\text{V to }+25.5\text{V}$ |
| **TP3** | `VCC_24V` | `protection` | 0.0V DC | +20.9V to +24.0V | 0.0V DC | $+20.0\text{V to }+25.5\text{V}$ |
| **TP4** | `VCC_5V` | `power_supply` | +5.02V DC | +5.00V DC | +5.00V DC | $+4.85\text{V to }+5.15\text{V}$ |
| **TP5** | `VCC_3V3` | `power_supply` | +3.31V DC | +3.30V DC | +3.30V DC | $+3.20\text{V to }+3.40\text{V}$ |
| **TP6** | `VGND_12V` | `power_supply` | +12.0V DC | +10.5V to +12.0V | +12.0V DC | $\frac{V_{CC\_24V}}{2} \pm 0.2\text{V}$ |
| **TP7** | `RELAY_CTRL` | `controller` | 0.0V DC (LOW) | +3.3V DC (HIGH) | 0.0V DC (LOW) | Logic High $> 2.8\text{V}$ |
| **TP8** | `MUTE_ALL` | `controller` | 0.0V DC (Muted) | +3.3V DC (Unmuted)| 0.0V DC (Muted) | Logic High $> 2.8\text{V}$ |
| **TP9** | `FAULT1` (IC1) | `amplifier` | +3.3V DC | +3.3V DC (No Fault)| 0.0V DC (Fault) | Open-drain pull-up |
| **TP10**| `FAULT2` (IC2) | `amplifier` | +3.3V DC | +3.3V DC (No Fault)| 0.0V DC (Fault) | Open-drain pull-up |
| **TP11**| `FAULT3` (IC3) | `amplifier` | +3.3V DC | +3.3V DC (No Fault)| 0.0V DC (Fault) | Open-drain pull-up |
| **TP12**| `NTC_ADC` | `protection` | $\sim 1.65\text{V}$ (25°C) | $1.2\text{V to }1.5\text{V}$ (40°C)| $< 0.43\text{V}$ (>80°C) | Temp-dependent divider |
| **TP13**| `DC_OFFSET_ADC`| `protection` | $\sim 0.0\text{V}$ (AC GND) | $< 0.2\text{V DC}$ | $> 1.8\text{V DC}$ (DC Short) | Clamped at 3.3V max |
| **TP14**| `GVDD` (TPA3116)| `amplifier` | 0.0V DC | +5.0V DC | 0.0V DC | Pin 7 internal reg |

---

## 6. OSCILLOSCOPE WAVEFORMS & SIGNAL TRACING

Connect a dual-channel 100MHz digital storage oscilloscope (Rigol DS1054Z or equivalent):

```
WAVEFORM W1: TPA3116D2 SWITCHING OUTPUT (PINS 19, 21, 26, 28)
Probe: 10X attenuation directly on OUTPL / OUTNL before LC inductor
Condition: 24V supply, idle (no audio input)
Timebase: 1.0 µs / div | Sensitivity: 5.0 V / div

      +24V ──┐       ┌───────┐       ┌───────┐
             │       │       │       │       │
             │       │       │       │       │
        0V ──┴───────┘       └───────┘       └───────
             ▲               ▲
             └─ Period: 2.5 µs (Frequency: 400 kHz ± 15 kHz)
             Duty Cycle: 50.0% (BD modulation mode balance)
             Ringing on edges: Must be < 4.0V peak-to-peak
```

```
WAVEFORM W2: RECONSTRUCTED AUDIO SINE WAVE AT SPEAKER TERMINAL
Probe: 1X attenuation across J_SPK1 screw terminals (+ to -)
Condition: 1.0 kHz sine wave input from AUX, Volume = 80%, 6-Ohm load resistor
Timebase: 200 µs / div | Sensitivity: 5.0 V / div

             .-''''-.              .-''''-.
           .'        '.          .'        '.
          /            \        /            \
         ;              ;      ;              ;
        ─┼──────────────┼──────┼──────────────┼── 0V Differential
          \            /        \            /
           '.        .'          '.        .'
             '-....-'              '-....-'
        Peak-to-Peak: 34.6V p-p (Clean, zero crossover distortion, no clipping)
        Residual 400kHz carrier ripple: < 120 mV RMS
```

```
WAVEFORM W3: SUBWOOFER OUTPUT AT 1000 Hz INPUT (FILTER REJECTION)
Probe: 1X on J_SPK6 (Subwoofer output)
Condition: 1000 Hz 1.0V RMS input signal applied to AUX
Timebase: 500 µs / div | Sensitivity: 50 mV / div

        ───────────────────────────────────────── (Flatline)
        Amplitude: < 6.3 mV RMS (-44 dB attenuation relative to passband)
        Verifies 2nd-order active Sallen-Key low-pass filter operation.
```

---

## 7. DIAGNOSTIC TEST MODES & FIRMWARE CLI

The system firmware includes dedicated engineering diagnostic routines accessible without removing the board:

### 7.1 Entering Hardware Diagnostic Mode via Front Panel
1. With the unit powered off, press and hold down the **Rotary Encoder Push Switch**.
2. Switch mains power switch $SW_1$ ON while maintaining pressure on the encoder.
3. Keep holding for 4 seconds until the OLED shows:
   ```
   ====================
   * SERVICE TEST MODE *
   REV: 1.0.0 (DIAG)
   ====================
   ```
4. Release the encoder. Rotating the knob cycles through the test routines:
   - **T1: RELAY & POWER TEST:** Toggles relay $K_1$ on and off at 1Hz rate. Audible click confirms coil and 2N2222 health.
   - **T2: CHANNEL PINK NOISE WALK:** Injects a 440Hz calibration tone through channels sequentially: `FL` $\rightarrow$ `FR` $\rightarrow$ `C` $\rightarrow$ `SUB` $\rightarrow$ `SL` $\rightarrow$ `SR`. Use to identify open voice coils or dead channels.
   - **T3: OLED PIXEL EXERCISE:** Lights 100% of OLED pixels for burn-in and dead row inspection.
   - **T4: SENSOR TELEMETRY STREAM:** Displays continuous live ADC values for `NTC_ADC`, `DC_OFFSET_ADC`, and pin states for `FAULT1`, `FAULT2`, `FAULT3`.

### 7.2 Terminal Command Line Interface (UART Diagnostic Port)
Connect a PC USB-UART adapter to the 6-pin header $J_{PROG}$ ($115200\text{ baud}, 8\text{-N-}1$). Open PuTTY or minicom and enter:

```
> STATUS
OK:STATUS:{"volume":180,"input":"BT","muted":false,"btConnected":true,"temp_c":41.2,"relay":true,"uptime_s":1420}

> PROTECTION
OK:PROT:{"fault_ic1":false,"fault_ic2":false,"fault_ic3":false,"dc_offset_mv":14,"temp_c":41.2,"wdt_resets":0}

> VOL 220
OK:VOL:220

> INPUT AUX
OK:INPUT:AUX

> TEMP?
OK:TEMP:41.2C

> REBOOT
OK:REBOOTING...
```

---

## 8. SYSTEMATIC TROUBLESHOOTING FLOWCHARTS

### 8.1 Condition A: Dead Unit / No Power / No OLED

```
Is AC Line cord plugged in and switch SW1 ON?
  │
  ├── NO  ──▶ Connect power, turn switch ON.
  │
  └── YES ──▶ Check AC mains voltage at J_AC terminals (TP1).
                │
                ├── 0V  ──▶ Check wall socket, cord continuity, power switch SW1.
                │
                └── 230V ─▶ Check fuse F1 (3A 250V).
                              │
                              ├── BLOWN ──▶ Inspect varistor RV1 for carbon charring.
                              │             Check bridge rectifier BR1 for shorted diode.
                              │             Check C1/C2 bulk caps for short circuit.
                              │             REPLACE DEFECTIVE COMPONENT; INSTALL NEW FUSE.
                              │
                              └── INTACT ─▶ Measure VCC_24V_RAW at cathode of BR1 (TP2).
                                            │
                                            ├── 0V  ──▶ Transformer T1 primary/secondary open.
                                            │           Bridge rectifier BR1 open.
                                            │
                                            └── +24V ─▶ Measure VCC_5V at Pin 2 of U_BUCK (TP4).
                                                          │
                                                          ├── 0V  ──▶ LM2596 shorted; L_BUCK open;
                                                          │           D_BUCK Schottky shorted to GND.
                                                          │
                                                          └── +5V ──▶ Measure VCC_3V3 at U_LDO (TP5).
                                                                        │
                                                                        ├── 0V  ──▶ AMS1117-3.3 defective;
                                                                        │           C_LDO_OUT shorted.
                                                                        │
                                                                        └── +3.3V ─▶ Check ESP32 EN pin
                                                                                    (must be +3.3V).
                                                                                    Check OLED 7-pin ribbon.
```

---

### 8.2 Condition B: Unit Enters Protection Lockout / Emergency Shutdown

```
OLED shows "EMERGENCY SHUTDOWN" banner on boot:
  │
  ├── REASON: "THERMAL SHUTDOWN"
  │     │
  │     ├── Check physical heatsink temperature.
  │     │     │
  │     │     ├── COLD (<30°C) ──▶ NTC thermistor broken, disconnected, or
  │     │     │                   pull-up R_NTC_PU (10k) open. Measure TP12.
  │     │     │
  │     │     └── HOT (>80°C)  ──▶ Amplifier thermal runaway.
  │     │                         Check speaker impedance (must be >= 6 Ohm).
  │     │                         Check for shorted speaker wiring.
  │     │                         Ensure thermal pad is installed on TPA3116.
  │
  ├── REASON: "DC OFFSET DETECTED"
  │     │
  │     └── Measure DC voltage at speaker outputs J_SPK1 through J_SPK6.
  │           │
  │           └── ANY TERMINAL HAS > 0.5V DC:
  │                 │
  │                 ├── Output LC filter capacitor (680nF) shorted.
  │                 ├── Bootstrap capacitor (100nF) shorted or leaky.
  │                 └── TPA3116D2 internal MOSFET half-bridge shorted.
  │                     REPLACE AFFECTED TPA3116D2 IC.
  │
  └── REASON: "AMP FAULT: 1 / 2 / 3"
        │
        └── Measure FAULT1 (TP9), FAULT2 (TP10), FAULT3 (TP11).
              │
              └── The pin reading 0.0V DC identifies the faulted IC:
                    ├── Fault 1: IC1 (Front L/R)
                    ├── Fault 2: IC2 (Surround L/R)
                    └── Fault 3: IC3 (Center / Sub)
                    Action: Inspect LC filter inductors for overheating/short.
                            Check speaker wiring for pinch short.
                            Check TPA3116 pin 7 GVDD (must be +5.0V).
```

---

### 8.3 Condition C: No Sound from One or All Channels

```
Unit powers up normally; OLED shows volume bar; no sound:
  │
  ├── Check RELAY_CTRL (TP7) and listen for relay K1 click.
  │     │
  │     ├── NO CLICK / TP7 = 0V ──▶ ESP32 in startup lockout. Inspect serial terminal.
  │     │
  │     └── TP7 = +3.3V / NO CLICK ▶ Transistor Q1 (2N2222) open; flyback diode shorted;
  │                                  Relay K1 coil open. Measure voltage across coil.
  │
  ├── Check MUTE_ALL (TP8).
  │     │
  │     └── TP8 = 0.0V (LOW) ──▶ System is muted in software or hardware pull-down
  │                              R_MUTE_PD is holding rail low due to open MCU pin.
  │
  ├── Check Virtual Ground VGND_12V (TP6).
  │     │
  │     └── TP6 != 12.0V DC ──▶ TLE2426 failure or op-amp NE5532 internal short
  │                             pulling virtual ground to rail.
  │
  └── Is failure isolated to ONE SINGLE CHANNEL?
        │
        ├── YES ──▶ Check polyfuse for that channel (PF1 to PF6) for high resistance.
        │           Normal cold resistance: < 0.15 Ohm.
        │           If blown / high-Z: Voice coil short or excessive sustained volume.
        │           Trace signal from CD4052 -> MCP4252 -> Op-Amp -> TPA3116 input cap.
        │
        └── NO (ALL DEAD) ──▶ CD4052 multiplexer defective or MCP4252 digital pot
                              shutdown pin /SHDN held low.
```

---

### 8.4 Condition D: Audio Distorted, Muffled, or Rattling

```
Distortion observed during playback:
  │
  ├── SATELLITE SPEAKERS SOUND MUFFLED / MUDDY (NO HIGH FREQUENCIES):
  │     │
  │     ├── Check front horn tweeters / surround piezo tweeters in cabinets.
  │     └── Verify NE5532 op-amp feedback resistors R11..R16 on crossover board.
  │
  ├── SATELLITE SPEAKERS RATTLING / CRACKING ON BASS NOTES:
  │     │
  │     └── High-pass filter failed; full bass reaching 100mm/200mm woofers.
  │         Check crossover capacitors C_F1 through C_F12 (100nF) for open circuit.
  │
  ├── SUBWOOFER SOUNDS THIN OR HARSH (VOCALS LEAKING INTO SUB):
  │     │
  │     └── Subwoofer low-pass filter failed; high frequencies passing to sub.
  │         Check op-amp U_OP3B and filter cap C31/C32 for open solder joint.
  │
  └── HARSH "BUZZ" OR "STATIC" AT HIGHER VOLUMES:
        │
        ├── Bulk filter capacitors C1/C2 lost capacitance (excessive 100Hz ripple).
        │   Measure AC ripple at TP2 with oscilloscope. If > 7.0V p-p, replace C1/C2.
        │
        └── Class-D output inductor L1..L12 core cracked or saturated.
            Inspect inductors with thermal camera; saturated inductors run scalding hot.
```

---

### 8.5 Condition E: Bluetooth Pairing / Wi-Fi / OLED Failure

```
Bluetooth will not pair or sound drops out:
  │
  ├── Measure VCC_3V3 on QCC3008 Pin 1 (must be 3.30V).
  ├── Pulse KEY pin (Pin 8) to GND for 3 seconds to force re-pairing.
  └── Relocate external Bluetooth antenna away from toroidal transformer T1.

OLED display blank or corrupted characters:
  │
  ├── Check SPI_SCK (GPIO18) and SPI_MOSI (GPIO23) with oscilloscope for data clock.
  ├── Check OLED reset circuit (pin 5 /RES must be +3.3V).
  └── Inspect 7-pin header for cracked solder joints caused by cable strain.

Wi-Fi SoftAP "Sony5.1-Revival" not visible:
  │
  ├── ESP32 radio initialization failure or brownout.
  ├── Check 10uF tantalum decoupling capacitor on ESP32 3V3 rail.
  └── Reflash firmware binary via PlatformIO.
```

---

## 9. FAIL-SAFE PROTECTION SYSTEM CALIBRATION

The protection subsystem requires verification after replacing any op-amp, TPA3116D2, or ADC-related passive component:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CALIBRATION BENCH TEST SETUP                          │
│                                                                             │
│  [ Adjustable DC Power Supply ] ──▶ 100k Resistor ──▶ Test Point TP13      │
│  [ Fluke 87V Multimeter       ] ──▶ Across Speaker Terminals J_SPK1         │
│  [ Oscilloscope Channel 1     ] ──▶ Pin 12 (RELAY_CTRL)                     │
│  [ Oscilloscope Channel 2     ] ──▶ Pin 13 (MUTE_ALL)                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Procedure 1: DC Offset Trip Threshold Verification
1. Power unit in normal running state (Relay engaged, unmuted).
2. Connect external bench supply ground to system **GND**.
3. Apply $+2.0\text{V DC}$ through a $10\text{k}\Omega$ safety resistor to the speaker terminal positive pin.
4. Verify unit trips into **EMERGENCY SHUTDOWN** within **$150\text{ ms}$**.
5. Observe oscilloscope: `MUTE_ALL` must drop to 0V first, followed by `RELAY_CTRL` dropping to 0V within $100\,\mu\text{s}$.
6. Verify OLED displays: `! ! ! EMERGENCY SHUTDOWN: DC OFFSET DETECTED ! ! !`.

### Procedure 2: Thermal Cutoff Verification
1. Heat the NTC thermistor ring lug gently with a controlled hot air pencil set to 75°C.
2. Monitor terminal output: At $60^\circ\text{C}$, the firmware must reduce volume by $-6\text{ dB}$ (`EVENT:THERMAL_THROTTLE`).
3. Increase hot air until NTC reaches $80^\circ\text{C}$: System must enter immediate emergency shutdown (`EVENT:THERMAL_SHUTDOWN`), releasing relay $K_1$.

---

## 10. CRITICAL COMPONENT REPLACEMENT & SOLDERING GUIDE

### 10.1 Replacing the TPA3116D2 HTSSOP-32 IC
The TPA3116D2 features a large copper thermal slug (PowerPAD) on its underside that is soldered directly to the ground plane:

```
               ┌───────────────────────────────┐
               │         TPA3116D2 IC          │
               │   ┌───────────────────────┐   │
               └───┤  EXPOSED THERMAL PAD  ├───┘
                   └───┬───────────────┬───┘
                       ▼               ▼
          ═════════════╦═══════════════╦═══════════════ PCB TOP LAYER
                       ║  THERMAL VIAS ║
          ═════════════╩═══════════════╩═══════════════ PCB BOTTOM LAYER
```

1. **Removal:**
   - Apply liquid rosin flux generously along both pin rows (Pins 1–16 and 17–32).
   - Preheat the underside of the PCB beneath the IC to $150^\circ\text{C}$ using a bottom preheater.
   - Use a hot air rework station set to $360^\circ\text{C}$ with a medium nozzle, swirling over the package body.
   - When the solder melts on the thermal pad, lift the IC vertically using vacuum tweezers. **Do not pry with dental picks** (will tear surface copper).
2. **Site Preparation:**
   - Clean the pads and thermal area using copper desoldering braid and isopropyl alcohol (IPA).
   - Inspect thermal vias; verify they are open and clear of dross.
3. **Installation:**
   - Apply a micro-layer of lead-free SAC305 solder paste to the center ground pad (do not over-apply; excess paste creates solder balls under pins).
   - Align replacement IC using a stereomicroscope; tack diagonal corner pins (Pin 1 and Pin 17).
   - Reflow with hot air at $350^\circ\text{C}$ until package settles flat onto the thermal pad.
   - Solder peripheral pins using drag soldering technique with a mini-wave / spoon tip.
   - Inspect with 20× microscope: verify zero bridges between pins 16–17 (PVCC) and 20–21 (OUTNR/PGND).

---

## 11. COMPLETE PARTS LIST & OEM CROSS-REFERENCE

| Circuit Ref | Original Component | Package / Case | Function / Rating | OEM Manufacturer | Alternative Cross-Reference |
|---|---|---|---|---|---|
| **U_AMP1..3** | TPA3116D2DADR | HTSSOP-32-1EP | 50W+50W Class-D Amp | Texas Instruments | TI TPA3118D2 (Lower pwr pin-compatible) |
| **U_OP1..3** | NE5532D | SOIC-8 | Dual Low-Noise Op-Amp | Texas Instruments | OPA2134UA, LM4562MA |
| **U_MCU** | ESP32-WROOM-32E | SMD Module | Dual-Core 240MHz MCU | Espressif Systems | ESP32-WROOM-32D |
| **U_BT** | QCC3008 Module | 12-Pin Stamp | Bluetooth 5.0 aptX | Qualcomm | BTM308-C, CSR8675 Module |
| **U_VOL** | MCP4252-103E/SL | SOIC-14 | Dual 10k SPI Digipot | Microchip | MCP4262-103E/SL |
| **U_MUX** | CD4052BM96 | SOIC-16 | Dual 4:1 Analog Mux | Texas Instruments | Nexperia 74HC4052D |
| **U_BUCK** | LM2596S-5.0 | TO-263-5 | 3A 5V Buck Regulator | Texas Instruments | XL2596S-5.0, LM2576S-5.0 |
| **U_LDO** | AMS1117-3.3 | SOT-223 | 1A 3.3V Linear LDO | Advanced Monolithic | TI TLV1117-33CDCYR |
| **U_VGND** | TLE2426CLP | TO-92-3 | Precision Rail Splitter | Texas Instruments | TLE2426CD (SOIC-8) |
| **BR1** | KBU810 | Single-Phase Bridge | 8A 1000V Silicon Rect. | Vishay Semiconductor | GBU810, RS807 |
| **K1** | SRD-05VDC-SL-C | Form A SPST | 5V Coil 10A 250VAC | Songle Relay | Omron G5LE-1-DC5, Panasonic JS1-5V |
| **Q1** | MMBT2222A | SOT-23 | 40V 800mA NPN BJT | ON Semiconductor | 2N2222A (TO-92 THT) |
| **D_FLY** | S1M (1N4007) | SMA (DO-214AC) | 1A 1000V Standard Rect. | Diodes Incorporated | 1N4007G |
| **D_BUCK** | SS34 (1N5822) | SMC (DO-214AB) | 3A 40V Schottky Barrier | Vishay Semiconductor | B340A, SK34 |
| **D_CLAMP** | BZX84C3V3 | SOT-23 | 3.3V 350mW Zener Diode | Nexperia | MMSZ5226B |
| **PF1..PF6** | MF-MSMF200-2 | 1812 SMD | 2.0A Hold / 4.0A Trip PTC | Bourns | Bel Fuse 0ZCG0200FF2C |
| **TH_NTC** | NTC 10k $\beta=3950$ | Ring Lug Terminal | 10k Negative Temp Coeff. | TDK / Murata | Epcos B57861S0103F040 |
| **U_IR** | TSOP1738 | 3-Pin Cast | 38kHz IR Receiver Sensor | Vishay Semiconductor | TSOP4838, VS1838B |
| **DISP1** | 2.42" SSD1309 | 7-Pin Header | 128×64 SPI White OLED | Solomon Systech | Standard UG-2864ASYEG01 |
| **L1..L12** | MSS1210-223MEB | 12×12mm SMD | $22\,\mu\text{H}$ 5.2A Shielded | Coilcraft | Wurth 7447709220 |
| **C1, C2** | ULD1V472MHD | Radial 18×35.5mm | $4700\,\mu\text{F}$ 35V 105°C | Nichicon | Panasonic EEU-FR1V472 |
| **C_O1..12** | MKS4B046803F | Box 7.2×4.5mm | $680\text{ nF}$ 63V Polyprop. | WIMA | KEMET R82DC3680AA60J |
| **C_F1..12** | FKP2C021001D | 5mm Lead Pitch | $100\text{ nF}$ 50V 5% Film | WIMA | Epcos B32529C0104J |
| **F1** | 0217003.HXP | 5×20mm Cartridge | 3.15A 250V Fast-Acting | Littelfuse | Schurter FSF 0034.1521 |
| **RV1** | B72214S0271K101| Disc 14mm | 275V RMS 14D431K MOV | TDK / Epcos | Bourns MOV-14D431K |

---

*Sony® is a registered trademark of Sony Corporation. This manual is an independent engineering repair specification developed for maintenance and restoration of enclosures SS-GN1300D, SS-CT1300D, SS-RSX1300D, and SS-WGV1300D.*  
*Published by Antigravity Engineering Systems. All rights reserved.*
