import subprocess
import os

# Let's inspect how kicad-cli sch erc and export handles a schematic with symbols
test_sch = """(kicad_sch
	(version 20260306)
	(generator "eeschema")
	(generator_version "10.0")
	(uuid "11111111-2222-3333-4444-555555555555")
	(paper "A3")
	(title_block
		(title "Visual Test Sheet")
	)
	(lib_symbols
		(symbol "Device:R"
			(pin_numbers (offset 0.254))
			(pin_names (offset 0) (hide yes))
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
			(symbol "R_0_1"
				(rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254)) (fill (type none)))
			)
			(symbol "R_1_1"
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
	)
	(symbol
		(lib_id "Device:R")
		(at 100 100 0)
		(unit 1)
		(uuid "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee")
		(property "Reference" "R1" (at 102 100 0) (effects (font (size 1.27 1.27))))
		(property "Value" "10k" (at 98 100 0) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "11111111-1111-1111-1111-111111111111"))
		(pin "2" (uuid "22222222-2222-2222-2222-222222222222"))
	)
)
"""

with open("/tmp/test_vis.kicad_sch", "w") as f:
    f.write(test_sch)

print("Saved /tmp/test_vis.kicad_sch")
