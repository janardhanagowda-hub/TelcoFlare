import os

TEMPLATE_PATH = r"C:\TelcoFlare\Fetching_Templates\Radio_Script_Template\8_port_8x4_template.txt"
OUTPUT_DIR = r"C:\TelcoFlare\Output"

SECTOR_MAPPING = {
    1: "Alpha",
    2: "Beta",
    3: "Gamma",
    4: "Delta",
    5: "Epsilon",
    6: "Foxtrot"
}


def generate_8_port_8x4(data: dict) -> str:
    """
    Core logic for 8-port 8x4 radio script generation
    """

    replacements = {
        "xxNodeIDxx": data["xxNodeIDxx"],
        "xxAntennaUnitGroupxx": data["xxAntennaUnitGroupxx"],
        "xxAntennaUnitxx": data["xxAntennaUnitxx"],
        "xxAntennaSubunitxx": data["xxAntennaSubunitxx"],
        "xxRRUxx": data["xxRRUxx"],
        "xxrfb1xx": data["xxrfb1xx"],
        "xxrfb2xx": data["xxrfb2xx"],
        "xxrfb3xx": data["xxrfb3xx"],
        "xxrfb4xx": data["xxrfb4xx"],
        "xxrfb5xx": data["xxrfb5xx"],
        "xxrfb6xx": data["xxrfb6xx"],
        "xxrfb7xx": data["xxrfb7xx"],
        "xxrfb8xx": data["xxrfb8xx"],
        "xxAttenuationxx": data["xxAttenuationxx"],
        "xxTrafficDelayxx": data["xxTrafficDelayxx"],
        "xxSectorEquipmentFunctionxx": data["xxSectorEquipmentFunctionxx"],
    }

    # Load template
    with open(TEMPLATE_PATH, "r") as f:
        content = f.read()

    # Replace placeholders
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", value)

    node_id = data["xxNodeIDxx"]
    sector_id = int(data["xxAntennaUnitGroupxx"])
    sector_name = SECTOR_MAPPING[sector_id]

    output_filename = f"{node_id}_{sector_name}_8_port_8x4_RRU_Final.txt"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    # Save output
    with open(output_path, "w") as f:
        f.write(content)

    return output_path
