import os
from pathlib import Path
import tempfile


# ===============================
# CORE: 8 PORT 4x4 RADIO SCRIPT
# ===============================
def generate_8_port_4x4(
    xxNodeIDxx: str,
    replacements: dict
):

    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "Radio_Script_Template" / "8_port_4x4_template.txt"
    
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

    # Ensure output
    temp_dir = Path(tempfile.gettempdir())
    safe_node = xxNodeIDxx.replace(" ", "_").replace("/", "_")
    file_path = temp_dir / f"{xxNodeIDxx}_{sector_id}_8_Port_4x4_RRU_Final.txt"
    file_path.write_text(content, encoding="utf-8")

    print("✅ Radio Script 8 Ports 4x4 FILE GENERATED:", file_path)
    return file_path
