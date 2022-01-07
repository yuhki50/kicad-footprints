#!/usr/bin/env python

# require Python 3.8.0 or newer

from pathlib import Path

try:
    script_dir = Path(__file__).parent.resolve()

    with (script_dir / "fp-lib-table").open("w", newline="\n") as f:
        f.write("\n".join([
            "(fp_lib_table",
            "\n".join([
                f"""  (lib (name {v.stem})(type KiCad)(uri ${{KIPRJMOD}}/modules/{v.name})(options "")(descr ""))"""
                for v in sorted(script_dir.glob("*.pretty"), key=lambda v: v.stem)
            ]),
            ")",
        ]))

except KeyboardInterrupt:
    pass
