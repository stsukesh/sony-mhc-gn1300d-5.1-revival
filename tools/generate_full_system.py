import os
import uuid
import csv

BASE_DIR = "hardware/sony-5.1-revival"
os.makedirs(f"{BASE_DIR}/libs", exist_ok=True)

def uid():
    return str(uuid.uuid4())

def pt(x, y):
    # Align to 1.27 mm grid
    gx = round(x / 1.27) * 1.27
    gy = round(y / 1.27) * 1.27
    return f"{gx:.2f} {gy:.2f}"

# 1. WRITE SYMBOL LIBRARY
with open(f"{BASE_DIR}/libs/sony-revival.kicad_sym", "w") as f:
    f.write("""(kicad_symbol_lib
	(version 20231120)
	(generator "eeschema")
	(generator_version "8.0")
	(symbol "TPA3116D2"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "U" (at -15.24 35.56 0) (effects (font (size 1.27 1.27))))
		(property "Value" "TPA3116D2" (at 5.08 35.56 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Package_SO:HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm" (at 0 -40.64 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "http://www.ti.com/lit/ds/symlink/tpa3116d2.pdf" (at 0 -43.18 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "50W Stereo / 100W Mono Class-D Audio Amplifier, HTSSOP-32" (at 0 -45.72 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "TPA3116D2_0_1"
			(rectangle (start -15.24 33.02) (end 15.24 -38.1) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "TPA3116D2_1_1"
			(pin input line (at -17.78 30.48 0) (length 2.54) (name "MODSEL" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 27.94 0) (length 2.54) (name "~{SD}" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin open_collector line (at -17.78 25.4 0) (length 2.54) (name "~{FAULT}" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 20.32 0) (length 2.54) (name "INPL" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 17.78 0) (length 2.54) (name "INNL" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 12.7 0) (length 2.54) (name "PLIMIT" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			(pin power_out line (at -17.78 7.62 0) (length 2.54) (name "GVDD" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 2.54 0) (length 2.54) (name "GAIN/SLV" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 -40.64 90) (length 2.54) (name "AGND" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 -2.54 0) (length 2.54) (name "INNR" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 -5.08 0) (length 2.54) (name "INPR" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 -10.16 0) (length 2.54) (name "SYNC" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 -12.7 0) (length 2.54) (name "FREQ" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 -15.24 0) (length 2.54) (name "AM1" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
			(pin input line (at -17.78 -17.78 0) (length 2.54) (name "AM0" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 17.78 30.48 180) (length 2.54) (name "PVCC" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 17.78 27.94 180) (length 2.54) (name "PVCC" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 17.78 22.86 180) (length 2.54) (name "BSPR" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
			(pin output line (at 17.78 20.32 180) (length 2.54) (name "OUTPR" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 2.54 -40.64 90) (length 2.54) (name "PGND" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
			(pin output line (at 17.78 15.24 180) (length 2.54) (name "OUTNR" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 17.78 12.7 180) (length 2.54) (name "BSNR" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
			(pin power_out line (at 17.78 7.62 180) (length 2.54) (name "VREG" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
			(pin power_out line (at 17.78 5.08 180) (length 2.54) (name "VCLAMP" (effects (font (size 1.27 1.27)))) (number "24" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 17.78 0 180) (length 2.54) (name "BSNL" (effects (font (size 1.27 1.27)))) (number "25" (effects (font (size 1.27 1.27)))))
			(pin output line (at 17.78 -2.54 180) (length 2.54) (name "OUTNL" (effects (font (size 1.27 1.27)))) (number "26" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 5.08 -40.64 90) (length 2.54) (name "PGND" (effects (font (size 1.27 1.27)))) (number "27" (effects (font (size 1.27 1.27)))))
			(pin output line (at 17.78 -7.62 180) (length 2.54) (name "OUTPL" (effects (font (size 1.27 1.27)))) (number "28" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 17.78 -10.16 180) (length 2.54) (name "BSPL" (effects (font (size 1.27 1.27)))) (number "29" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 17.78 -15.24 180) (length 2.54) (name "PVCC" (effects (font (size 1.27 1.27)))) (number "30" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 17.78 -17.78 180) (length 2.54) (name "PVCC" (effects (font (size 1.27 1.27)))) (number "31" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at -2.54 -40.64 90) (length 2.54) (name "AVCC" (effects (font (size 1.27 1.27)))) (number "32" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 -40.64 90) (length 2.54) (name "EPAD" (effects (font (size 1.27 1.27)))) (number "33" (effects (font (size 1.27 1.27)))))
		)
	)
	(symbol "MCP4252"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "U" (at -10.16 20.32 0) (effects (font (size 1.27 1.27))))
		(property "Value" "MCP4252" (at 5.08 20.32 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm" (at 0 -22.86 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "https://ww1.microchip.com/downloads/en/DeviceDoc/22060b.pdf" (at 0 -25.4 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "7/8-Bit Dual SPI Digital POT with Non-Volatile Memory" (at 0 -27.94 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "MCP4252_0_1"
			(rectangle (start -10.16 17.78) (end 10.16 -20.32) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "MCP4252_1_1"
			(pin input line (at -12.7 15.24 0) (length 2.54) (name "~{CS}" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 12.7 0) (length 2.54) (name "SCK" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 10.16 0) (length 2.54) (name "SDI" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 -22.86 90) (length 2.54) (name "VSS" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 12.7 5.08 180) (length 2.54) (name "P1B" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 12.7 7.62 180) (length 2.54) (name "P1W" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 12.7 10.16 180) (length 2.54) (name "P1A" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 12.7 -5.08 180) (length 2.54) (name "P0A" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 12.7 -7.62 180) (length 2.54) (name "P0W" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 12.7 -10.16 180) (length 2.54) (name "P0B" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 0 0) (length 2.54) (name "~{WP}" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 -2.54 0) (length 2.54) (name "~{SHDN}" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
			(pin output line (at -12.7 -7.62 0) (length 2.54) (name "SDO" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 20.32 270) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
		)
	)
	(symbol "CD4052"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "U" (at -10.16 22.86 0) (effects (font (size 1.27 1.27))))
		(property "Value" "CD4052" (at 5.08 22.86 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm" (at 0 -25.4 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "http://www.ti.com/lit/ds/symlink/cd4052b.pdf" (at 0 -27.94 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "Dual 4-Channel Analog Multiplexer / Demultiplexer" (at 0 -30.48 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "CD4052_0_1"
			(rectangle (start -10.16 20.32) (end 10.16 -22.86) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "CD4052_1_1"
			(pin bidirectional line (at 12.7 15.24 180) (length 2.54) (name "Y0" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 10.16 180) (length 2.54) (name "Y2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at -12.7 12.7 0) (length 2.54) (name "Y_COM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 7.62 180) (length 2.54) (name "Y3" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 12.7 180) (length 2.54) (name "Y1" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 -15.24 0) (length 2.54) (name "INH" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 2.54 -25.4 90) (length 2.54) (name "VEE" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at -2.54 -25.4 90) (length 2.54) (name "VSS" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 -12.7 0) (length 2.54) (name "B" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 -10.16 0) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 -7.62 180) (length 2.54) (name "X3" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 0 180) (length 2.54) (name "X0" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "X_COM" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 -2.54 180) (length 2.54) (name "X1" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
			(pin bidirectional line (at 12.7 -5.08 180) (length 2.54) (name "X2" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 22.86 270) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
		)
	)
	(symbol "QCC3008_MODULE"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "U" (at -10.16 17.78 0) (effects (font (size 1.27 1.27))))
		(property "Value" "QCC3008_MODULE" (at 5.08 17.78 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x12_P2.54mm_Vertical" (at 0 -20.32 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at 0 -22.86 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "Qualcomm QCC3008 Bluetooth 5.0 Audio Module (aptX / aptX-LL)" (at 0 -25.4 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "QCC3008_MODULE_0_1"
			(rectangle (start -10.16 15.24) (end 10.16 -17.78) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "QCC3008_MODULE_1_1"
			(pin power_in line (at 0 17.78 270) (length 2.54) (name "3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 -20.32 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin output line (at 12.7 12.7 180) (length 2.54) (name "AOUTL_P" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			(pin output line (at 12.7 10.16 180) (length 2.54) (name "AOUTL_N" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			(pin output line (at 12.7 5.08 180) (length 2.54) (name "AOUTR_P" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			(pin output line (at 12.7 2.54 180) (length 2.54) (name "AOUTR_N" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			(pin output line (at 12.7 -2.54 180) (length 2.54) (name "SPDIF" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 10.16 0) (length 2.54) (name "KEY" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
			(pin output line (at -12.7 5.08 0) (length 2.54) (name "LED1" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
			(pin output line (at -12.7 2.54 0) (length 2.54) (name "LED2" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
			(pin output line (at -12.7 -7.62 0) (length 2.54) (name "TX" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 -10.16 0) (length 2.54) (name "RX" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
		)
	)
	(symbol "RELAY_SPST"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "K" (at -7.62 10.16 0) (effects (font (size 1.27 1.27))))
		(property "Value" "RELAY_SPST" (at 2.54 10.16 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Relay_THT:Relay_SPST_SANYOU_SRD_Series_Form_A" (at 0 -12.7 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at 0 -15.24 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "SPST Power Relay 10A 250VAC, 5V Coil" (at 0 -17.78 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "RELAY_SPST_0_1"
			(rectangle (start -7.62 7.62) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "RELAY_SPST_1_1"
			(pin passive line (at -10.16 5.08 0) (length 2.54) (name "COIL+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin passive line (at -10.16 -5.08 0) (length 2.54) (name "COIL-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 10.16 5.08 180) (length 2.54) (name "COM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 10.16 -5.08 180) (length 2.54) (name "NO" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
		)
	)
	(symbol "TLE2426"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "U" (at -7.62 10.16 0) (effects (font (size 1.27 1.27))))
		(property "Value" "TLE2426" (at 2.54 10.16 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Package_TO_SOT_THT:TO-92_Inline" (at 0 -12.7 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "http://www.ti.com/lit/ds/symlink/tle2426.pdf" (at 0 -15.24 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "The 'Rail Splitter' Precision Virtual Ground" (at 0 -17.78 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "TLE2426_0_1"
			(rectangle (start -7.62 7.62) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "TLE2426_1_1"
			(pin power_in line (at 0 10.16 270) (length 2.54) (name "IN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin power_out line (at 10.16 0 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 -12.7 90) (length 2.54) (name "COM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
		)
	)
	(symbol "LM2596_5V"
		(in_bom yes)
		(on_board yes)
		(property "Reference" "U" (at -10.16 12.7 0) (effects (font (size 1.27 1.27))))
		(property "Value" "LM2596_5V" (at 2.54 12.7 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 -15.24 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "http://www.ti.com/lit/ds/symlink/lm2596.pdf" (at 0 -17.78 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "SIMPLE SWITCHER 3A Step-Down Voltage Regulator, 5.0V Output" (at 0 -20.32 0) (effects (font (size 1.27 1.27)) hide))
		(symbol "LM2596_5V_0_1"
			(rectangle (start -10.16 10.16) (end 10.16 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
		)
		(symbol "LM2596_5V_1_1"
			(pin power_in line (at -12.7 7.62 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin power_out line (at 12.7 7.62 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			(pin power_in line (at 0 -15.24 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			(pin input line (at 12.7 -5.08 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			(pin input line (at -12.7 -5.08 0) (length 2.54) (name "~{ON}/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
		)
	)
)
""")

print("Symbols written.")

# Helper to format a complete sub-sheet
def make_sheet(title, notes, labels, components_desc):
    lines = []
    lines.append('(kicad_sch')
    lines.append('\t(version 20231120)')
    lines.append('\t(generator "eeschema")')
    lines.append('\t(generator_version "8.0")')
    lines.append(f'\t(uuid "{uid()}")')
    lines.append('\t(paper "A3")')
    lines.append('\t(title_block')
    lines.append(f'\t\t(title "{title}")')
    lines.append('\t\t(date "2026-09-06")')
    lines.append('\t\t(rev "1.0")')
    lines.append('\t\t(comment 1 "Sony MHC-GN1300D 5.1 System Revival")')
    lines.append('\t\t(comment 2 "Lion Circuits 2-Layer 150x200mm Fab")')
    lines.append('\t)')
    lines.append('\t(lib_symbols)')
    
    # Place text notes
    y_text = 40.64
    lines.append(f'\t(text "{notes}"')
    lines.append(f'\t\t(at 30.48 {y_text:.2f} 0)')
    lines.append('\t\t(effects')
    lines.append('\t\t\t(font (size 1.524 1.524))')
    lines.append('\t\t\t(justify left top)')
    lines.append('\t\t)')
    lines.append(f'\t\t(uuid "{uid()}")')
    lines.append('\t)')

    # Place components description block
    y_comp = 80.0
    lines.append(f'\t(text "{components_desc}"')
    lines.append(f'\t\t(at 30.48 {y_comp:.2f} 0)')
    lines.append('\t\t(effects')
    lines.append('\t\t\t(font (size 1.27 1.27))')
    lines.append('\t\t\t(justify left top)')
    lines.append('\t\t)')
    lines.append(f'\t\t(uuid "{uid()}")')
    lines.append('\t)')

    # Place global labels connected with wires
    start_x = 240.0
    start_y = 50.0
    spacing = 7.62
    for i, (lbl_name, lbl_shape) in enumerate(labels):
        pos_y = round((start_y + i * spacing) / 1.27) * 1.27
        wx1 = round((start_x - 12.7) / 1.27) * 1.27
        wx2 = round(start_x / 1.27) * 1.27
        
        # Wire
        lines.append('\t(wire')
        lines.append(f'\t\t(pts (xy {wx1:.2f} {pos_y:.2f}) (xy {wx2:.2f} {pos_y:.2f}))')
        lines.append('\t\t(stroke (width 0) (type default))')
        lines.append(f'\t\t(uuid "{uid()}")')
        lines.append('\t)')
        
        # Global label
        lines.append(f'\t(global_label "{lbl_name}"')
        lines.append(f'\t\t(shape {lbl_shape})')
        lines.append(f'\t\t(at {wx2:.2f} {pos_y:.2f} 0)')
        lines.append('\t\t(fields_autoplaced yes)')
        lines.append('\t\t(effects')
        lines.append('\t\t\t(font (size 1.27 1.27))')
        lines.append('\t\t\t(justify left)')
        lines.append('\t\t)')
        lines.append(f'\t\t(uuid "{uid()}")')
        lines.append('\t)')
        
    lines.append(')')
    return '\n'.join(lines)

# 2. POWER SUPPLY SHEET
psu_notes = """POWER SUPPLY ARCHITECTURE:
- AC Input: 230V AC 50Hz with 3A Fast-Blow Fuse + 275V 14D431K MOV Surge Suppressor + SPST Switch
- Transformer: 230V : 18V AC 200VA Toroidal Transformer
- Rectifier: KBU810 8A 1000V Silicon Bridge Rectifier
- Unregulated Rail: VCC_24V_RAW (~25.4V peak DC unloaded, 22.8V at full 6A load)
- Primary Smoothing: 2x 4700uF 35V Low-ESR Electrolytic + 2x 100nF High-Frequency Decoupling
- 5V Auxiliary Rail: LM2596-5.0 Buck Regulator (33uH 3A Inductor, 1N5822 Schottky, 220uF output)
- 3.3V Digital Rail: AMS1117-3.3 Linear LDO (Fed from 5V rail to minimize thermal dissipation)
- Virtual Ground: TLE2426 Precision Rail Splitter generating VGND_12V (VCC_24V / 2) with 100uF buffer
"""

psu_components = """CIRCUIT COMPONENTS & DESIGN VALUES:
- J_AC: 3-Pin Screw Terminal (Live, Neutral, Earth) [5.08mm pitch]
- F1: 3A 250V 5x20mm Cartridge Fuse in PCB clips
- RV1: 14D431K Varistor (Clamping at 430V, 275V RMS continuous)
- BR1: KBU810 Bridge Rectifier (8A max, 1000V PIV)
- C1, C2: 4700uF 35V 105C Radial Electrolytic Capacitors (Ripple rating > 2.8A)
- C3, C4: 100nF 50V X7R 0805 MLCC
- U_BUCK: LM2596-5.0 TO-263-5 Step-down Regulator
- L_BUCK: 33uH 3A High-Current Shielded Inductor
- D_BUCK: 1N5822 3A 40V Schottky Barrier Diode
- C_BUCK_IN: 100uF 35V Electrolytic + 100nF Ceramic
- C_BUCK_OUT: 220uF 16V Low-ESR Electrolytic
- U_LDO: AMS1117-3.3 SOT-223 Linear Regulator
- C_LDO_IN: 10uF 16V 0805 MLCC
- C_LDO_OUT: 22uF 10V 0805 MLCC
- U_VGND: TLE2426 TO-92 Virtual Ground Generator
- C_VGND: 100uF 25V Electrolytic + 100nF 0805 MLCC
- D_PWR: 3mm Green LED + 1k 0805 Resistor (5V rail indicator)
"""

psu_labels = [
    ("AC_LIVE", "input"),
    ("AC_NEUTRAL", "input"),
    ("EARTH", "input"),
    ("VCC_24V_RAW", "output"),
    ("VCC_24V", "bidirectional"),
    ("VCC_5V", "output"),
    ("VCC_3V3", "output"),
    ("VGND_12V", "output"),
    ("GND", "bidirectional")
]

with open(f"{BASE_DIR}/power_supply.kicad_sch", "w") as f:
    f.write(make_sheet("Power Supply Subsystem", psu_notes, psu_labels, psu_components))

# 3. AMPLIFIER SHEET
amp_notes = """AMPLIFICATION SUBSYSTEM: 6 CHANNELS VIA 3x TI TPA3116D2
- Topology: Class-D Bridge-Tied Load (BTL) for high efficiency (>90%) and zero DC offset across voice coils
- IC1 (Front Left & Front Right):
  * Drives SS-GN1300D 6-Ohm 200mm Woofers + Horn Tweeters
  * Gain configured for 26dB (GAIN0=0, GAIN1=1)
  * Output: 50W+50W clean into 6 Ohms at 24V supply
- IC2 (Surround Left & Surround Right):
  * Drives SS-RSX1300D 6-Ohm 100mm Satellites + Piezo Tweeters
  * Gain configured for 20dB (GAIN0=0, GAIN1=0)
  * Output: 35W+35W clean into 6 Ohms
- IC3 (Center & Subwoofer):
  * Channel A: Drives SS-CT1300D (Dual 80mm full-range cone, 6 Ohms, 26dB Gain)
  * Channel B: Drives SS-WGV1300D (250mm cone subwoofer, 8 Ohms, 26dB Gain)
  * High-current bootstrap capacitors and dedicated copper heatsink plane
- Protection & Controls:
  * Master Mute: Active-Low /MUTE tied to MUTE_ALL with 10k Hardware Pull-down to GND
  * Fault Detection: Open-drain /FAULT pins pulled up to 3.3V, connected to FAULT1, FAULT2, FAULT3
  * AM Avoidance / Frequency Setting: Configured for 400kHz switching frequency
"""

amp_components = """CIRCUIT COMPONENTS & RECONSTRUCTION FILTERS:
- U_AMP1: TPA3116D2 HTSSOP-32 (Front L/R)
- U_AMP2: TPA3116D2 HTSSOP-32 (Surround L/R)
- U_AMP3: TPA3116D2 HTSSOP-32 (Center & Subwoofer)
- L1..L12: 22uH 5A Shielded Inductors for Class-D LC output reconstruction
- C_O1..C_O12: 680nF 63V Metallized Polypropylene Film Capacitors
- C_BS1..C_BS12: 100nF 50V X7R 0805 Bootstrap Capacitors (between BST and OUT pins)
- C_IN1..C_IN6: 1.0uF 50V Polyester Film DC-Blocking Input Capacitors
- R_IN1..R_IN6: 20k 1% 0805 Input Bias Resistors
- C_BULK1..C_BULK3: 1000uF 35V Low-ESR Radial Capacitors (one per IC PVCC pin)
- C_DEC1..C_DEC6: 100nF 50V X7R 0805 Local Decoupling Capacitors
- C_GVDD1..C_GVDD3: 1.0uF 16V 0805 Decoupling on pin 7
- R_MUTE_PD: 10k 1% 0805 Pull-down resistor on MUTE_ALL (HARDWARE FAIL-SAFE)
- R_FLT_PU1..3: 10k 1% 0805 Pull-up resistors on FAULT1, FAULT2, FAULT3 to VCC_3V3
"""

amp_labels = [
    ("VCC_24V", "input"),
    ("VCC_3V3", "input"),
    ("GND", "bidirectional"),
    ("MUTE_ALL", "input"),
    ("FAULT1", "output"),
    ("FAULT2", "output"),
    ("FAULT3", "output"),
    ("HPF_FL", "input"),
    ("HPF_FR", "input"),
    ("HPF_SL", "input"),
    ("HPF_SR", "input"),
    ("CENTER_OUT", "input"),
    ("SUB_OUT", "input"),
    ("SPK_FL_P", "output"),
    ("SPK_FL_N", "output"),
    ("SPK_FR_P", "output"),
    ("SPK_FR_N", "output"),
    ("SPK_SL_P", "output"),
    ("SPK_SL_N", "output"),
    ("SPK_SR_P", "output"),
    ("SPK_SR_N", "output"),
    ("SPK_C_P", "output"),
    ("SPK_C_N", "output"),
    ("SPK_SUB_P", "output"),
    ("SPK_SUB_N", "output")
]

with open(f"{BASE_DIR}/amplifier.kicad_sch", "w") as f:
    f.write(make_sheet("Amplifier Subsystem", amp_notes, amp_labels, amp_components))

# 4. CROSSOVER & INPUT SHEET
cross_notes = """ANALOG ACTIVE CROSSOVER, MULTIPLEXER & DIGITAL VOLUME CONTROL:
- Audio Input Stage:
  * Bluetooth: Qualcomm QCC3008 aptX audio module (AOUTL, AOUTR)
  * AUX: 3.5mm Gold-Plated Stereo Jack with 10k bias to VGND_12V
  * USB Audio: 5-Pin Header for external USB FLAC/MP3 decoder module
- Input Selector: CD4052 Dual 4-Channel Analog Multiplexer
  * Controlled by ESP32 via MUX_A and MUX_B lines
  * Biased to VGND_12V virtual ground rail for single-supply 24V operation
- Master Volume Attenuator: Microchip MCP4252 Dual SPI Digital Potentiometer
  * 8-Bit resolution (256 logarithmic steps), zero click/pop transient
  * Controlled via SPI bus (SCK, MOSI, MISO, VOL_CS)
- Active Crossover Filter Network (3x TI NE5532 Low-Noise Dual Op-Amps):
  * Front L/R: 2nd-Order Sallen-Key High-Pass Filter @ 80 Hz, Q=0.707 (Butterworth)
    R1=R2=20k, C1=C2=100nF -> fc = 1 / (2*pi*R*C) = 79.6 Hz
  * Surround L/R: 2nd-Order Sallen-Key High-Pass Filter @ 100 Hz, Q=0.707
    R1=R2=16k, C1=C2=100nF -> fc = 99.5 Hz
  * Center Channel: Active Inverting Summing Amplifier (L+R)/2 followed by 100Hz HPF
  * Subwoofer Channel: Active Inverting Summing Amplifier (L+R) followed by
    2nd-Order Sallen-Key Low-Pass Filter @ 80 Hz, Q=0.707
    R1=R2=20k, C1=C2=100nF -> fc = 79.6 Hz
"""

cross_components = """CIRCUIT COMPONENTS & OP-AMP TOPOLOGY:
- U_MUX: CD4052 SOIC-16 Dual 4:1 Multiplexer
- U_VOL: MCP4252 SOIC-14 Dual Digital Potentiometer (10k end-to-end)
- U_BT: QCC3008 Bluetooth 5.0 Module on 2.54mm Header
- J_AUX: 3.5mm Stereo Audio Jack (CUI Devices SJ1-3523N)
- J_USB: 5-Pin 2.54mm Header (5V, GND, USB_L, USB_R, GND)
- U_OP1: NE5532 SOIC-8 (Front L & Front R Sallen-Key HPF @ 80Hz)
- U_OP2: NE5532 SOIC-8 (Center Summing Buffer & Subwoofer Summing Buffer)
- U_OP3: NE5532 SOIC-8 (Surround L/R HPF @ 100Hz & Subwoofer Sallen-Key LPF @ 80Hz)
- C_F1..C_F12: 100nF 5% Metallized Film / C0G Ceramic Filter Capacitors
- R_F1..R_F16: 20k / 16k / 10k 1% 0805 Precision Metal Film Resistors
- C_AC_IN1..6: 2.2uF 50V AC Coupling Capacitors
- C_OP_DEC1..3: 100nF 50V X7R 0805 Power Decoupling on each op-amp VCC pin
"""

cross_labels = [
    ("VCC_24V", "input"),
    ("VCC_5V", "input"),
    ("VCC_3V3", "input"),
    ("VGND_12V", "input"),
    ("GND", "bidirectional"),
    ("SPI_SCK", "input"),
    ("SPI_MOSI", "input"),
    ("SPI_MISO", "output"),
    ("VOL_CS", "input"),
    ("MUX_A", "input"),
    ("MUX_B", "input"),
    ("BT_KEY", "input"),
    ("HPF_FL", "output"),
    ("HPF_FR", "output"),
    ("HPF_SL", "output"),
    ("HPF_SR", "output"),
    ("CENTER_OUT", "output"),
    ("SUB_OUT", "output")
]

with open(f"{BASE_DIR}/crossover_input.kicad_sch", "w") as f:
    f.write(make_sheet("Crossover & Input Subsystem", cross_notes, cross_labels, cross_components))

# 5. CONTROLLER SHEET
ctrl_notes = """EMBEDDED CONTROLLER SUBSYSTEM: ESP32-WROOM-32
- Brain: Espressif ESP32-WROOM-32 Dual-Core Xtensa LX6 (240MHz, 520KB SRAM, 4MB Flash)
- User Interfaces:
  * 2.42-inch 128x64 SPI OLED Display (SSD1309 Driver) via 7-Pin Plug-and-Play Header
  * Optical/Mechanical Rotary Encoder with Integrated Pushbutton for Volume & Source Select
  * Vishay TSOP1738 38kHz IR Receiver for Wireless Remote Control
- Connectivity & Remote Control Port:
  * Wi-Fi SoftAP ('Sony5.1-Revival') + Web Server with REST API & WebSockets
  * USB-UART Serial Interface (115200 baud) for Direct Terminal Control
- Telemetry & System Health:
  * GPIO35 (NTC_ADC): Continuous thermal monitoring of main amplifier heatsink
  * GPIO36 (DC_OFFSET_ADC): Continuous sampling of speaker DC offset
  * GPIO32/33/34: Dedicated fault interrupt lines for TPA3116D2 ICs
  * Hardware Watchdog Timer (TWDT) enabled at 10-second timeout
"""

ctrl_components = """CIRCUIT COMPONENTS & INTERFACES:
- U_MCU: ESP32-WROOM-32 Module
- J_OLED: 7-Pin 2.54mm Female Header (GND, 3V3, SCK, MOSI, RES, DC, CS)
- J_ENC: 5-Pin 2.54mm Header (A, B, SW, 3V3, GND) with 10k pullups & 100nF filter
- U_IR: TSOP1738 38kHz Infrared Receiver with 100R/100nF RC power filter
- J_PROG: 6-Pin Header (3V3, TX0, RX0, GND, IO0, EN) for flashing & serial control
- SW_BOOT: Tactile Pushbutton for manual bootloader entry
- SW_RESET: Tactile Pushbutton for manual hardware reset
- D_STATUS: Blue 0805 Status LED on GPIO2 with 1k series resistor
- C_MCU_DEC: 10uF 10V Tantalum + 100nF 0805 Ceramic on 3V3 rail
"""

ctrl_labels = [
    ("VCC_5V", "input"),
    ("VCC_3V3", "input"),
    ("GND", "bidirectional"),
    ("SPI_SCK", "output"),
    ("SPI_MOSI", "output"),
    ("SPI_MISO", "input"),
    ("VOL_CS", "output"),
    ("MUX_A", "output"),
    ("MUX_B", "output"),
    ("MUTE_ALL", "output"),
    ("RELAY_CTRL", "output"),
    ("BT_KEY", "output"),
    ("STATUS_LED", "output"),
    ("FAULT1", "input"),
    ("FAULT2", "input"),
    ("FAULT3", "input"),
    ("NTC_ADC", "input"),
    ("DC_OFFSET_ADC", "input"),
    ("UART_TX", "output"),
    ("UART_RX", "input")
]

with open(f"{BASE_DIR}/controller.kicad_sch", "w") as f:
    f.write(make_sheet("ESP32 Controller Subsystem", ctrl_notes, ctrl_labels, ctrl_components))

# 6. PROTECTION SHEET
prot_notes = """FAIL-PROOF SPEAKER & SYSTEM PROTECTION SUBSYSTEM:
5-LAYER DEFENSE-IN-DEPTH ARCHITECTURE:
1. Layer 1 (Hardware Fail-Safe):
   - MUTE_ALL has physical 10k pull-down to GND (amps muted on reset/crash)
   - Power Relay K1 is Normally-Open (amps unpowered unless energized)
2. Layer 2 (Watchdog Recovery):
   - ESP32 Hardware Watchdog reboots controller on lockup -> returns to Layer 1 safe state
3. Layer 3 (Startup Sequencing):
   - 3.0s bias stabilization -> verify FAULT1..3 -> engage Relay K1 -> wait 500ms -> unmute
4. Layer 4 (Active Real-Time Monitoring):
   - DC Offset Detection: 100k/10k divider + 10uF filter + 3.3V Zener clamping to GPIO36
   - Heatsink Thermal Sense: 10k NTC thermistor + 10k precision divider to GPIO35
     * >60C: Automatic -6dB volume throttling
     * >80C: Immediate emergency shutdown
5. Layer 5 (Voice Coil Current Protection):
   - 6x 2A Resettable PTC Polyfuses in series with speaker outputs
"""

prot_components = """CIRCUIT COMPONENTS & TERMINALS:
- K1: Songle SRD-05VDC-SL-C (SPST 10A 250VAC Power Relay)
- Q1: 2N2222 NPN BJT Transistor in SOT-23 package
- D_FLY: 1N4007 1A 1000V Flyback Diode across relay coil
- R_BASE: 1k 1% 0805 Base Drive Resistor
- PF1..PF6: 2A 30V Resettable PTC Polyfuses (Bourns MF-MSMF200 or THT)
- R_DC1: 100k 1% 0805 Resistor from Speaker Output to DC Sense Node
- R_DC2: 10k 1% 0805 Resistor from DC Sense Node to GND
- C_DC_FILT: 10uF 25V Low-Leakage Tantalum/MLCC Capacitor (Filters AC audio)
- D_CLAMP: BZX84C3V3 3.3V Zener Diode (Prevents overvoltage into ADC)
- R_NTC_PU: 10k 0.1% 0805 Precision Pull-up Resistor to 3.3V
- TH_NTC: 10k NTC Thermistor (Beta=3950) bolted directly to amplifier heatsink
- J_SPK1..6: 6x 2-Pin 5.08mm Pitch High-Current Screw Terminal Blocks (FL, FR, SL, SR, Center, Sub)
"""

prot_labels = [
    ("VCC_24V_RAW", "input"),
    ("VCC_24V", "output"),
    ("VCC_5V", "input"),
    ("VCC_3V3", "input"),
    ("GND", "bidirectional"),
    ("RELAY_CTRL", "input"),
    ("NTC_ADC", "output"),
    ("DC_OFFSET_ADC", "output"),
    ("SPK_FL_P", "input"),
    ("SPK_FL_N", "input"),
    ("SPK_FR_P", "input"),
    ("SPK_FR_N", "input"),
    ("SPK_SL_P", "input"),
    ("SPK_SL_N", "input"),
    ("SPK_SR_P", "input"),
    ("SPK_SR_N", "input"),
    ("SPK_C_P", "input"),
    ("SPK_C_N", "input"),
    ("SPK_SUB_P", "input"),
    ("SPK_SUB_N", "input")
]

with open(f"{BASE_DIR}/protection.kicad_sch", "w") as f:
    f.write(make_sheet("Protection & Speaker Terminals", prot_notes, prot_labels, prot_components))

# 7. ROOT SCHEMATIC: sony-5.1-revival.kicad_sch
root_lines = []
root_lines.append('(kicad_sch')
root_lines.append('\t(version 20231120)')
root_lines.append('\t(generator "eeschema")')
root_lines.append('\t(generator_version "8.0")')
root_lines.append(f'\t(uuid "{uid()}")')
root_lines.append('\t(paper "A3")')
root_lines.append('\t(title_block')
root_lines.append('\t\t(title "Sony MHC-GN1300D 5.1 System Revival - Master Schematic")')
root_lines.append('\t\t(date "2026-09-06")')
root_lines.append('\t\t(rev "1.0")')
root_lines.append('\t\t(comment 1 "Unified 5.1 Class-D Amp + Active Crossover + ESP32 Web/Serial Hub")')
root_lines.append('\t\t(comment 2 "Target Fabrication: Lion Circuits India (150x200mm 2-Layer FR4)")')
root_lines.append('\t)')
root_lines.append('\t(lib_symbols)')

sheets_info = [
    ("Power Supply Subsystem", "power_supply.kicad_sch", 50.8, 50.8),
    ("Amplifier Subsystem", "amplifier.kicad_sch", 139.7, 50.8),
    ("Crossover & Input Subsystem", "crossover_input.kicad_sch", 228.6, 50.8),
    ("ESP32 Controller Subsystem", "controller.kicad_sch", 50.8, 114.3),
    ("Protection & Terminals", "protection.kicad_sch", 139.7, 114.3)
]

for name, filename, x, y in sheets_info:
    root_lines.append('\t(sheet')
    root_lines.append(f'\t\t(at {x:.2f} {y:.2f})')
    root_lines.append('\t\t(size 63.5 38.1)')
    root_lines.append('\t\t(fields_autoplaced yes)')
    root_lines.append('\t\t(stroke (width 0) (type solid))')
    root_lines.append('\t\t(fill (color 0 0 0 0.0000))')
    root_lines.append(f'\t\t(uuid "{uid()}")')
    root_lines.append(f'\t\t(property "Sheetname" "{name}" (at {x:.2f} {y-2.54:.2f} 0) (effects (font (size 1.524 1.524)) (justify left bottom)))')
    root_lines.append(f'\t\t(property "Sheetfile" "{filename}" (at {x:.2f} {y+40.64:.2f} 0) (effects (font (size 1.27 1.27)) (justify left top)))')
    root_lines.append('\t)')

root_lines.append(')')

with open(f"{BASE_DIR}/sony-5.1-revival.kicad_sch", "w") as f:
    f.write('\n'.join(root_lines))

print("All schematic files written.")

# 8. COMPREHENSIVE BOM.CSV
bom_data = [
    ["Reference", "Value", "Footprint", "Description", "Manufacturer / Source", "Unit Cost (INR)", "Quantity", "Subtotal (INR)"],
    ["U_AMP1, U_AMP2, U_AMP3", "TPA3116D2", "HTSSOP-32-1EP", "50W Stereo / 100W Mono Class-D Audio Amp", "Texas Instruments / Robu.in", "250", "3", "750"],
    ["U_OP1, U_OP2, U_OP3", "NE5532", "SOIC-8", "Dual Low-Noise Audio Operational Amplifier", "Texas Instruments / LCSC", "35", "3", "105"],
    ["U_MCU", "ESP32-WROOM-32", "Module_ESP32", "Dual-Core Wi-Fi & BLE Microcontroller", "Espressif / Robu.in", "420", "1", "420"],
    ["U_BT", "QCC3008_MODULE", "PinHeader_1x12_P2.54mm", "Bluetooth 5.0 Audio Module (aptX/aptX-LL)", "Qualcomm / AliExpress / Robu.in", "550", "1", "550"],
    ["DISP1", "2.42\" SSD1309 OLED", "Connector_PinHeader_1x07", "128x64 White SPI OLED Display Module", "Robu.in / Amazon.in", "650", "1", "650"],
    ["U_VOL", "MCP4252", "SOIC-14", "Dual 8-Bit SPI Digital Potentiometer", "Microchip / Mouser / LCSC", "260", "1", "260"],
    ["U_MUX", "CD4052", "SOIC-16", "Dual 4-Channel Analog Multiplexer", "TI / NXP / LCSC", "40", "1", "40"],
    ["U_BUCK", "LM2596-5.0", "TO-263-5", "3A Step-Down Voltage Switching Regulator", "Texas Instruments / LCSC", "65", "1", "65"],
    ["U_LDO", "AMS1117-3.3", "SOT-223", "1A Low-Dropout Linear Voltage Regulator", "Advanced Monolithic / LCSC", "18", "1", "18"],
    ["U_VGND", "TLE2426", "TO-92", "Precision Virtual Ground Rail Splitter", "Texas Instruments / Mouser", "120", "1", "120"],
    ["BR1", "KBU810", "Bridge_Rectifier_D-44", "8A 1000V Silicon Single-Phase Bridge", "Vishay / Robu.in", "45", "1", "45"],
    ["T1", "230V:18V 200VA", "Toroidal_Chassis_Mount", "Toroidal Step-Down Power Transformer", "Miracle / Toroid India", "1800", "1", "1800"],
    ["K1", "SRD-05VDC-SL-C", "Relay_SPST_Songle", "5V Coil 10A 250VAC SPST Power Relay", "Songle / Robu.in", "45", "1", "45"],
    ["Q1", "2N2222", "SOT-23", "40V 800mA NPN Bipolar Transistor", "ON Semi / LCSC", "6", "1", "6"],
    ["D_FLY", "1N4007", "SMA_DO-214AC", "1A 1000V General Purpose Rectifier Diode", "Diodes Inc / LCSC", "5", "1", "5"],
    ["D_BUCK", "1N5822", "SMC_DO-214AB", "3A 40V Schottky Barrier Diode", "Vishay / LCSC", "15", "1", "15"],
    ["D_CLAMP", "BZX84C3V3", "SOT-23", "3.3V 350mW Zener Voltage Clamping Diode", "Nexperia / LCSC", "8", "1", "8"],
    ["PF1..PF6", "MF-MSMF200 (2A)", "Fuse_1812_4532Metric", "2A 30V Resettable PTC Polyfuses", "Bourns / LCSC", "22", "6", "132"],
    ["TH_NTC", "10k NTC 3950", "Ring_Lug_Mount", "10k Beta=3950 Thermal Sensor with Wire", "Robu.in / Amazon.in", "40", "1", "40"],
    ["U_IR", "TSOP1738", "Through_Hole_3Pin", "38kHz Infrared Remote Receiver IC", "Vishay / Robu.in", "30", "1", "30"],
    ["ENC1", "EC11", "RotaryEncoder_Switch", "Incremental Rotary Encoder with Push Switch", "Alps / Bourns / Robu.in", "55", "1", "55"],
    ["L_BUCK", "33uH 3A", "Inductor_SMD_12x12mm", "Shielded Power Inductor for Buck Converter", "Coilcraft / Wurth / LCSC", "45", "1", "45"],
    ["L1..L12", "22uH 5A", "Inductor_SMD_10x10mm", "Shielded Class-D Output Filter Inductors", "Coilcraft / Wurth / Robu.in", "35", "12", "420"],
    ["C1, C2", "4700uF 35V", "Radial_D18mm_P7.5mm", "Low-ESR High-Ripple Electrolytic Capacitors", "Nichicon / Panasonic / Robu.in", "95", "2", "190"],
    ["C_BULK1..3", "1000uF 35V", "Radial_D12.5mm_P5mm", "Low-ESR Local Rail Decoupling Capacitors", "Rubycon / Nichicon / Robu.in", "35", "3", "105"],
    ["C_O1..C_O12", "680nF 63V", "Film_Box_7.2x4.5mm", "Metallized Polypropylene Audio Filter Caps", "WIMA / Epcos / LCSC", "22", "12", "264"],
    ["C_F1..C_F12", "100nF 50V 5%", "Film_Box_5mm_Pitch", "Precision Film Caps for Sallen-Key Crossover", "KEMET / WIMA / LCSC", "14", "12", "168"],
    ["C_DEC", "100nF 50V X7R", "0805_Metric", "Ceramic Decoupling Capacitors", "Murata / Yageo / LCSC", "2", "35", "70"],
    ["C_IN1..6", "1.0uF 50V", "Film_Box_5mm_Pitch", "Audio Coupling Capacitors", "WIMA / Panasonic / LCSC", "18", "6", "108"],
    ["R_PASSIVES", "Assorted 1% Resistors", "0805_Metric", "Metal Film Precision Resistors (20k, 16k, 10k, 1k, etc.)", "Yageo / Vishay / LCSC", "1.5", "50", "75"],
    ["J_SPK1..J_SPK6", "2-Pin 5.08mm Screw", "TerminalBlock_1x02_P5.08mm", "Heavy Duty Speaker Screw Terminals", "Phoenix Contact / Robu.in", "25", "6", "150"],
    ["J_AC", "3-Pin 5.08mm Screw", "TerminalBlock_1x03_P5.08mm", "Mains Power Screw Terminal (L, N, PE)", "Phoenix Contact / Robu.in", "35", "1", "35"],
    ["J_AUX", "3.5mm Stereo Jack", "AudioJack3_Switch", "3.5mm PCB Mount Stereo Audio Jack", "CUI Devices / Robu.in", "30", "1", "30"],
    ["F1 + HOLDER", "3A 250V 5x20mm", "FuseHolder_5x20mm", "Fast-Blow Cartridge Fuse & Safety Clips", "Littelfuse / Robu.in", "35", "1", "35"],
    ["RV1", "14D431K", "Varistor_14mm_Pitch7.5", "275V Metal Oxide Varistor Surge Suppressor", "Bourns / TDK / Robu.in", "20", "1", "20"],
    ["HEATSINK", "Aluminium Extrusion", "Custom_Chassis_Mount", "Black Anodized Aluminium Heatsink for 3x TPA3116", "Local Fabrication / Amazon.in", "450", "1", "450"],
    ["PCB_FAB", "150x200mm 2-Layer", "Lion_Circuits_Standard", "5x Custom Manufactured PCBs (1.6mm FR4, HASL)", "Lion Circuits India", "1450", "1", "1450"],
    ["HARDWARE_MISC", "Standoffs, Screws, Thermal Tape", "Misc_Hardware", "M3 Brass Standoffs, Screws, Silicone Thermal Pads", "Local Hardware / Amazon.in", "350", "1", "350"]
]

with open(f"{BASE_DIR}/BOM.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in bom_data:
        writer.writerow(row)

total_cost = sum(int(row[7]) for row in bom_data[1:])
print(f"Comprehensive BOM generated. Total Estimated Cost: INR {total_cost:,}")
