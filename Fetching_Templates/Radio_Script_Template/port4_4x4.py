import os
from pathlib import Path
import tempfile


# ---------------------------------
# CORE FUNCTION
# ---------------------------------
def generate_port4_4x4(
    xxNodeIDxx: str,
    xxAntennaUnitGroupxx: str,
    xxAntennaUnitxx: str,
    xxAntennaSubunitxx: str,
    xxRRUxx: str,
    xxrfb1xx: str,
    xxrfb2xx: str,
    xxrfb3xx: str,
    xxrfb4xx: str,
    xxAttenuationxx: str,
    xxTrafficDelayxx: str,
    xxSectorEquipmentFunctionxx: str,
):
    # -----------------------------
    # Replacements
    # -----------------------------
    replacements = {
        "xxNodeIDxx": xxNodeIDxx,
        "xxAntennaUnitGroupxx": xxAntennaUnitGroupxx,
        "xxAntennaUnitxx": xxAntennaUnitxx,
        "xxAntennaSubunitxx": xxAntennaSubunitxx,
        "xxRRUxx": xxRRUxx,
        "xxrfb1xx": xxrfb1xx,
        "xxrfb2xx": xxrfb2xx,
        "xxrfb3xx": xxrfb3xx,
        "xxrfb4xx": xxrfb4xx,
        "xxAttenuationxx": xxAttenuationxx,
        "xxTrafficDelayxx": xxTrafficDelayxx,
        "xxSectorEquipmentFunctionxx": xxSectorEquipmentFunctionxx,
    }

    # -----------------------------
    # Load template
    # -----------------------------

    
    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "Radio_Script_Template" / "4_port_4x4_template.txt"
    
    output_dir = BASE_DIR / "Output"
    output_dir.mkdir(exist_ok=True)

    with open(template_path, "r") as f:
        content = f.read()

    # -----------------------------
    # Replace placeholders
    # -----------------------------
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", value)

    # -----------------------------
    # Sector mapping
    # -----------------------------
    sector_mapping = {
        1: "Alpha",
        2: "Beta",
        3: "Gamma",
        4: "Delta",
        5: "Epsilon",
        6: "Foxtrot",
    }

    sector_id = int(xxAntennaUnitGroupxx)
    sector_name = sector_mapping.get(sector_id, "Unknown")

    # -----------------------------
    # Write output file
    # -----------------------------
    temp_dir = Path(tempfile.gettempdir())
    safe_node = xxNodeIDxx.replace(" ", "_").replace("/", "_")
    file_path = temp_dir / f"{safe_node}_{sector_name}_4_port_4x4_RRU_Final.txt"
    file_path.write_text(content, encoding="utf-8")

    print("✅ Radio Script 4 Ports 4x4 FILE GENERATED:", file_path)
    return file_path
