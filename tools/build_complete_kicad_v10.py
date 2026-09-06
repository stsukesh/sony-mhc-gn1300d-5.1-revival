import os
import uuid

BASE = "hardware/sony-5.1-revival"
os.makedirs(f"{BASE}/libs", exist_ok=True)

ROOT_UUID = "936307ec-ff2e-4b68-b34e-0a0684a0c8b0"
SHEET_UUIDS = {
    "power_supply": "00000000-0000-0000-0000-000000000001",
    "amplifier": "00000000-0000-0000-0000-000000000002",
    "crossover_input": "00000000-0000-0000-0000-000000000003",
    "controller": "00000000-0000-0000-0000-000000000004",
    "protection": "00000000-0000-0000-0000-000000000005",
}

def make_uid():
    return str(uuid.uuid4())

# Standard Symbol Definitions to embed in (lib_symbols)
LIB_SYMBOLS_COMMON = """
		(symbol "Device:R"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at -1.778 0 90) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Resistor" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "R_0_1"
				(rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "R_1_1"
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:C"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Unpolarized capacitor" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "C_0_1"
				(polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
				(polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
			)
			(symbol "C_1_1"
				(pin passive line (at 0 3.81 270) (length 3.048) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 3.048) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:C_Polarized"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 1.27 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "C_Polarized" (at 1.27 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Polarized capacitor" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "C_Polarized_0_1"
				(polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
				(polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
			)
			(symbol "C_Polarized_1_1"
				(pin passive line (at 0 3.81 270) (length 3.048) (name "+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 3.048) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:L"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "L" (at 1.27 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "L" (at -1.27 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Inductor" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "L_0_1"
				(arc (start 0 -2.54) (mid 1.27 -1.27) (end 0 0) (stroke (width 0.254) (type default)) (fill (type none)))
				(arc (start 0 0) (mid 1.27 1.27) (end 0 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "L_1_1"
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:D"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "D" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Diode" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "D_0_1"
				(polyline (pts (xy -1.27 -1.27) (xy 1.27 0) (xy -1.27 1.27) (xy -1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type outline)))
				(polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "D_1_1"
				(pin passive line (at -3.81 0 0) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Connector:Conn_01x02"
			(pin_numbers (offset 0.254))
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x02" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Generic connector, single row, 01x02" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x02_0_1"
				(rectangle (start -1.27 1.27) (end 1.27 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "Conn_01x02_1_1"
				(pin passive line (at -3.81 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at -3.81 -2.54 0) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Connector:Conn_01x03"
			(pin_numbers (offset 0.254))
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x03" (at 0 -6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "Generic connector, single row, 01x03" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x03_0_1"
				(rectangle (start -1.27 2.54) (end 1.27 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "Conn_01x03_1_1"
				(pin passive line (at -3.81 1.27 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at -3.81 -1.27 0) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin passive line (at -3.81 -3.81 0) (length 2.54) (name "3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "sony-revival:TPA3116D2"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at -15.24 22.86 0) (effects (font (size 1.27 1.27))))
			(property "Value" "TPA3116D2" (at 5.08 22.86 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "Package_SO:HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm" (at 0 -25.4 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "http://www.ti.com/lit/ds/symlink/tpa3116d2.pdf" (at 0 -27.94 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "50W Stereo / 100W Mono Class-D Audio Amplifier, HTSSOP-32" (at 0 -30.48 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "TPA3116D2_0_1"
				(rectangle (start -15.24 20.32) (end 15.24 -22.86) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "TPA3116D2_1_1"
				(pin input line (at -17.78 17.78 0) (length 2.54) (name "MODSEL" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 15.24 0) (length 2.54) (name "~{SD}" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin open_collector line (at -17.78 12.7 0) (length 2.54) (name "~{FAULT}" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 7.62 0) (length 2.54) (name "INPL" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 5.08 0) (length 2.54) (name "INNL" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 0 0) (length 2.54) (name "PLIMIT" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at -17.78 -5.08 0) (length 2.54) (name "GVDD" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -10.16 0) (length 2.54) (name "GAIN" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -25.4 90) (length 2.54) (name "AGND" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -15.24 0) (length 2.54) (name "INNR" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -17.78 0) (length 2.54) (name "INPR" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 17.78 17.78 180) (length 2.54) (name "PVCC" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 17.78 12.7 180) (length 2.54) (name "BSPR" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
				(pin output line (at 17.78 10.16 180) (length 2.54) (name "OUTPR" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 2.54 -25.4 90) (length 2.54) (name "PGND" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
				(pin output line (at 17.78 5.08 180) (length 2.54) (name "OUTNR" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 17.78 2.54 180) (length 2.54) (name "BSNR" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 17.78 -5.08 180) (length 2.54) (name "BSNL" (effects (font (size 1.27 1.27)))) (number "25" (effects (font (size 1.27 1.27)))))
				(pin output line (at 17.78 -7.62 180) (length 2.54) (name "OUTNL" (effects (font (size 1.27 1.27)))) (number "26" (effects (font (size 1.27 1.27)))))
				(pin output line (at 17.78 -12.7 180) (length 2.54) (name "OUTPL" (effects (font (size 1.27 1.27)))) (number "28" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 17.78 -15.24 180) (length 2.54) (name "BSPL" (effects (font (size 1.27 1.27)))) (number "29" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -2.54 -25.4 90) (length 2.54) (name "AVCC" (effects (font (size 1.27 1.27)))) (number "32" (effects (font (size 1.27 1.27)))))
			)
		)
"""

def generate_placed_symbol(lib_id, ref, val, x, y, angle, sheet_path, pin_count=2, footprint="", datasheet=""):
    s_lines = []
    s_lines.append('\t(symbol')
    s_lines.append(f'\t\t(lib_id "{lib_id}")')
    s_lines.append(f'\t\t(at {x:.2f} {y:.2f} {angle})')
    s_lines.append('\t\t(unit 1)')
    s_lines.append('\t\t(exclude_from_sim no)')
    s_lines.append('\t\t(in_bom yes)')
    s_lines.append('\t\t(on_board yes)')
    s_lines.append('\t\t(dnp no)')
    s_lines.append(f'\t\t(uuid "{make_uid()}")')
    s_lines.append(f'\t\t(property "Reference" "{ref}" (at {x+2.54:.2f} {y:.2f} 0) (effects (font (size 1.27 1.27))))')
    s_lines.append(f'\t\t(property "Value" "{val}" (at {x+2.54:.2f} {y-2.54:.2f} 0) (effects (font (size 1.27 1.27))))')
    s_lines.append(f'\t\t(property "Footprint" "{footprint}" (at {x:.2f} {y:.2f} 0) (effects (font (size 1.27 1.27)) (hide yes)))')
    s_lines.append(f'\t\t(property "Datasheet" "{datasheet}" (at {x:.2f} {y:.2f} 0) (effects (font (size 1.27 1.27)) (hide yes)))')
    s_lines.append(f'\t\t(property "Description" "" (at {x:.2f} {y:.2f} 0) (effects (font (size 1.27 1.27)) (hide yes)))')
    
    # pins
    for p in range(1, pin_count + 1):
        s_lines.append(f'\t\t(pin "{p}" (uuid "{make_uid()}"))')
        
    # instances
    s_lines.append('\t\t(instances')
    s_lines.append('\t\t\t(project "sony-5.1-revival"')
    s_lines.append(f'\t\t\t\t(path "{sheet_path}"')
    s_lines.append(f'\t\t\t\t\t(reference "{ref}")')
    s_lines.append('\t\t\t\t\t(unit 1)')
    s_lines.append('\t\t\t\t)')
    s_lines.append('\t\t\t)')
    s_lines.append('\t\t)')
    s_lines.append('\t)')
    return '\n'.join(s_lines)

# 1. BUILD ROOT SCHEMATIC (sony-5.1-revival.kicad_sch)
def build_root_schematic():
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20260306)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "10.0")')
    lines.append(f'\t(uuid "{ROOT_UUID}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block')
    lines.append('\t\t(title "Sony MHC-GN1300D 5.1 System Revival - Master Schematic")')
    lines.append('\t\t(date "2026-09-06")')
    lines.append('\t\t(rev "1.0")')
    lines.append('\t\t(comment 1 "Unified 5.1 Class-D Amp + Active Crossover + ESP32 Web/Serial Hub")')
    lines.append('\t\t(comment 2 "Target Fabrication: Lion Circuits India (150x200mm 2-Layer FR4)")')
    lines.append('\t)')
    lines.append('\t(lib_symbols)')
    
    sheets_info = [
        ("Power Supply Subsystem", "power_supply.kicad_sch", SHEET_UUIDS["power_supply"], 50.8, 50.8),
        ("Amplifier Subsystem", "amplifier.kicad_sch", SHEET_UUIDS["amplifier"], 152.4, 50.8),
        ("Crossover & Input Subsystem", "crossover_input.kicad_sch", SHEET_UUIDS["crossover_input"], 254.0, 50.8),
        ("ESP32 Controller Subsystem", "controller.kicad_sch", SHEET_UUIDS["controller"], 50.8, 127.0),
        ("Protection & Terminals", "protection.kicad_sch", SHEET_UUIDS["protection"], 152.4, 127.0)
    ]
    
    for name, filename, suuid, x, y in sheets_info:
        lines.append('\t(sheet')
        lines.append(f'\t\t(at {x:.2f} {y:.2f})')
        lines.append('\t\t(size 76.2 45.72)')
        lines.append('\t\t(fields_autoplaced yes)')
        lines.append('\t\t(stroke (width 0) (type solid))')
        lines.append('\t\t(fill (color 0 0 0 0.0000))')
        lines.append(f'\t\t(uuid "{suuid}")')
        lines.append(f'\t\t(property "Sheetname" "{name}" (at {x:.2f} {y-2.54:.2f} 0) (effects (font (size 1.524 1.524)) (justify left bottom)))')
        lines.append(f'\t\t(property "Sheetfile" "{filename}" (at {x:.2f} {y+48.26:.2f} 0) (effects (font (size 1.27 1.27)) (justify left top)))')
        lines.append('\t\t(instances')
        lines.append('\t\t\t(project "sony-5.1-revival"')
        lines.append(f'\t\t\t\t(path "/{ROOT_UUID}"')
        lines.append(f'\t\t\t\t\t(page "{name}")')
        lines.append('\t\t\t\t)')
        lines.append('\t\t\t)')
        lines.append('\t\t)')
        lines.append('\t)')
    
    lines.append(')')
    with open(f"{BASE}/sony-5.1-revival.kicad_sch", "w") as f:
        f.write('\n'.join(lines))
    print("Master root schematic built.")

# 2. BUILD POWER SUPPLY SHEET
def build_power_supply_sheet():
    s_uuid = SHEET_UUIDS["power_supply"]
    s_path = f"/{ROOT_UUID}/{s_uuid}"
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20260306)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "10.0")')
    lines.append(f'\t(uuid "{s_uuid}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block (title "Power Supply Subsystem") (date "2026-09-06") (rev "1.0"))')
    lines.append('\t(lib_symbols')
    lines.append(LIB_SYMBOLS_COMMON)
    lines.append('\t)')
    
    # Placed Components
    lines.append(generate_placed_symbol("Connector:Conn_01x03", "J_AC", "230V_MAINS", 60.96, 76.2, 0, s_path, 3, "TerminalBlock:TerminalBlock_1x03_P5.08mm"))
    lines.append(generate_placed_symbol("Device:R", "F1", "FUSE_3A", 88.9, 76.2, 90, s_path, 2, "Fuse:Fuseholder_5x20mm_Schurter_0031_8201"))
    lines.append(generate_placed_symbol("Device:R", "RV1", "14D431K_MOV", 106.68, 88.9, 0, s_path, 2, "Varistor:RV_Disc_D14mm_W3.8mm_P7.5mm"))
    lines.append(generate_placed_symbol("Device:C_Polarized", "C1", "4700uF_35V", 147.32, 76.2, 0, s_path, 2, "Capacitor_THT:CP_Radial_D18.0mm_P7.50mm"))
    lines.append(generate_placed_symbol("Device:C_Polarized", "C2", "4700uF_35V", 162.56, 76.2, 0, s_path, 2, "Capacitor_THT:CP_Radial_D18.0mm_P7.50mm"))
    lines.append(generate_placed_symbol("Device:C", "C3", "100nF_50V", 177.8, 76.2, 0, s_path, 2, "Capacitor_SMD:C_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:C", "C4", "100nF_50V", 190.5, 76.2, 0, s_path, 2, "Capacitor_SMD:C_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:L", "L_BUCK", "33uH_3A", 228.6, 76.2, 90, s_path, 2, "Inductor_SMD:L_12x12mm_H6mm"))
    lines.append(generate_placed_symbol("Device:D", "D_BUCK", "1N5822_Schottky", 215.9, 88.9, 90, s_path, 2, "Diode_SMD:D_SMC"))
    lines.append(generate_placed_symbol("Device:C_Polarized", "C_BUCK_OUT", "220uF_16V", 243.84, 76.2, 0, s_path, 2, "Capacitor_SMD:CP_Elec_8x10.5"))
    lines.append(generate_placed_symbol("Device:C", "C_LDO_IN", "10uF", 279.4, 76.2, 0, s_path, 2, "Capacitor_SMD:C_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:C", "C_LDO_OUT", "22uF", 304.8, 76.2, 0, s_path, 2, "Capacitor_SMD:C_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:C_Polarized", "C_VGND", "100uF_25V", 147.32, 127.0, 0, s_path, 2, "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm"))
    
    # Global Labels
    glabels = [
        ("VCC_24V_RAW", 203.2, 60.96),
        ("VCC_24V", 203.2, 71.12),
        ("VCC_5V", 254.0, 60.96),
        ("VCC_3V3", 317.5, 60.96),
        ("VGND_12V", 165.1, 127.0),
        ("GND", 101.6, 114.3)
    ]
    for lbl, lx, ly in glabels:
        lines.append(f'\t(global_label "{lbl}" (shape bidirectional) (at {lx:.2f} {ly:.2f} 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27)) (justify left)) (uuid "{make_uid()}"))')
        lines.append(f'\t(wire (pts (xy {lx-7.62:.2f} {ly:.2f}) (xy {lx:.2f} {ly:.2f})) (stroke (width 0) (type default)) (uuid "{make_uid()}"))')

    lines.append(')')
    with open(f"{BASE}/power_supply.kicad_sch", "w") as f:
        f.write('\n'.join(lines))
    print("Power supply sheet built.")

# 3. BUILD AMPLIFIER SHEET
def build_amplifier_sheet():
    s_uuid = SHEET_UUIDS["amplifier"]
    s_path = f"/{ROOT_UUID}/{s_uuid}"
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20260306)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "10.0")')
    lines.append(f'\t(uuid "{s_uuid}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block (title "6-Channel Class-D Amplifier Subsystem") (date "2026-09-06") (rev "1.0"))')
    lines.append('\t(lib_symbols')
    lines.append(LIB_SYMBOLS_COMMON)
    lines.append('\t)')
    
    # IC1: Front L/R
    lines.append(generate_placed_symbol("sony-revival:TPA3116D2", "U_AMP1", "TPA3116D2_FL_FR", 101.6, 88.9, 0, s_path, 21, "Package_SO:HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm"))
    # IC2: Surround L/R
    lines.append(generate_placed_symbol("sony-revival:TPA3116D2", "U_AMP2", "TPA3116D2_SL_SR", 203.2, 88.9, 0, s_path, 21, "Package_SO:HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm"))
    # IC3: Center / Subwoofer
    lines.append(generate_placed_symbol("sony-revival:TPA3116D2", "U_AMP3", "TPA3116D2_C_SUB", 304.8, 88.9, 0, s_path, 21, "Package_SO:HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm"))
    
    # Output Reconstruction LC Filters
    for i in range(1, 13):
        col = (i - 1) % 4
        row = (i - 1) // 4
        bx = 88.9 + (row * 101.6) + (col * 17.78)
        lines.append(generate_placed_symbol("Device:L", f"L{i}", "22uH_5A", bx, 139.7, 0, s_path, 2, "Inductor_SMD:L_12x12mm_H6mm"))
        lines.append(generate_placed_symbol("Device:C", f"C_O{i}", "680nF_63V", bx, 157.48, 0, s_path, 2, "Capacitor_THT:C_Rect_L7.2mm_W4.5mm_P5.00mm"))

    lines.append(generate_placed_symbol("Device:R", "R_MUTE_PD", "10k_FAILSAFE", 60.96, 152.4, 0, s_path, 2, "Resistor_SMD:R_0805_2012Metric"))

    amp_labels = [
        ("VCC_24V", 50.8, 50.8),
        ("GND", 50.8, 60.96),
        ("MUTE_ALL", 50.8, 71.12),
        ("FAULT1", 50.8, 81.28),
        ("FAULT2", 50.8, 91.44),
        ("FAULT3", 50.8, 101.6),
        ("HPF_FL", 50.8, 114.3),
        ("HPF_FR", 50.8, 124.46),
        ("HPF_SL", 165.1, 114.3),
        ("HPF_SR", 165.1, 124.46),
        ("CENTER_OUT", 266.7, 114.3),
        ("SUB_OUT", 266.7, 124.46),
        ("SPK_FL_P", 114.3, 177.8),
        ("SPK_FL_N", 127.0, 177.8),
        ("SPK_FR_P", 139.7, 177.8),
        ("SPK_FR_N", 152.4, 177.8),
        ("SPK_SL_P", 215.9, 177.8),
        ("SPK_SL_N", 228.6, 177.8),
        ("SPK_SR_P", 241.3, 177.8),
        ("SPK_SR_N", 254.0, 177.8),
        ("SPK_C_P", 317.5, 177.8),
        ("SPK_C_N", 330.2, 177.8),
        ("SPK_SUB_P", 342.9, 177.8),
        ("SPK_SUB_N", 355.6, 177.8)
    ]
    for lbl, lx, ly in amp_labels:
        lines.append(f'\t(global_label "{lbl}" (shape bidirectional) (at {lx:.2f} {ly:.2f} 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27)) (justify left)) (uuid "{make_uid()}"))')
        lines.append(f'\t(wire (pts (xy {lx-5.08:.2f} {ly:.2f}) (xy {lx:.2f} {ly:.2f})) (stroke (width 0) (type default)) (uuid "{make_uid()}"))')

    lines.append(')')
    with open(f"{BASE}/amplifier.kicad_sch", "w") as f:
        f.write('\n'.join(lines))
    print("Amplifier sheet built.")

# 4. BUILD CROSSOVER & INPUT SHEET
def build_crossover_sheet():
    s_uuid = SHEET_UUIDS["crossover_input"]
    s_path = f"/{ROOT_UUID}/{s_uuid}"
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20260306)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "10.0")')
    lines.append(f'\t(uuid "{s_uuid}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block (title "Active Crossover & Audio Input Stage") (date "2026-09-06") (rev "1.0"))')
    lines.append('\t(lib_symbols')
    lines.append(LIB_SYMBOLS_COMMON)
    lines.append('\t)')
    
    lines.append(generate_placed_symbol("Connector:Conn_01x03", "J_AUX", "3.5mm_STEREO_AUX", 60.96, 76.2, 0, s_path, 3, "Connector_Audio:Jack_3.5mm_CUI_SJ1-3523N_Horizontal"))
    lines.append(generate_placed_symbol("Connector:Conn_01x03", "J_USB_IN", "USB_AUDIO_L_R", 60.96, 101.6, 0, s_path, 3, "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical"))
    
    for c in range(1, 7):
        cx = 127.0 + (c * 20.32)
        lines.append(generate_placed_symbol("Device:R", f"R_F{c}", "20k_1%", cx, 88.9, 0, s_path, 2, "Resistor_SMD:R_0805_2012Metric"))
        lines.append(generate_placed_symbol("Device:C", f"C_F{c}", "100nF_FILM", cx, 114.3, 0, s_path, 2, "Capacitor_THT:C_Rect_L7.2mm_W4.5mm_P5.00mm"))

    cross_labels = [
        ("VCC_24V", 50.8, 50.8),
        ("VGND_12V", 50.8, 60.96),
        ("GND", 50.8, 71.12),
        ("MUX_A", 127.0, 50.8),
        ("MUX_B", 127.0, 60.96),
        ("VOL_CS", 203.2, 50.8),
        ("SPI_SCK", 203.2, 60.96),
        ("SPI_MOSI", 203.2, 71.12),
        ("SPI_MISO", 203.2, 81.28),
        ("HPF_FL", 304.8, 88.9),
        ("HPF_FR", 304.8, 101.6),
        ("HPF_SL", 304.8, 114.3),
        ("HPF_SR", 304.8, 127.0),
        ("CENTER_OUT", 304.8, 139.7),
        ("SUB_OUT", 304.8, 152.4)
    ]
    for lbl, lx, ly in cross_labels:
        lines.append(f'\t(global_label "{lbl}" (shape bidirectional) (at {lx:.2f} {ly:.2f} 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27)) (justify left)) (uuid "{make_uid()}"))')
        lines.append(f'\t(wire (pts (xy {lx-5.08:.2f} {ly:.2f}) (xy {lx:.2f} {ly:.2f})) (stroke (width 0) (type default)) (uuid "{make_uid()}"))')

    lines.append(')')
    with open(f"{BASE}/crossover_input.kicad_sch", "w") as f:
        f.write('\n'.join(lines))
    print("Crossover sheet built.")

# 5. BUILD CONTROLLER SHEET
def build_controller_sheet():
    s_uuid = SHEET_UUIDS["controller"]
    s_path = f"/{ROOT_UUID}/{s_uuid}"
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20260306)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "10.0")')
    lines.append(f'\t(uuid "{s_uuid}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block (title "ESP32 Controller & Telemetry Subsystem") (date "2026-09-06") (rev "1.0"))')
    lines.append('\t(lib_symbols')
    lines.append(LIB_SYMBOLS_COMMON)
    lines.append('\t)')
    
    lines.append(generate_placed_symbol("Connector:Conn_01x03", "J_OLED_PWR", "OLED_PWR_GND_3V3", 76.2, 76.2, 0, s_path, 3, "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical"))
    lines.append(generate_placed_symbol("Connector:Conn_01x03", "J_PROG", "UART_TX_RX_GND", 76.2, 101.6, 0, s_path, 3, "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical"))
    lines.append(generate_placed_symbol("Connector:Conn_01x03", "J_ENC_A_B", "ENCODER_A_B_SW", 76.2, 127.0, 0, s_path, 3, "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical"))
    lines.append(generate_placed_symbol("Device:D", "D_STATUS", "BLUE_LED", 165.1, 76.2, 0, s_path, 2, "LED_SMD:LED_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:R", "R_STATUS", "1k_1%", 180.34, 76.2, 0, s_path, 2, "Resistor_SMD:R_0805_2012Metric"))

    ctrl_labels = [
        ("VCC_5V", 50.8, 50.8),
        ("VCC_3V3", 50.8, 60.96),
        ("GND", 50.8, 71.12),
        ("MUTE_ALL", 127.0, 50.8),
        ("RELAY_CTRL", 127.0, 60.96),
        ("STATUS_LED", 127.0, 71.12),
        ("SPI_SCK", 215.9, 50.8),
        ("SPI_MOSI", 215.9, 60.96),
        ("SPI_MISO", 215.9, 71.12),
        ("VOL_CS", 215.9, 81.28),
        ("MUX_A", 215.9, 91.44),
        ("MUX_B", 215.9, 101.6),
        ("FAULT1", 304.8, 50.8),
        ("FAULT2", 304.8, 60.96),
        ("FAULT3", 304.8, 71.12),
        ("NTC_ADC", 304.8, 88.9),
        ("DC_OFFSET_ADC", 304.8, 101.6)
    ]
    for lbl, lx, ly in ctrl_labels:
        lines.append(f'\t(global_label "{lbl}" (shape bidirectional) (at {lx:.2f} {ly:.2f} 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27)) (justify left)) (uuid "{make_uid()}"))')
        lines.append(f'\t(wire (pts (xy {lx-5.08:.2f} {ly:.2f}) (xy {lx:.2f} {ly:.2f})) (stroke (width 0) (type default)) (uuid "{make_uid()}"))')

    lines.append(')')
    with open(f"{BASE}/controller.kicad_sch", "w") as f:
        f.write('\n'.join(lines))
    print("Controller sheet built.")

# 6. BUILD PROTECTION SHEET
def build_protection_sheet():
    s_uuid = SHEET_UUIDS["protection"]
    s_path = f"/{ROOT_UUID}/{s_uuid}"
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20260306)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "10.0")')
    lines.append(f'\t(uuid "{s_uuid}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block (title "Protection & Output Speaker Terminals") (date "2026-09-06") (rev "1.0"))')
    lines.append('\t(lib_symbols')
    lines.append(LIB_SYMBOLS_COMMON)
    lines.append('\t)')
    
    spk_names = ["FL", "FR", "SL", "SR", "CENTER", "SUB"]
    for i, name in enumerate(spk_names, 1):
        sx = 88.9 + ((i - 1) * 35.56)
        lines.append(generate_placed_symbol("Connector:Conn_01x02", f"J_SPK_{name}", f"SPK_{name}_TERM", sx, 139.7, 0, s_path, 2, "TerminalBlock:TerminalBlock_1x02_P5.08mm"))
        lines.append(generate_placed_symbol("Device:R", f"PF{i}", "2A_PTC_POLYFUSE", sx, 114.3, 90, s_path, 2, "Fuse:Fuse_1812_4532Metric"))

    lines.append(generate_placed_symbol("Device:R", "R_DC1", "100k_1%", 88.9, 76.2, 0, s_path, 2, "Resistor_SMD:R_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:R", "R_DC2", "10k_1%", 106.68, 76.2, 0, s_path, 2, "Resistor_SMD:R_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:C", "C_DC_FILT", "10uF_25V", 124.46, 76.2, 0, s_path, 2, "Capacitor_SMD:C_0805_2012Metric"))
    lines.append(generate_placed_symbol("Device:R", "R_NTC_PU", "10k_0.1%", 165.1, 76.2, 0, s_path, 2, "Resistor_SMD:R_0805_2012Metric"))

    prot_labels = [
        ("VCC_24V_RAW", 50.8, 50.8),
        ("VCC_24V", 50.8, 60.96),
        ("RELAY_CTRL", 50.8, 71.12),
        ("GND", 50.8, 81.28),
        ("NTC_ADC", 180.34, 76.2),
        ("DC_OFFSET_ADC", 139.7, 76.2),
        ("SPK_FL_P", 76.2, 101.6),
        ("SPK_FL_N", 88.9, 101.6),
        ("SPK_FR_P", 114.3, 101.6),
        ("SPK_FR_N", 127.0, 101.6),
        ("SPK_SL_P", 147.32, 101.6),
        ("SPK_SL_N", 160.02, 101.6),
        ("SPK_SR_P", 182.88, 101.6),
        ("SPK_SR_N", 195.58, 101.6),
        ("SPK_C_P", 218.44, 101.6),
        ("SPK_C_N", 231.14, 101.6),
        ("SPK_SUB_P", 254.0, 101.6),
        ("SPK_SUB_N", 266.7, 101.6)
    ]
    for lbl, lx, ly in prot_labels:
        lines.append(f'\t(global_label "{lbl}" (shape bidirectional) (at {lx:.2f} {ly:.2f} 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27)) (justify left)) (uuid "{make_uid()}"))')
        lines.append(f'\t(wire (pts (xy {lx-5.08:.2f} {ly:.2f}) (xy {lx:.2f} {ly:.2f})) (stroke (width 0) (type default)) (uuid "{make_uid()}"))')

    lines.append(')')
    with open(f"{BASE}/protection.kicad_sch", "w") as f:
        f.write('\n'.join(lines))
    print("Protection sheet built.")

build_root_schematic()
build_power_supply_sheet()
build_amplifier_sheet()
build_crossover_sheet()
build_controller_sheet()
build_protection_sheet()
print("All KiCad 10 files successfully generated.")
