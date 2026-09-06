import uuid

def make_uuid():
    return str(uuid.uuid4())

sch = f"""(kicad_sch
	(version 20231120)
	(generator "eeschema")
	(generator_version "8.0")
	(uuid "{make_uuid()}")
	(paper "A3")
	(title_block
		(title "Power Supply")
		(date "2026-09-06")
		(rev "1.0")
	)
	(lib_symbols)
	(wire
		(pts (xy 90 50) (xy 100 50))
		(stroke (width 0) (type default))
		(uuid "{make_uuid()}")
	)
	(global_label "VCC_24V"
		(shape bidirectional)
		(at 100 50 0)
		(fields_autoplaced yes)
		(effects
			(font (size 1.27 1.27))
			(justify left)
		)
		(uuid "{make_uuid()}")
	)
)
"""
with open("/tmp/test_power.kicad_sch", "w") as f:
    f.write(sch)

