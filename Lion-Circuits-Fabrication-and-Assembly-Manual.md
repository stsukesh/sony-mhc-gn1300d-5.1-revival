# Sony MHC-GN1300D 5.1 Revival — PCB Fabrication & Assembly Manual

**Target Manufacturer:** Lion Circuits (Bangalore / Chennai, India — https://www.lioncircuits.com/)  
**Project:** Sony MHC-GN1300D 5.1 Custom Audio Hub (Rev 1.0)  
**Board Dimensions:** 150.0 mm × 200.0 mm (2-Layer FR4)  
**Deliverable Archive:** `hardware/sony-5.1-revival/lioncircuits_fab_files.zip` (68 KB)

---

## 1. Fabrication Files Overview

The file [`lioncircuits_fab_files.zip`](file:///run/media/stsukesh/Work/Revive%20SonyAudio%20sytem/hardware/sony-5.1-revival/lioncircuits_fab_files.zip) contains all industry-standard RS-274X Extended Gerbers and Excellon drill files generated directly from KiCad 10:

| Filename | Layer Description | Polarity / Function |
| :--- | :--- | :--- |
| `sony-5.1-revival-Edge_Cuts.gm1` | Board Outline & Cutouts | Board Profile (150×200mm rectangle) |
| `sony-5.1-revival-F_Cu.gtl` | Top Copper Layer (Component Side) | Signal traces, power buses, audio paths |
| `sony-5.1-revival-B_Cu.gbl` | Bottom Copper Layer (Solder Side) | High-current power returns & solid GND plane |
| `sony-5.1-revival-F_Mask.gts` | Top Solder Mask | Green photoimageable solder mask |
| `sony-5.1-revival-B_Mask.gbs` | Bottom Solder Mask | Green photoimageable solder mask |
| `sony-5.1-revival-F_Silkscreen.gto` | Top Silkscreen Legend | Component outlines, zone boxes, pin 1, labels |
| `sony-5.1-revival-B_Silkscreen.gbo` | Bottom Silkscreen Legend | Inspection markers & bottom test labels |
| `sony-5.1-revival-F_Paste.gtp` | Top Solder Paste (SMD Stencil) | Required if ordering laser-cut stainless stencil |
| `sony-5.1-revival-drl.drl` | Excellon NC Drill File | Plated vias, THT component leads & M3 holes |

---

## 2. Step-by-Step Lion Circuits Ordering Process

1. **Visit Lion Circuits:**
   - Go to [https://www.lioncircuits.com/](https://www.lioncircuits.com/) and log in (or create an account with an Indian mobile number & GSTIN/personal address).
2. **Select "Instant PCB Quote":**
   - Click **Get Quote** -> **PCB Fabrication**.
3. **Upload the Zip File:**
   - Drag and drop `lioncircuits_fab_files.zip` into the file uploader.
   - Lion Circuits’ automated DFM engine will analyze the layers and automatically detect:
     - **Width:** 200 mm
     - **Height:** 150 mm
     - **Layer Count:** 2 Layers
4. **Enter Exact Board Specifications:**
   - **Board Type:** Standard Rigid FR-4
   - **Board Thickness:** 1.6 mm (Standard)
   - **Copper Weight:** 1 oz (35 µm) — *sufficient for up to 10A peak with our wide 2.5mm traces*
   - **Solder Mask Color:** Green (Default, fastest turnaround) or Matte Black
   - **Silkscreen Color:** White
   - **Surface Finish:** HASL Lead-Free (RoHS compliant, optimal for hand soldering)
   - **Minimum Track/Spacing:** 8 mil / 8 mil (Our design uses minimum 14 mil signal, 40–100 mil power)
   - **Minimum Hole Size:** 0.8 mm (Our smallest via drill is 0.8 mm; M3 mounting holes are 3.2 mm)
   - **Quantity:** 5 pieces (Standard prototype minimum batch)
5. **Add Laser Stencil (Optional):**
   - If using solder paste and hot-air reflow for the TPA3116D2 ICs (HTSSOP-32) and ESP32:
     - Check **Include Stencil** -> Frameless -> Top Side Only -> Thickness 0.12 mm (5 mil). Cost is typically ₹600–₹800.
6. **Review Quote & Checkout:**
   - **Estimated PCB Fab Cost (5 pcs):** ₹1,500 – ₹2,200 (+ 18% GST).
   - **Turnaround Time:** 3–5 working days (Standard Dispatch via BlueDart/Delhivery inside India).

---

## 3. PCB Physical Partitioning & Component Placement Map

The board layout is organized into 5 isolated functional zones to avoid noise coupling:

```
+---------------------------------------------------------------------------------------------------+
|  [ZONE 1: AC-DC POWER SUPPLY]         [ZONE 2: ANALOG CROSSOVER]      [ZONE 3: ESP32 CONTROL]     |
|                                                                                                   |
|  J_AC (230V In)                       J_AUX (3.5mm)   J_USB_IN        U_MCU (ESP32)  J_OLED (SPI) |
|  F1 (3A Fuse)   RV1 (MOV)             U_BT (QCC3008 aptX)             J_ENC (Rotary) J_CTRL(UART) |
|  BR1 (KBU810 Bridge)                  U_MUX (CD4052)  U_VOL(MCP4252)  U_IR (TSOP)    D_STATUS     |
|  C1, C2 (2x 4700uF/35V Bulk Caps)     U_OP1, U_OP2, U_OP3 (3x NE5532)                             |
|  U_BUCK (LM2596-5V)  U_LDO (3.3V)     Sallen-Key 80Hz RC Filters                                  |
|  U_VGND (TLE2426 12V Rail Splitter)                                                               |
+---------------------------------------------------------------------------------------------------+
|  [ZONE 4: 6-CHANNEL CLASS-D AMPLIFIER]                                [ZONE 5: PROTECTION & OUT]  |
|                                                                                                   |
|  +==================================================================+ K1 (10A 24V Relay)          |
|  |     U_AMP1 (FL/FR)       U_AMP2 (SL/SR)       U_AMP3 (C/SUB)     | Q1 (2N2222)   D_FLY (1N4007)|
|  |     TPA3116D2            TPA3116D2            TPA3116D2          | DC Offset & NTC Sense       |
|  |     [ HEATSINK MOUNTING ZONE: 100mm x 20mm EXTRUDED ALUMINUM ]   |                             |
|  +==================================================================+ PF1-PF6 (6x 2A PTC Fuses)   |
|                                                                       J_SPK_FL   (Front L  +/-)   |
|  L1-L12: 12x 22uH 5A Shielded Toroidal Inductors                      J_SPK_FR   (Front R  +/-)   |
|  C_O1-C_O12: 12x 680nF 63V Low-Loss Film Capacitors                   J_SPK_SL   (Surround L +/-) |
|                                                                       J_SPK_SR   (Surround R +/-) |
|                                                                       J_SPK_C    (Center   +/-)   |
|                                                                       J_SPK_SUB  (Sub      +/-)   |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. Component Sourcing Guide (India)

All components are standard off-the-shelf parts readily available from Indian distributors:

| Component Category | Key Parts | Recommended Indian Source | Est. Cost (INR) |
| :--- | :--- | :--- | :--- |
| **Amplifier ICs** | 3× TPA3116D2 (HTSSOP-32) | Robu.in / Rajiv Electronics / LCSC | ₹750 – ₹900 |
| **Microcontroller** | ESP32-WROOM-32 Module | Robu.in / ElectronicsComp | ₹320 – ₹380 |
| **Op-Amps & Mux** | 3× NE5532, 1× CD4052, 1× MCP4252 | Robu.in / LCSC | ₹350 – ₹500 |
| **Bluetooth Module** | QCC3008 aptX Module | Robu.in / AliExpress / Amazon India | ₹450 – ₹650 |
| **Display & HUD** | 2.42" SSD1309 OLED SPI (White/Yellow) | Robu.in / Amazon India | ₹650 – ₹850 |
| **Power Magnetics** | 12× 22µH 5A SMD Inductors | Robu.in / LCSC | ₹300 – ₹450 |
| **Capacitors** | 2× 4700µF/35V, 12× 680nF film | Robu.in / Rajiv Electronics | ₹450 – ₹600 |
| **Protection** | 1× 10A SPST 5V/24V Relay, 6× 2A PTC | Robu.in / ElectronicsComp | ₹180 – ₹250 |
| **Connectors & Misc** | 6× 2-pin screw terminals, 3-pin AC, jacks | Local store / Robu.in | ₹250 – ₹350 |
| **Toroidal Transformer** | 230V Primary, 18V AC 200VA Secondary | Toroidal India / Miracle Electronic | ₹1,600 – ₹2,200 |
| **TOTAL BOM COST** | | | **₹5,300 – ₹7,130** |

---

## 5. Assembly & Soldering Sequence

To ensure highest yield and prevent heat damage to sensitive ICs:

1. **Step 1: Surface Mount ICs (Top Side)**
   - Solder `U_AMP1`, `U_AMP2`, `U_AMP3` (TPA3116D2). Ensure generous solder on the thermal bottom pad with thermal vias to B.Cu.
   - Solder `U_MCU` (ESP32-WROOM-32), `U_OP1`-`U_OP3` (NE5532), `U_MUX` (CD4052), and `U_VOL` (MCP4252).
   - Solder small SMD resistors (0805) and ceramic decoupling caps (0805).
2. **Step 2: Power Regulators & Inductors**
   - Solder `U_BUCK` (LM2596 TO-263 tab to ground pad), `U_LDO` (AMS1117 SOT-223), and `D_BUCK` (1N5822 Schottky).
   - Solder the 12 shielded inductors `L1`..`L12` and buck inductor `L_BUCK`.
3. **Step 3: Through-Hole Passives & Protection**
   - Solder `F1` fuseholder, `RV1` varistor, and `BR1` KBU810 bridge rectifier.
   - Solder bulk electrolytic caps `C1`, `C2` (observe polarity: white stripe = Negative `-`).
   - Solder `K1` relay, `Q1` 2N2222, and `U_VGND` TLE2426.
4. **Step 4: Connectors & Headers**
   - Solder `J_AC` 3-pin terminal block and `J_AUX` 3.5mm jack.
   - Solder headers `J_OLED`, `J_ENC`, `J_CTRL`, and `U_BT`.
   - Solder the 6 heavy-duty speaker terminal blocks along the right board edge.
5. **Step 5: Heatsink Installation**
   - Apply thin thermal paste (e.g., Arctic MX-4) or a 1.0mm silicone thermal pad across the tops of `U_AMP1`, `U_AMP2`, and `U_AMP3`.
   - Bolt a 100mm × 20mm aluminum finned heatsink over the amplifier zone using M3 screws and insulated washers.

---

## 6. Pre-Flight Electrical Bench Testing

Before connecting speakers or mains 230V AC:

1. **Cold Resistance Checks (Multimeter in Ohms mode):**
   - Measure across `VCC_24V_RAW` to `GND`: must be > 10 kΩ (no direct short).
   - Measure across `VCC_5V` to `GND`: must be > 1 kΩ.
   - Measure across `VCC_3V3` to `GND`: must be > 500 Ω.
2. **Low-Voltage DC Test:**
   - Connect a current-limited bench DC power supply (set to 24V DC, current limit 500 mA) across `VCC_24V_RAW` and `GND`.
   - Check `VCC_5V`: verify 4.95V – 5.05V.
   - Check `VCC_3V3`: verify 3.25V – 3.35V.
   - Check `VGND_12V`: verify 11.8V – 12.2V (exactly half rail).
3. **Firmware & Control Checkout:**
   - ESP32 boots; blue LED flashes heartbeat.
   - 2.42" OLED displays `"SONY 5.1 REVIVAL"`.
   - After 3 seconds startup delay, relay `K1` clicks closed; `MUTE_ALL` transitions from 0V to 3.3V.
   - Measure DC offset on all 6 speaker terminal pairs (+ to -): must be **< 20 mV DC**.
4. **Full System Test:**
   - Connect speakers, connect 230V AC transformer to `J_AC`, pair Bluetooth, and verify rich 5.1 surround sound.
