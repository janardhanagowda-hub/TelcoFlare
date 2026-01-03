import os

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
    template_path = r"C:\TelcoFlare\Fetching_Templates\Radio_Script_Template\4_port_4x4_template.txt"

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
    output_dir = r"C:\TelcoFlare\Output"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(
        output_dir,
        f"{xxNodeIDxx}_{sector_name}_4_port_4x4_RRU_Final.txt"
    )

    with open(output_file, "w") as f:
        f.write(content)

    return output_file
