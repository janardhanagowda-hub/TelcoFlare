import os
from pathlib import Path


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
    
    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "Radio_Script_Template" / "C_D_add_template.txt"
    
    output_dir = BASE_DIR / "Output"
    output_dir.mkdir(exist_ok=True)

    
    with open(template_path, "r") as f:
        content = f.read()

    # Replace placeholders
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", value)

    # Sector name
    sector_id = int(xxAntennaUnitGroupxx)
    sector_name = SECTOR_MAPPING.get(sector_id, "Unknown")

    # Output file
    output_file = os.path.join
    output_file = output_dir / f"{xxNodeIDxx}_{sector_name}_CD_Port_RRU_Final.txt"
    

    with open(output_file, "w") as f:
        f.write(content)

    return output_file
