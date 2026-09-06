import subprocess

test_sch = """(kicad_sch
	(version 20260306)
	(generator "eeschema")
	(generator_version "10.0")
	(uuid "28f865a0-4433-4a53-bbd7-b62f276848e4")
	(paper "A4")
	(title_block
		(title "Test Exact Syntax")
	)
	(lib_symbols
		(symbol "test:R"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at -1.778 0 90) (effects (font (size 0.762 0.762))))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 0.762 0.762))))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27))))
			(symbol "R_0_1"
				(rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "R_1_1"
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
	)
	(symbol
		(lib_id "test:R")
		(at 150 100 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "00000000-0000-0000-0000-00004549f38a")
		(property "Reference" "R1"
			(at 155 100 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "10k"
			(at 150 105 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 150 100 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at 150 100 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Description" ""
			(at 150 100 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "490a35ba-1ba2-44c5-adce-e27a045257ab"))
		(pin "2" (uuid "51355c82-d1cf-445b-b079-21c660dd8989"))
		(instances
			(project "test"
				(path "/28f865a0-4433-4a53-bbd7-b62f276848e4"
					(reference "R1")
					(unit 1)
				)
			)
		)
	)
)
"""

with open("/tmp/test_exact.kicad_sch", "w") as f:
    f.write(test_sch)

print("Written /tmp/test_exact.kicad_sch")
