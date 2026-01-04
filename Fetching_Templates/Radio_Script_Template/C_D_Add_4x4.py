import os
from pathlib import Path
import tempfile


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
    temp_dir = Path(tempfile.gettempdir())
    safe_node = xxNodeIDxx.replace(" ", "_").replace("/", "_")
    file_path = temp_dir / f"{safe_node}_{sector_name}_CD_Port_RRU_Final.txt"
    file_path.write_text(content, encoding="utf-8")

    print("✅ Radio Script CD Ports 4x4 FILE GENERATED:", file_path)
    return file_path
