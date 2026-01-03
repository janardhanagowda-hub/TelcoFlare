import os

TEMPLATE_PATH = r"C:\TelcoFlare\Fetching_Templates\Radio_Script_Template\C_D_add_template.txt"
OUTPUT_DIR = r"C:\TelcoFlare\Output"

SECTOR_MAPPING = {
    1: "Alpha",
    2: "Beta",
    3: "Gamma",
    4: "Delta",
    5: "Epsilon",
    6: "Foxtrot"
}


def generate_cd_add_4x4(
    xxNodeIDxx: str,
    xxAntennaUnitGroupxx: str,
    replacements: dict
):
    # Load template
    with open(TEMPLATE_PATH, "r") as f:
        content = f.read()

    # Replace placeholders
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", value)

    # Sector name
    sector_id = int(xxAntennaUnitGroupxx)
    sector_name = SECTOR_MAPPING.get(sector_id, "Unknown")

    # Output file
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_DIR,
        f"{xxNodeIDxx}_{sector_name}_C_D_Add_4x4_RRU_Final.txt"
    )

    with open(output_file, "w") as f:
        f.write(content)

    return output_file
