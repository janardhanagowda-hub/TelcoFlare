import os

TEMPLATE_PATH = r"C:\TelcoFlare\Fetching_Templates\Gutra_Template\Cband_DOD_GUTRA_Template.txt"
OUTPUT_DIR = r"C:\TelcoFlare\Output"


def generate_gutra_cband_dod(
    xxNodeIDxx: str,
    replacements: dict,
    cellnames: list
) -> str:
    # -----------------------------
    # Load template
    # -----------------------------
    with open(TEMPLATE_PATH, "r") as f:
        content = f.read()

    # -----------------------------
    # CELLNAME handling
    # -----------------------------
    for i, cell in enumerate(cellnames, start=1):
        replacements[f"CELLNAME{i}"] = cell

    # -----------------------------
    # Truncate unused CELLNAMEs
    # -----------------------------
    first_unused = len(cellnames) + 1
    lines = content.splitlines()

    for idx, line in enumerate(lines):
        if f"{{CELLNAME{first_unused}}}" in line:
            content = "\n".join(lines[:max(idx - 1, 0)])
            break

    # -----------------------------
    # Replace placeholders
    # -----------------------------
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", value)

    # -----------------------------
    # Write output file
    # -----------------------------
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_DIR,
        f"{xxNodeIDxx}_Cband_DOD_GUTRA_Final.txt"
    )

    with open(output_file, "w") as f:
        f.write(content)

    return output_file
