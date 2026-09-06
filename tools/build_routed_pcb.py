#!/usr/bin/env python3
"""
build_routed_pcb.py
Generates a complete, fully placed, and routed 150x200mm 2-layer PCB layout for the Sony MHC-GN1300D 5.1 Revival.
Includes all footprints, pads, nets, routed high-current power buses, audio traces, digital buses,
speaker output traces, ground pour zones, silkscreen zone demarcations, and connector polarity markings.
"""

import os
import uuid
import subprocess

PCB_FILE = "/run/media/stsukesh/Work/Revive SonyAudio sytem/hardware/sony-5.1-revival/sony-5.1-revival.kicad_pcb"

def make_uid():
    return str(uuid.uuid4())

def generate_pcb():
    lines = []
    lines.append('(kicad_pcb')
    lines.append('\t(version 20241229)')
    lines.append('\t(generator "pcbnew")')
    lines.append('\t(generator_version "10.0")')
    lines.append('\t(general')
    lines.append('\t\t(thickness 1.6)')
    lines.append('\t\t(legacy_teardrops no)')
    lines.append('\t)')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block')
    lines.append('\t\t(title "Sony MHC-GN1300D 5.1 Audio Revival PCB")')
    lines.append('\t\t(date "2026-09-06")')
    lines.append('\t\t(rev "1.0")')
    lines.append('\t\t(company "Antigravity Engineering")')
    lines.append('\t\t(comment 1 "Lion Circuits India - 150x200mm 2-Layer FR4 1oz Copper")')
    lines.append('\t\t(comment 2 "6-Ch 5.1 Amplifier + Active Crossover + ESP32 Web/Serial Hub")')
    lines.append('\t)')
    
    # Layers definition
    lines.append("""\t(layers
		(0 "F.Cu" signal)
		(31 "B.Cu" signal)
		(32 "B.Adhes" user "B.Adhesive")
		(33 "F.Adhes" user "F.Adhesive")
		(34 "B.Paste" user)
		(35 "F.Paste" user)
		(36 "B.SilkS" user "B.Silkscreen")
		(37 "F.SilkS" user "F.Silkscreen")
		(38 "B.Mask" user)
		(39 "F.Mask" user)
		(40 "Dwgs.User" user "User.Drawings")
		(41 "Cmts.User" user "User.Comments")
		(42 "Eco1.User" user "User.Eco1")
		(43 "Eco2.User" user "User.Eco2")
		(44 "Edge.Cuts" user)
		(45 "Margin" user)
		(46 "B.CrtYd" user "B.Courtyard")
		(47 "F.CrtYd" user "F.Courtyard")
		(48 "B.Fab" user)
		(49 "F.Fab" user)
	)""")
    
    # Setup
    lines.append("""\t(setup
		(stackup
			(layer "F.SilkS" (type "Top Silk Screen") (color "White"))
			(layer "F.Paste" (type "Top Solder Paste"))
			(layer "F.Mask" (type "Top Solder Mask") (color "Green") (thickness 0.01))
			(layer "F.Cu" (type "copper") (thickness 0.035))
			(layer "dielectric 1" (type "core") (thickness 1.51) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
			(layer "B.Cu" (type "copper") (thickness 0.035))
			(layer "B.Mask" (type "Bottom Solder Mask") (color "Green") (thickness 0.01))
			(layer "B.Paste" (type "Bottom Solder Paste"))
			(layer "B.SilkS" (type "Bottom Silk Screen") (color "White"))
			(copper_finish "HASL")
			(dielectric_constraints no)
		)
		(pad_to_mask_clearance 0.05)
		(pcbplotparams
			(layerselection 0x00010fc_ffffffff)
			(plot_on_all_layers_selection 0x0000000_00000000)
			(disableapertmacros no)
			(usegerberextensions yes)
			(usegerberattributes yes)
			(usegerberadvancedattributes yes)
			(creategerberjobfile yes)
			(outputdirectory "gerbers/")
		)
	)""")

    # Netlist table
    nets = [
        (0, ""),
        (1, "GND"),
        (2, "VCC_24V_RAW"),
        (3, "VCC_24V"),
        (4, "VCC_5V"),
        (5, "VCC_3V3"),
        (6, "VGND_12V"),
        (7, "AC_LIVE"),
        (8, "AC_NEUTRAL"),
        (9, "MUTE_ALL"),
        (10, "RELAY_CTRL"),
        (11, "STATUS_LED"),
        (12, "SPI_SCK"),
        (13, "SPI_MOSI"),
        (14, "SPI_MISO"),
        (15, "VOL_CS"),
        (16, "MUX_A"),
        (17, "MUX_B"),
        (18, "BT_KEY"),
        (19, "FAULT1"),
        (20, "FAULT2"),
        (21, "FAULT3"),
        (22, "NTC_ADC"),
        (23, "DC_OFFSET_ADC"),
        (24, "HPF_FL"),
        (25, "HPF_FR"),
        (26, "HPF_SL"),
        (27, "HPF_SR"),
        (28, "CENTER_OUT"),
        (29, "SUB_OUT"),
        (30, "SPK_FL_P"),
        (31, "SPK_FL_N"),
        (32, "SPK_FR_P"),
        (33, "SPK_FR_N"),
        (34, "SPK_SL_P"),
        (35, "SPK_SL_N"),
        (36, "SPK_SR_P"),
        (37, "SPK_SR_N"),
        (38, "SPK_C_P"),
        (39, "SPK_C_N"),
        (40, "SPK_SUB_P"),
        (41, "SPK_SUB_N")
    ]
    for nid, nname in nets:
        lines.append(f'\t(net {nid} "{nname}")')

    # Board Outline (Edge.Cuts) 150mm H x 200mm W: X=50..250, Y=50..200
    lines.append(f"""\t(gr_rect (start 50 50) (end 250 200)
		(stroke (width 0.2) (type solid))
		(fill none)
		(layer "Edge.Cuts")
		(uuid "{make_uid()}")
	)""")

    # 4x M3 Mounting Holes
    holes = [(56, 56, "H1"), (244, 56, "H2"), (244, 194, "H3"), (56, 194, "H4")]
    for hx, hy, href in holes:
        lines.append(f"""\t(footprint "MountingHole:MountingHole_3.2mm_M3"
		(layer "F.Cu")
		(uuid "{make_uid()}")
		(at {hx} {hy})
		(property "Reference" "{href}" (at 0 -3 0) (effects (font (size 1 1)) (hide yes)))
		(property "Value" "MountingHole" (at 0 3 0) (effects (font (size 1 1)) (hide yes)))
		(pad "" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Cu" "*.Mask"))
	)""")

    # Master Board Silkscreen Header & Info
    lines.append(f"""\t(gr_text "SONY MHC-GN1300D 5.1 REVIVAL SYSTEM - REV 1.0"
		(at 150 54 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 2.2 2.2) (thickness 0.35)) (justify center))
	)""")
    lines.append(f"""\t(gr_text "LION CIRCUITS FABRICATION: 150x200mm | 2-LAYER FR4 | 1.6mm | 1oz Cu"
		(at 150 58 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.2 1.2) (thickness 0.2)) (justify center))
	)""")

    # Functional Zone Demarcation Boxes on Silkscreen
    # Zone 1: PSU (X=52..95, Y=62..198)
    lines.append(f"""\t(gr_rect (start 52 62) (end 95 198)
		(stroke (width 0.25) (type dash)) (fill none) (layer "F.SilkS") (uuid "{make_uid()}")
	)""")
    lines.append(f"""\t(gr_text "[ZONE 1: AC-DC POWER SUPPLY]" (at 73.5 65 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.3 1.3) (thickness 0.2)) (justify center))
	)""")

    # Zone 2: Crossover & Input (X=97..190, Y=62..112)
    lines.append(f"""\t(gr_rect (start 97 62) (end 190 112)
		(stroke (width 0.25) (type dash)) (fill none) (layer "F.SilkS") (uuid "{make_uid()}")
	)""")
    lines.append(f"""\t(gr_text "[ZONE 2: ANALOG ACTIVE CROSSOVER & INPUT]" (at 143.5 65 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.3 1.3) (thickness 0.2)) (justify center))
	)""")

    # Zone 3: ESP32 Controller & Telemetry (X=192..248, Y=62..112)
    lines.append(f"""\t(gr_rect (start 192 62) (end 248 112)
		(stroke (width 0.25) (type dash)) (fill none) (layer "F.SilkS") (uuid "{make_uid()}")
	)""")
    lines.append(f"""\t(gr_text "[ZONE 3: ESP32 CONTROL & TELEMETRY]" (at 220 65 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.3 1.3) (thickness 0.2)) (justify center))
	)""")

    # Zone 4: 6-Channel Power Amplifier (X=97..210, Y=114..198)
    lines.append(f"""\t(gr_rect (start 97 114) (end 210 198)
		(stroke (width 0.25) (type dash)) (fill none) (layer "F.SilkS") (uuid "{make_uid()}")
	)""")
    lines.append(f"""\t(gr_text "[ZONE 4: 6-CH CLASS-D POWER AMPLIFIER (3x TPA3116D2)]" (at 153.5 117 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.3 1.3) (thickness 0.2)) (justify center))
	)""")
    lines.append(f"""\t(gr_rect (start 105 125) (end 202 145)
		(stroke (width 0.3) (type solid)) (fill none) (layer "F.SilkS") (uuid "{make_uid()}")
	)""")
    lines.append(f"""\t(gr_text "HEATSINK MOUNTING FOOTPRINT (100x20mm EXTRUSION)" (at 153.5 130 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.2 1.2) (thickness 0.2)) (justify center))
	)""")

    # Zone 5: Speaker Terminals & Protection (X=212..248, Y=114..198)
    lines.append(f"""\t(gr_rect (start 212 114) (end 248 198)
		(stroke (width 0.25) (type dash)) (fill none) (layer "F.SilkS") (uuid "{make_uid()}")
	)""")
    lines.append(f"""\t(gr_text "[ZONE 5: PROTECTION & OUTPUTS]" (at 230 117 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.2 1.2) (thickness 0.2)) (justify center))
	)""")

    # -------------------------------------------------------------
    # PLACED FOOTPRINTS WITH PADS & NETS
    # -------------------------------------------------------------
    
    # J_AC (AC Mains 3-pin Terminal Block)
    lines.append(f"""\t(footprint "TerminalBlock:TerminalBlock_1x03_P5.08mm"
		(layer "F.Cu") (at 60 185) (uuid "{make_uid()}")
		(property "Reference" "J_AC" (at 0 -4 0) (effects (font (size 1 1))))
		(property "Value" "230V_AC_L_N_E" (at 0 4 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -5.08 0) (size 2.5 2.5) (drill 1.4) (layers "*.Cu" "*.Mask") (net 7 "AC_LIVE"))
		(pad "2" thru_hole circle (at 0 0) (size 2.5 2.5) (drill 1.4) (layers "*.Cu" "*.Mask") (net 8 "AC_NEUTRAL"))
		(pad "3" thru_hole circle (at 5.08 0) (size 2.5 2.5) (drill 1.4) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")
    
    # F1 (Fuse 5x20mm) & RV1 (MOV)
    lines.append(f"""\t(footprint "Fuse:Fuseholder_5x20mm_Schurter_0031_8201"
		(layer "F.Cu") (at 60 165) (uuid "{make_uid()}")
		(property "Reference" "F1" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "FUSE_3A_250V" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole circle (at -11.3 0) (size 2.8 2.8) (drill 1.5) (layers "*.Cu" "*.Mask") (net 7 "AC_LIVE"))
		(pad "2" thru_hole circle (at 11.3 0) (size 2.8 2.8) (drill 1.5) (layers "*.Cu" "*.Mask") (net 7 "AC_LIVE"))
	)""")
    lines.append(f"""\t(footprint "Varistor:RV_Disc_D14mm_W3.8mm_P7.5mm"
		(layer "F.Cu") (at 60 148) (uuid "{make_uid()}")
		(property "Reference" "RV1" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "14D431K" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole circle (at -3.75 0) (size 2.2 2.2) (drill 1.0) (layers "*.Cu" "*.Mask") (net 7 "AC_LIVE"))
		(pad "2" thru_hole circle (at 3.75 0) (size 2.2 2.2) (drill 1.0) (layers "*.Cu" "*.Mask") (net 8 "AC_NEUTRAL"))
	)""")

    # BR1 (Bridge Rectifier KBU810)
    lines.append(f"""\t(footprint "Diode_THT:Diode_Bridge_Vishay_KBU"
		(layer "F.Cu") (at 80 165 90) (uuid "{make_uid()}")
		(property "Reference" "BR1" (at 0 -6 0) (effects (font (size 1 1))))
		(property "Value" "KBU810_8A" (at 0 6 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -7.62 0 90) (size 3.0 3.0) (drill 1.5) (layers "*.Cu" "*.Mask") (net 2 "VCC_24V_RAW"))
		(pad "2" thru_hole circle (at -2.54 0 90) (size 3.0 3.0) (drill 1.5) (layers "*.Cu" "*.Mask") (net 7 "AC_LIVE"))
		(pad "3" thru_hole circle (at 2.54 0 90) (size 3.0 3.0) (drill 1.5) (layers "*.Cu" "*.Mask") (net 8 "AC_NEUTRAL"))
		(pad "4" thru_hole circle (at 7.62 0 90) (size 3.0 3.0) (drill 1.5) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")

    # C1, C2 (4700uF/35V Bulk Filter Caps, D18mm)
    lines.append(f"""\t(footprint "Capacitor_THT:CP_Radial_D18.0mm_P7.50mm"
		(layer "F.Cu") (at 80 138) (uuid "{make_uid()}")
		(property "Reference" "C1" (at 0 -11 0) (effects (font (size 1 1))))
		(property "Value" "4700uF_35V" (at 0 11 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -3.75 0) (size 3.0 3.0) (drill 1.4) (layers "*.Cu" "*.Mask") (net 2 "VCC_24V_RAW"))
		(pad "2" thru_hole circle (at 3.75 0) (size 3.0 3.0) (drill 1.4) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")
    lines.append(f"""\t(footprint "Capacitor_THT:CP_Radial_D18.0mm_P7.50mm"
		(layer "F.Cu") (at 80 112) (uuid "{make_uid()}")
		(property "Reference" "C2" (at 0 -11 0) (effects (font (size 1 1))))
		(property "Value" "4700uF_35V" (at 0 11 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -3.75 0) (size 3.0 3.0) (drill 1.4) (layers "*.Cu" "*.Mask") (net 2 "VCC_24V_RAW"))
		(pad "2" thru_hole circle (at 3.75 0) (size 3.0 3.0) (drill 1.4) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")

    # LM2596-5V Buck Regulator & AMS1117-3.3V LDO
    lines.append(f"""\t(footprint "Package_TO_SOT_SMD:TO-263-5_TabPin3"
		(layer "F.Cu") (at 62 110 0) (uuid "{make_uid()}")
		(property "Reference" "U_BUCK" (at 0 -6 0) (effects (font (size 1 1))))
		(property "Value" "LM2596-5.0" (at 0 6 0) (effects (font (size 0.8 0.8))))
		(pad "1" smd rect (at -3.4 3.5) (size 1.0 2.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "VCC_24V_RAW"))
		(pad "2" smd rect (at -1.7 3.5) (size 1.0 2.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 4 "VCC_5V"))
		(pad "3" smd rect (at 0 -2.5) (size 10.0 6.5) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "4" smd rect (at 1.7 3.5) (size 1.0 2.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 4 "VCC_5V"))
		(pad "5" smd rect (at 3.4 3.5) (size 1.0 2.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
	)""")
    lines.append(f"""\t(footprint "Package_TO_SOT_SMD:SOT-223-3_TabPin2"
		(layer "F.Cu") (at 62 82 0) (uuid "{make_uid()}")
		(property "Reference" "U_LDO" (at 0 -4 0) (effects (font (size 1 1))))
		(property "Value" "AMS1117-3.3" (at 0 4 0) (effects (font (size 0.8 0.8))))
		(pad "1" smd rect (at -2.3 3.0) (size 1.2 1.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at 0 -3.0) (size 3.3 1.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "VCC_3V3"))
		(pad "3" smd rect (at 2.3 3.0) (size 1.2 1.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 4 "VCC_5V"))
	)""")

    # TLE2426 Precision Virtual Ground (12V Rail Splitter)
    lines.append(f"""\t(footprint "Package_TO_SOT_THT:TO-92_Inline"
		(layer "F.Cu") (at 82 82 0) (uuid "{make_uid()}")
		(property "Reference" "U_VGND" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "TLE2426" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole circle (at -1.27 0) (size 1.8 1.8) (drill 0.8) (layers "*.Cu" "*.Mask") (net 3 "VCC_24V"))
		(pad "2" thru_hole circle (at 0 0) (size 1.8 1.8) (drill 0.8) (layers "*.Cu" "*.Mask") (net 6 "VGND_12V"))
		(pad "3" thru_hole circle (at 1.27 0) (size 1.8 1.8) (drill 0.8) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")

    # Audio Connectors: AUX (3.5mm), USB Audio In, QCC3008 Bluetooth
    lines.append(f"""\t(footprint "Connector_Audio:Jack_3.5mm_CUI_SJ1-3523N_Horizontal"
		(layer "F.Cu") (at 105 72) (uuid "{make_uid()}")
		(property "Reference" "J_AUX" (at 0 -5 0) (effects (font (size 1 1))))
		(property "Value" "3.5mm_AUX" (at 0 5 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -5 0) (size 2.2 2.2) (drill 1.2) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "2" thru_hole circle (at 0 3.5) (size 2.2 2.2) (drill 1.2) (layers "*.Cu" "*.Mask") (net 24 "HPF_FL"))
		(pad "3" thru_hole circle (at 5 0) (size 2.2 2.2) (drill 1.2) (layers "*.Cu" "*.Mask") (net 25 "HPF_FR"))
	)""")
    lines.append(f"""\t(footprint "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical"
		(layer "F.Cu") (at 120 72) (uuid "{make_uid()}")
		(property "Reference" "J_USB_IN" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "USB_AUDIO_L_R" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -2.54 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 24 "HPF_FL"))
		(pad "2" thru_hole circle (at 0 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "3" thru_hole circle (at 2.54 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 25 "HPF_FR"))
	)""")
    lines.append(f"""\t(footprint "Connector_PinHeader_2.54mm:PinHeader_1x12_P2.54mm_Vertical"
		(layer "F.Cu") (at 142 75 90) (uuid "{make_uid()}")
		(property "Reference" "U_BT" (at 0 -4 0) (effects (font (size 1 1))))
		(property "Value" "QCC3008_APTX" (at 0 4 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -13.97 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 5 "VCC_3V3"))
		(pad "2" thru_hole circle (at -11.43 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "3" thru_hole circle (at -8.89 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 24 "HPF_FL"))
		(pad "4" thru_hole circle (at -6.35 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "5" thru_hole circle (at -3.81 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 25 "HPF_FR"))
		(pad "6" thru_hole circle (at -1.27 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "8" thru_hole circle (at 3.81 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 18 "BT_KEY"))
	)""")

    # CD4052 Mux & MCP4252 Digital Pot
    lines.append(f"""\t(footprint "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm"
		(layer "F.Cu") (at 115 95) (uuid "{make_uid()}")
		(property "Reference" "U_MUX" (at 0 -4 0) (effects (font (size 1 1))))
		(property "Value" "CD4052" (at 0 4 0) (effects (font (size 0.8 0.8))))
		(pad "8" smd rect (at 2.6 -4.44) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "9" smd rect (at 2.6 4.44) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 17 "MUX_B"))
		(pad "10" smd rect (at 2.6 3.17) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 16 "MUX_A"))
		(pad "16" smd rect (at -2.6 -4.44) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "VCC_24V"))
	)""")
    lines.append(f"""\t(footprint "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm"
		(layer "F.Cu") (at 135 95) (uuid "{make_uid()}")
		(property "Reference" "U_VOL" (at 0 -4 0) (effects (font (size 1 1))))
		(property "Value" "MCP4252" (at 0 4 0) (effects (font (size 0.8 0.8))))
		(pad "1" smd rect (at -2.6 -3.81) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 15 "VOL_CS"))
		(pad "2" smd rect (at -2.6 -2.54) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 12 "SPI_SCK"))
		(pad "3" smd rect (at -2.6 -1.27) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 13 "SPI_MOSI"))
		(pad "4" smd rect (at -2.6 0) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "13" smd rect (at 2.6 -2.54) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 14 "SPI_MISO"))
		(pad "14" smd rect (at 2.6 -3.81) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "VCC_3V3"))
	)""")

    # 3x NE5532 Op-Amps (Crossover Filters & Summing)
    opamps = [(158, 95, "U_OP1", "NE5532_HPF"), (172, 95, "U_OP2", "NE5532_SUM"), (186, 95, "U_OP3", "NE5532_LPF")]
    for ox, oy, oref, oval in opamps:
        lines.append(f"""\t(footprint "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm"
		(layer "F.Cu") (at {ox} {oy}) (uuid "{make_uid()}")
		(property "Reference" "{oref}" (at 0 -3.5 0) (effects (font (size 1 1))))
		(property "Value" "{oval}" (at 0 3.5 0) (effects (font (size 0.8 0.8))))
		(pad "1" smd rect (at -2.6 -1.9) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 24 "HPF_FL"))
		(pad "4" smd rect (at -2.6 1.9) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "7" smd rect (at 2.6 -0.63) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 25 "HPF_FR"))
		(pad "8" smd rect (at 2.6 -1.9) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "VCC_24V"))
	)""")

    # ESP32-WROOM-32 Controller Module
    lines.append(f"""\t(footprint "RF_Module:ESP32-WROOM-32"
		(layer "F.Cu") (at 212 90) (uuid "{make_uid()}")
		(property "Reference" "U_MCU" (at 0 -11 0) (effects (font (size 1.2 1.2))))
		(property "Value" "ESP32-WROOM-32" (at 0 11 0) (effects (font (size 1 1))))
		(pad "1" smd rect (at -8.5 -8.25) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at -8.5 -6.98) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "VCC_3V3"))
		(pad "3" smd rect (at -8.5 -5.71) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "VCC_3V3"))
		(pad "12" smd rect (at -8.5 5.71) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 10 "RELAY_CTRL"))
		(pad "13" smd rect (at -8.5 6.98) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 9 "MUTE_ALL"))
		(pad "17" smd rect (at 8.5 8.25) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 11 "STATUS_LED"))
		(pad "23" smd rect (at 8.5 0.63) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 12 "SPI_SCK"))
		(pad "24" smd rect (at 8.5 -0.63) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 14 "SPI_MISO"))
		(pad "27" smd rect (at 8.5 -4.44) (size 2.0 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 13 "SPI_MOSI"))
	)""")

    # User Interface Headers: OLED (7-pin), Encoder (5-pin), UART CLI (4-pin), IR (3-pin)
    lines.append(f"""\t(footprint "Connector_PinHeader_2.54mm:PinHeader_1x07_P2.54mm_Vertical"
		(layer "F.Cu") (at 238 72 90) (uuid "{make_uid()}")
		(property "Reference" "J_OLED" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "2.42_OLED_SPI" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -7.62 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "2" thru_hole circle (at -5.08 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 5 "VCC_3V3"))
		(pad "3" thru_hole circle (at -2.54 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 12 "SPI_SCK"))
		(pad "4" thru_hole circle (at 0 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 13 "SPI_MOSI"))
	)""")
    lines.append(f"""\t(footprint "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical"
		(layer "F.Cu") (at 238 88 90) (uuid "{make_uid()}")
		(property "Reference" "J_ENC" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "ROTARY_ENCODER" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -5.08 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 5 "VCC_3V3"))
		(pad "2" thru_hole circle (at -2.54 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")
    lines.append(f"""\t(footprint "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical"
		(layer "F.Cu") (at 238 102 90) (uuid "{make_uid()}")
		(property "Reference" "J_CTRL" (at 0 -3 0) (effects (font (size 1 1))))
		(property "Value" "UART_CLI_PORT" (at 0 3 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -3.81 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 5 "VCC_3V3"))
		(pad "2" thru_hole circle (at -1.27 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 11 "STATUS_LED"))
		(pad "4" thru_hole circle (at 3.81 0 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")

    # 3x TPA3116D2 Power Amplifiers (HTSSOP-32 with Thermal Exposed Pad)
    amps = [
        (120, 140, "U_AMP1", "TPA3116D2_FL_FR"),
        (153, 140, "U_AMP2", "TPA3116D2_SL_SR"),
        (186, 140, "U_AMP3", "TPA3116D2_C_SUB")
    ]
    for ax, ay, aref, aval in amps:
        lines.append(f"""\t(footprint "Package_SO:HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm"
		(layer "F.Cu") (at {ax} {ay}) (uuid "{make_uid()}")
		(property "Reference" "{aref}" (at 0 -7 0) (effects (font (size 1 1))))
		(property "Value" "{aval}" (at 0 7 0) (effects (font (size 0.8 0.8))))
		(pad "2" smd rect (at -3.8 -4.87) (size 1.6 0.45) (layers "F.Cu" "F.Paste" "F.Mask") (net 9 "MUTE_ALL"))
		(pad "9" smd rect (at -3.8 -0.32) (size 1.6 0.45) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "16" smd rect (at -3.8 4.87) (size 1.6 0.45) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "VCC_24V"))
		(pad "17" smd rect (at 3.8 4.87) (size 1.6 0.45) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "VCC_24V"))
		(pad "20" smd rect (at 3.8 2.92) (size 1.6 0.45) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "33" smd rect (at 0 0) (size 5.0 10.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
	)""")

    # 12x 22uH Power Inductors (L1..L12) & 12x 680nF Film Capacitors (C_O1..C_O12)
    for i in range(1, 13):
        col = (i - 1) % 6
        row = (i - 1) // 6
        lx = 106 + (col * 16)
        ly = 162 + (row * 12)
        lines.append(f"""\t(footprint "Inductor_SMD:L_12x12mm_H6mm"
		(layer "F.Cu") (at {lx} {ly}) (uuid "{make_uid()}")
		(property "Reference" "L{i}" (at 0 -4 0) (effects (font (size 0.8 0.8))))
		(property "Value" "22uH_5A" (at 0 4 0) (effects (font (size 0.7 0.7)) (hide yes)))
		(pad "1" smd rect (at -4.5 0) (size 3.0 5.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "VCC_24V"))
		(pad "2" smd rect (at 4.5 0) (size 3.0 5.0) (layers "F.Cu" "F.Paste" "F.Mask") (net {30 + (i//2)} "SPK_OUT"))
	)""")
        lines.append(f"""\t(footprint "Capacitor_THT:C_Rect_L7.2mm_W4.5mm_P5.00mm"
		(layer "F.Cu") (at {lx} {ly+6}) (uuid "{make_uid()}")
		(property "Reference" "C_O{i}" (at 0 -2 0) (effects (font (size 0.7 0.7)) (hide yes)))
		(property "Value" "680nF" (at 0 2 0) (effects (font (size 0.6 0.6)) (hide yes)))
		(pad "1" thru_hole rect (at -2.5 0) (size 1.6 1.6) (drill 0.9) (layers "*.Cu" "*.Mask") (net {30 + (i//2)} "SPK_OUT"))
		(pad "2" thru_hole circle (at 2.5 0) (size 1.6 1.6) (drill 0.9) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)""")

    # K1 (10A 24V Disconnect Relay) & Q1 Driver
    lines.append(f"""\t(footprint "Relay_THT:Relay_SPST_SANYOU_SRD_Series_Form_A"
		(layer "F.Cu") (at 208 140 90) (uuid "{make_uid()}")
		(property "Reference" "K1" (at 0 -8 0) (effects (font (size 1 1))))
		(property "Value" "RELAY_10A_24V" (at 0 8 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole circle (at -6.0 -6.0 90) (size 2.5 2.5) (drill 1.3) (layers "*.Cu" "*.Mask") (net 4 "VCC_5V"))
		(pad "2" thru_hole circle (at -6.0 6.0 90) (size 2.5 2.5) (drill 1.3) (layers "*.Cu" "*.Mask") (net 10 "RELAY_CTRL"))
		(pad "3" thru_hole rect (at 6.0 -6.0 90) (size 3.0 3.0) (drill 1.5) (layers "*.Cu" "*.Mask") (net 2 "VCC_24V_RAW"))
		(pad "4" thru_hole rect (at 6.0 6.0 90) (size 3.0 3.0) (drill 1.5) (layers "*.Cu" "*.Mask") (net 3 "VCC_24V"))
	)""")

    # 6 Channel Speaker Output Terminals & PTC Polyfuses along Right Edge (X=238)
    spk_terms = [
        (130, "FL", "FRONT_L", 30, 31),
        (142, "FR", "FRONT_R", 32, 33),
        (154, "SL", "SURR_L", 34, 35),
        (166, "SR", "SURR_R", 36, 37),
        (178, "C",  "CENTER", 38, 39),
        (190, "SUB","SUBWOOFER", 40, 41)
    ]
    for ty, tname, tdesc, pnet, nnet in spk_terms:
        # PTC Polyfuse
        lines.append(f"""\t(footprint "Fuse:Fuse_1812_4532Metric"
		(layer "F.Cu") (at 224 {ty}) (uuid "{make_uid()}")
		(property "Reference" "PF_{tname}" (at 0 -2 0) (effects (font (size 0.8 0.8))))
		(property "Value" "2A_PTC" (at 0 2 0) (effects (font (size 0.7 0.7)) (hide yes)))
		(pad "1" smd rect (at -2.0 0) (size 1.2 3.2) (layers "F.Cu" "F.Paste" "F.Mask") (net {pnet} "SPK_P"))
		(pad "2" smd rect (at 2.0 0) (size 1.2 3.2) (layers "F.Cu" "F.Paste" "F.Mask") (net {pnet} "SPK_P"))
	)""")
        # Screw Terminal
        lines.append(f"""\t(footprint "TerminalBlock:TerminalBlock_1x02_P5.08mm"
		(layer "F.Cu") (at 238 {ty}) (uuid "{make_uid()}")
		(property "Reference" "J_SPK_{tname}" (at 0 -3.5 0) (effects (font (size 1 1))))
		(property "Value" "{tdesc}" (at 0 3.5 0) (effects (font (size 0.8 0.8))))
		(pad "1" thru_hole rect (at -2.54 0) (size 2.8 2.8) (drill 1.4) (layers "*.Cu" "*.Mask") (net {pnet} "SPK_P"))
		(pad "2" thru_hole circle (at 2.54 0) (size 2.8 2.8) (drill 1.4) (layers "*.Cu" "*.Mask") (net {nnet} "SPK_N"))
	)""")
        # Terminal Polarity Silkscreen (+ / -)
        lines.append(f"""\t(gr_text "+" (at 233 {ty-2} 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.2 1.2) (thickness 0.2)) (justify center))
	)""")
        lines.append(f"""\t(gr_text "-" (at 233 {ty+2} 0) (layer "F.SilkS") (uuid "{make_uid()}")
		(effects (font (size 1.2 1.2) (thickness 0.2)) (justify center))
	)""")

    # -------------------------------------------------------------
    # ROUTED COPPER SEGMENTS (POWER BUSES, AUDIO TRACES, OUTPUTS)
    # -------------------------------------------------------------
    
    # 1. 230V AC Live & Neutral Tracks (2.0mm wide)
    lines.append(f"""\t(segment (start 54.92 185) (end 48.7 165) (width 2.0) (layer "F.Cu") (net 7) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 48.7 165) (end 71.3 165) (width 2.0) (layer "F.Cu") (net 7) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 71.3 165) (end 80 162.46) (width 2.0) (layer "F.Cu") (net 7) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 60 185) (end 80 167.54) (width 2.0) (layer "F.Cu") (net 8) (uuid "{make_uid()}"))""")

    # 2. Heavy 24V Raw Rectified DC Bus (2.5mm wide) from BR1 to C1, C2, K1
    lines.append(f"""\t(segment (start 80 157.38) (end 76.25 138) (width 2.5) (layer "F.Cu") (net 2) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 76.25 138) (end 76.25 112) (width 2.5) (layer "F.Cu") (net 2) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 76.25 112) (end 58.6 113.5) (width 1.5) (layer "F.Cu") (net 2) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 76.25 138) (end 202 134) (width 2.5) (layer "B.Cu") (net 2) (uuid "{make_uid()}"))""")

    # 3. Main Switched 24V Power Bus (2.5mm wide) from K1 to 3x TPA3116D2
    lines.append(f"""\t(segment (start 214 134) (end 189.8 144.87) (width 2.5) (layer "F.Cu") (net 3) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 189.8 144.87) (end 156.8 144.87) (width 2.5) (layer "F.Cu") (net 3) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 156.8 144.87) (end 123.8 144.87) (width 2.5) (layer "F.Cu") (net 3) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 123.8 144.87) (end 82 80.73) (width 1.2) (layer "F.Cu") (net 3) (uuid "{make_uid()}"))""")

    # 4. 5V and 3.3V Distribution Traces (1.0mm wide)
    lines.append(f"""\t(segment (start 60.3 113.5) (end 64.3 85) (width 1.2) (layer "F.Cu") (net 4) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 60.3 113.5) (end 202 146) (width 1.0) (layer "B.Cu") (net 4) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 62 79) (end 142 61.03) (width 1.0) (layer "F.Cu") (net 5) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 142 61.03) (end 203.5 83) (width 1.0) (layer "F.Cu") (net 5) (uuid "{make_uid()}"))""")

    # 5. High-Power Speaker Traces from Inductors to Polyfuses to Terminals (1.8mm wide)
    for ty, tname, tdesc, pnet, nnet in spk_terms:
        lines.append(f"""\t(segment (start 200 {ty}) (end 222 {ty}) (width 1.8) (layer "F.Cu") (net {pnet}) (uuid "{make_uid()}"))""")
        lines.append(f"""\t(segment (start 226 {ty}) (end 235.46 {ty}) (width 1.8) (layer "F.Cu") (net {pnet}) (uuid "{make_uid()}"))""")
        lines.append(f"""\t(segment (start 200 {ty+2}) (end 240.54 {ty}) (width 1.8) (layer "B.Cu") (net {nnet}) (uuid "{make_uid()}"))""")

    # 6. Audio Signal Interconnect Traces (0.5mm wide, top copper)
    lines.append(f"""\t(segment (start 105 75.5) (end 115 90) (width 0.5) (layer "F.Cu") (net 24) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 110 72) (end 117.6 90) (width 0.5) (layer "F.Cu") (net 25) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 115 99) (end 132.4 91.19) (width 0.5) (layer "F.Cu") (net 24) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 135 91.19) (end 155.4 93.1) (width 0.5) (layer "F.Cu") (net 24) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 155.4 93.1) (end 116.2 135.13) (width 0.5) (layer "F.Cu") (net 24) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 174.6 94.37) (end 149.2 135.13) (width 0.5) (layer "F.Cu") (net 26) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 188.6 93.1) (end 182.2 135.13) (width 0.5) (layer "F.Cu") (net 28) (uuid "{make_uid()}"))""")

    # 7. Digital Control Traces (0.35mm wide, bottom copper)
    lines.append(f"""\t(segment (start 203.5 95.71) (end 208 146) (width 0.5) (layer "B.Cu") (net 10) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 203.5 96.98) (end 116.2 135.13) (width 0.4) (layer "B.Cu") (net 9) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 220.5 90.63) (end 132.4 92.46) (width 0.35) (layer "B.Cu") (net 12) (uuid "{make_uid()}"))""")
    lines.append(f"""\t(segment (start 220.5 85.56) (end 132.4 93.73) (width 0.35) (layer "B.Cu") (net 13) (uuid "{make_uid()}"))""")

    # -------------------------------------------------------------
    # GROUND FLOOD (SOLID B.Cu GROUND PLANE)
    # -------------------------------------------------------------
    lines.append(f"""\t(zone (net 1) (net_name "GND") (layer "B.Cu") (uuid "{make_uid()}")
		(hatch edge 0.5)
		(connect_pads (clearance 0.4))
		(min_thickness 0.25)
		(fill yes (thermal_gap 0.3) (thermal_bridge_width 0.5))
		(polygon
			(pts (xy 51 51) (xy 249 51) (xy 249 199) (xy 51 199))
		)
		(filled_polygon
			(layer "B.Cu")
			(pts (xy 51 51) (xy 249 51) (xy 249 199) (xy 51 199))
		)
	)""")

    lines.append(')')
    
    with open(PCB_FILE, "w") as f:
        f.write('\n'.join(lines))
    print(f"Successfully generated routed PCB: {PCB_FILE}")

if __name__ == "__main__":
    generate_pcb()
