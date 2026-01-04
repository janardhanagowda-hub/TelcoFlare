import os
import re
from pathlib import Path
import tempfile


def generate_gutra_850(form_data: dict):
    print("✅ GUTRA 850 TOOL STARTED")

    xxNodeIDxx = form_data["xxNodeIDxx"]

    # ---------------- PARSE CELLNAMES ----------------
    cell_list = [
        c.strip() for c in form_data["cellnames"].splitlines() if c.strip()
    ]

    # ---------------- REPLACEMENTS ----------------
    replacements = {
        "xxNodeIDxx": xxNodeIDxx,
        "xxgNodebIDxx": form_data["xxgNodebIDxx"],
        "xxgNbIDxx": form_data["xxgNbIDxx"],
        "xxNrIPxx": form_data["xxNrIPxx"],
        "xx5G850SSBxx": form_data["xx5G850SSBxx"],
        "xx5G850AlphaCellIDxx": form_data["xx5G850AlphaCellIDxx"],
        "xx5G850BetaCellIDxx": form_data["xx5G850BetaCellIDxx"],
        "xx5G850GammaCellIDxx": form_data["xx5G850GammaCellIDxx"],
    }

    for i, cell in enumerate(cell_list, start=1):
        replacements[f"CELLNAME{i}"] = cell

    # ---------------- FILE OPS ----------------
    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "Gutra_Template" / "5G_850_GUTRA_Template.txt"
    
    output_dir = BASE_DIR / "Output"
    output_dir.mkdir(exist_ok=True)

    with open(template_path, "r") as f:
        content = f.read()

    # ---------------- TRUNCATE UNUSED CELLNAME ----------------
    first_unused = len(cell_list) + 1
    lines = content.splitlines()

    for idx, line in enumerate(lines):
        if f"{{CELLNAME{first_unused}}}" in line:
            content = "\n".join(lines[:max(idx - 1, 0)])
            break

    # ---------------- REPLACE ----------------
    for k, v in replacements.items():
        content = content.replace(f"{{{k}}}", v)

    temp_dir = Path(tempfile.gettempdir())
    safe_node = xxNodeIDxx.replace(" ", "_").replace("/", "_")
    file_path = temp_dir / f"{safe_node}_GUTRA_850_Final.txt"
    file_path.write_text(content, encoding="utf-8")

    print("✅ GUTRA 850 FILE GENERATED:", file_path)
    return file_path
