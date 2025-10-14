#!/usr/bin/env python3
# ipynb2py.py
import json
import pathlib
import sys
import glob

files = sys.argv[1:] if len(sys.argv) > 1 else glob.glob("*.ipynb")

if not files:
    print("Brak plików .ipynb do konwersji w katalogu.")
    sys.exit(0)

for path_str in files:
    path = pathlib.Path(path_str)
    out_path = path.with_suffix(".py")

    with path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    lines = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            lines.append("# %%")  # marker komórki dla VSCode
            lines.extend(cell.get("source", []))
            lines.append("\n")
        elif cell.get("cell_type") == "markdown":
            lines.append('"""')  # zakomentowanie markdown jako docstring
            lines.extend(cell.get("source", []))
            lines.append('"""\n')

    with out_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Zapisano {out_path}")
