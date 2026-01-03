import os

# ===============================
# CORE: 8 PORT 4x4 RADIO SCRIPT
# ===============================
def generate_8_port_4x4(
    xxNodeIDxx: str,
    replacements: dict
):
    template_path = r"C:\TelcoFlare\Fetching_Templates\Radio_Script_Template\8_port_4x4_template.txt"
    output_dir = r"C:\TelcoFlare\Output"

    # Sector mapping
    sector_mapping = {
        1: "Alpha",
        2: "Beta",
        3: "Gamma",
        4: "Delta",
        5: "Epsilon",
        6: "Foxtrot"
    }

    # Extract sector ID
    sector_id = int(replacements["xxAntennaUnitGroupxx"])

    # Read template
    with open(template_path, "r") as f:
        content = f.read()

    # Replace placeholders
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", value)

    # Ensure output directory
    os.makedirs(output_dir, exist_ok=True)

    # Output filename
    output_file = os.path.join(
        output_dir,
        f"{xxNodeIDxx}_{sector_mapping[sector_id]}_8_port_4x4_RRU_Final.txt"
    )

    # Write file
    with open(output_file, "w") as f:
        f.write(content)

    return output_file
