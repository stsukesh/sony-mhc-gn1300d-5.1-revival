# Sony MHC-GN1300D 5.1 Audio System Revival

[![KiCad 10](https://img.shields.io/badge/KiCad-v10.0-blue.svg)](https://kicad.org)
[![PlatformIO](https://img.shields.io/badge/PlatformIO-ESP32-orange.svg)](https://platformio.org)
[![Lion Circuits](https://img.shields.io/badge/Fabrication-Lion_Circuits_India-green.svg)](https://www.lioncircuits.com)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A complete, production-grade revival and modernization system for the vintage **Sony MHC-GN1300D Mini Hi-Fi Component System** (and similar 5.1 home theater units). 

This project replaces dead, obsolete hybrid IC amplifier boards (STK modules) and failing logic boards with a **single custom 150×200mm 2-layer PCB**, modern high-efficiency Class-D amplification, an active analog crossover, an ESP32 IoT control hub, and a multi-layer hardware-software fail-proof protection engine.

---

## Key System Specifications

| Parameter | Specification |
|---|---|
| **Form Factor** | 150 mm × 200 mm 2-Layer PCB (Lion Circuits India compatible) |
| **Output Channels** | 5.1 Channels (Front L/R, Surround L/R, Center, Subwoofer) |
| **Amplifier ICs** | 3× Texas Instruments TPA3116D2 Class-D stereo amplifiers |
| **Crossover Network** | Analog 2nd-order Sallen-Key active crossover (80 Hz cutoff, 3× NE5532 op-amps) |
| **Microcontroller** | ESP32-WROOM-32 (240 MHz dual-core, WiFi, BLE) |
| **Volume Control** | Microchip MCP4252 SPI 8-bit dual digital potentiometer |
| **Input Selection** | TI CD4052 dual 4:1 multiplexer (Bluetooth, 3.5mm AUX, USB Audio) |
| **Local Interface** | 2.42" SSD1309 SPI OLED (128×64) + Rotary Encoder + TSOP1738 IR Remote |
| **Connectivity** | WiFi AP (`Sony5.1-Revival`) & STA, Web dashboard, REST API, WebSockets, UART CLI |
| **Power Supply** | 230V AC mains input, internal 18V AC toroidal transformer, KBU810 bridge + 2× 4700µF filter (~24V DC), LM2596-5.0 buck, AMS1117-3.3 LDO, TLE2426 virtual ground |
| **Protection** | 5-layer fail-safe: DC offset detect, heatsink NTC thermal sensing, SPST 10A relay, polyfuses, HW pull-downs |
| **Total Build Cost** | ~₹9,124 INR (~$110 USD) — well within ₹10,000 budget |

---

## 5-Layer Fail-Proof Protection Engine

1. **Layer 1 — Hardware Fail-Safe Defaults:**
   - Amps default to hardware-muted via 10kΩ pull-downs on `/MUTE`.
   - Speaker 24V supply is isolated via normally-open relay `K1`. If the ESP32 crashes or loses power, speakers remain 100% silent and protected.
2. **Layer 2 — Hardware Watchdog Timer (TWDT):**
   - 10-second timeout automatically hard-resets the MCU into a safe state if firmware hangs.
3. **Layer 3 — Timed Startup Sequencing:**
   - 3-second power-on delay to stabilize rails, fault pin verification, relay closure, and a 500ms delayed un-mute to completely eliminate turn-on thumps.
4. **Layer 4 — Continuous Runtime ADC Telemetry:**
   - Sub-millivolt DC offset detection on speaker outputs (`GPIO36`).
   - Heatsink thermal monitoring via 10kΩ NTC thermistor (`GPIO35`): auto-attenuation at >60°C, emergency shutdown at >80°C.
   - Continuous latching on all 3 TPA3116D2 `/FAULT` lines (`GPIO32`, `GPIO33`, `GPIO34`).
5. **Layer 5 — Output Polyfuse Current Clamping:**
   - 2A resettable PTC polyfuses in series with speaker outputs to protect against external voice coil shorts.

---

## Repository Structure

```
├── hardware/
│   └── sony-5.1-revival/
│       ├── sony-5.1-revival.kicad_pro      # KiCad 10 Project File
│       ├── sony-5.1-revival.kicad_sch      # Top-level Hierarchical Schematic
│       ├── power_supply.kicad_sch          # Sheet 1: AC-DC, Buck, LDO & Virtual Ground
│       ├── amplifier.kicad_sch             # Sheet 2: 3× TPA3116D2 Class-D Stages
│       ├── crossover_input.kicad_sch       # Sheet 3: CD4052 Mux, MCP4252 Vol & NE5532 Filters
│       ├── controller.kicad_sch            # Sheet 4: ESP32, OLED, Rotary, IR, USB UART
│       ├── protection.kicad_sch            # Sheet 5: Relay, NTC, DC Sense, Screw Terminals
│       ├── sony-5.1-revival.kicad_pcb      # Fully placed & routed 150×200mm 2-layer PCB
│       ├── sony-5.1-revival-schematic.pdf  # Clean multi-page vectorized schematic
│       ├── pcb_preview_top.png             # High-resolution 300 DPI board render
│       ├── BOM.csv                         # Itemized 38-part Bill of Materials (INR)
│       ├── lioncircuits_fab_files.zip      # Ready-to-upload Gerber/Drill manufacturing zip
│       ├── gerbers/                        # Unpacked Gerber and drill files
│       └── libs/                           # Custom KiCad symbol library
├── firmware/
│   ├── platformio.ini                      # PlatformIO build configuration for ESP32
│   ├── src/
│   │   ├── main.cpp                        # System orchestrator and startup sequencing
│   │   ├── config.h                        # System parameters and protection thresholds
│   │   ├── pin_definitions.h               # Complete GPIO & SPI pin map
│   │   ├── audio_controller.cpp / .h       # MCP4252 digital pot and CD4052 mux driver
│   │   ├── display_manager.cpp / .h        # 2.42" SSD1309 OLED graphics engine
│   │   ├── input_handler.cpp / .h          # Rotary encoder (ISR) & NEC IR remote decoder
│   │   ├── protection.cpp / .h             # 5-layer telemetry and emergency shutdown engine
│   │   ├── web_server.cpp / .h             # Async web server, REST API & WebSockets
│   │   ├── serial_cmd.cpp / .h             # 115,200 baud UART command interface
│   │   └── wifi_manager.cpp / .h           # Dual AP/STA WiFi manager with NVS storage
│   └── data/
│       └── index.html                      # Responsive dark-theme browser dashboard
├── tools/                                  # Project automation, simulation & generators
├── MHC-GN1300D-Revival-Master-Plan.md      # Comprehensive architecture & wiring manual
├── Sony-5.1-Revival-Implementation-Report.md # Full design report and telemetry analysis
├── Sony-5.1-Revival-OEM-Service-Manual.md  # OEM-grade repair, schematics & troubleshooting guide
└── Lion-Circuits-Fabrication-and-Assembly-Manual.md # PCB fabrication & bench checkout guide
```

---

## PCB Fabrication Guide (Lion Circuits India)

The board layout is pre-configured and checked against Lion Circuits manufacturing capabilities:

1. Upload `hardware/sony-5.1-revival/lioncircuits_fab_files.zip` directly to [LionCircuits.com](https://www.lioncircuits.com/).
2. Specify the fabrication parameters:
   - **Dimensions:** 150.0 mm × 200.0 mm
   - **Layers:** 2 Layers
   - **PCB Thickness:** 1.6 mm
   - **Copper Weight:** 1 oz (35 µm)
   - **Solder Mask:** Green (or Matte Black)
   - **Silkscreen:** White
   - **Surface Finish:** HASL Lead-Free
3. Minimum trace width used: **0.30 mm** (Signal), **1.00 mm - 3.50 mm** (Power / Speaker).
4. Minimum clearance: **0.25 mm** (High-voltage AC clearance: > 5.0 mm).

---

## Firmware Setup & Flashing

### Prerequisites
- [PlatformIO Core](https://platformio.org/install/cli) or VS Code with PlatformIO IDE extension.
- Micro-USB cable connected to the ESP32 development board.

### Build and Upload
```bash
cd firmware

# Build firmware binary
pio run

# Upload to ESP32 (auto-detects port)
pio run -t upload

# Upload SPIFFS/LittleFS web dashboard assets
pio run -t uploadfs

# Open serial terminal monitor (115200 baud)
pio device monitor -b 115200
```

### Serial Control Interface
Connect any serial terminal at `115200 baud, 8-N-1`:
- `VOL <0-255>`: Set volume directly
- `VOL+` / `VOL-`: Adjust volume up/down by 5 steps
- `INPUT <BT|AUX|USB>`: Switch input audio source
- `MUTE`: Toggle mute
- `POWER`: Toggle 24V amplifier relay
- `STATUS`: Print full JSON telemetry report
- `PROTECTION`: Display ADC offsets, temperatures, and fault latch states

---

## License & Safety Disclaimer

**Mains Voltage Warning:** This design incorporates 230V AC mains input. Always disconnect AC mains before touching any part of the primary side. Use an isolation transformer during bench testing.

Licensed under the [MIT License](LICENSE).
