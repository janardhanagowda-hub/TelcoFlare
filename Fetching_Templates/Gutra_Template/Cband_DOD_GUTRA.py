import os
from pathlib import Path
import tempfile


def generate_gutra_cband_dod(form_data: dict) -> str:
    print("✅ GUTRA CBAND DOD TOOL STARTED")

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
        "xxCbandSSBxx": form_data["xxCbandSSBxx"],
        "xxDODSSBxx": form_data["xxDODSSBxx"],
        "xxCbandAlphaCellIDxx": form_data["xxCbandAlphaCellIDxx"],
        "xxCbandBetaCellIDxx": form_data["xxCbandBetaCellIDxx"],
        "xxCbandGammaCellIDxx": form_data["xxCbandGammaCellIDxx"],
        "xxDODAlphaCellIDxx": form_data["xxDODAlphaCellIDxx"],
        "xxDODBetaCellIDxx": form_data["xxDODBetaCellIDxx"],
        "xxDODGammaCellIDxx": form_data["xxDODGammaCellIDxx"],
    }

    # Add CELLNAME placeholders dynamically
    for i, cell in enumerate(cell_list, start=1):
        replacements[f"CELLNAME{i}"] = cell

    # ---------------- FILE OPS ----------------
    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "Gutra_Template" / "Cband_DOD_GUTRA_Template.txt"
    
    output_dir = BASE_DIR / "Output"
    output_dir.mkdir(exist_ok=True)

    # ---------------- LOAD TEMPLATE ----------------
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

    # ---------------- WRITE OUTPUT ----------------
    temp_dir = Path(tempfile.gettempdir())
    safe_node = xxNodeIDxx.replace(" ", "_").replace("/", "_")
    file_path = temp_dir / f"{safe_node}_GUTRA_CBAND_DOD_Final.txt"
    file_path.write_text(content, encoding="utf-8")

    print("✅ GUTRA CBAND DOD FILE GENERATED:", file_path)
    return file_path
