import os
from pathlib import Path


# ===============================
# CORE: 8 PORT 8x4 RADIO SCRIPT
# ===============================
def generate_8_port_8x4(
    xxNodeIDxx: str,
    replacements: dict
):

    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "Radio_Script_Template" / "8_port_8x4_template.txt"
    
    output_dir = BASE_DIR / "Output"
    output_dir.mkdir(exist_ok=True)

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
    output_file = os.path.join
    output_file = output_dir / f"{xxNodeIDxx}_{sector_id}_8_Port_8x4_RRU_Final.txt"
    # Write file
    with open(output_file, "w") as f:
        f.write(content)

    return output_file
