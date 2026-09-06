import re

with open("tools/build_complete_kicad_v10.py", "r") as f:
    code = f.read()

# Replace lines with nested escaped quotes inside f-string
code = code.replace("SHEET_UUIDS[\'power_supply\']", "SHEET_UUIDS[\"power_supply\"]")
code = code.replace("SHEET_UUIDS[\'amplifier\']", "SHEET_UUIDS[\"amplifier\"]")
code = code.replace("SHEET_UUIDS[\'crossover_input\']", "SHEET_UUIDS[\"crossover_input\"]")
code = code.replace("SHEET_UUIDS[\'controller\']", "SHEET_UUIDS[\"controller\"]")
code = code.replace("SHEET_UUIDS[\'protection\']", "SHEET_UUIDS[\"protection\"]")

with open("tools/build_complete_kicad_v10.py", "w") as f:
    f.write(code)

print("Fixed syntax.")
