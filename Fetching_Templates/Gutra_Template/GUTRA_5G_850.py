import os
import re

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

    # ---------------- LOAD TEMPLATE ----------------
    template_path = r"C:\TelcoFlare\Fetching_Templates\Gutra_Template\5G_850_GUTRA_Template.txt"

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

    # ---------------- OUTPUT ----------------
    output_dir = r"C:\TelcoFlare\Output"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(
        output_dir,
        f"{xxNodeIDxx}_5G_850_GUTRA_Final.txt"
    )

    with open(output_file, "w") as f:
        f.write(content)

    print("✅ GUTRA 850 FILE GENERATED:", output_file)
    return output_file
