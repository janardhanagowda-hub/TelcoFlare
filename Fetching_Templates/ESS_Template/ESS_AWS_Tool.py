import os
from pathlib import Path

def generate_aws_ess(form_data: dict):
    """
    form_data: dict containing all raw form inputs
    """
    print("✅ AWS ESS TOOL STARTED")

    # ---------------- PARSE INPUTS ----------------
    xxNodeIDxx = form_data["xxNodeIDxx"]

    ltecellnames = [x.strip() for x in form_data["ltecellnames"].splitlines() if x.strip()]
    ltescs = [x.strip() for x in form_data["ltescs"].splitlines() if x.strip()]
    nrcellnames = [x.strip() for x in form_data["nrcellnames"].splitlines() if x.strip()]

    replacements = {
        "xxNodeIDxx": xxNodeIDxx,
        "xxENBIDxx": form_data.get("xxENBIDxx", ""),
        "xxB66SSBxx": form_data.get("xxB66SSBxx", ""),
        "xxB66AlphaCellIDxx": form_data.get("xxB66AlphaCellIDxx", ""),
        "xxB66BetaCellIDxx": form_data.get("xxB66BetaCellIDxx", ""),
        "xxB66GammaCellIDxx": form_data.get("xxB66GammaCellIDxx", ""),
        "xxB66AlphaPCIxx": form_data.get("xxB66AlphaPCIxx", ""),
        "xxB66BetaPCIxx": form_data.get("xxB66BetaPCIxx", ""),
        "xxB66GammaPCIxx": form_data.get("xxB66GammaPCIxx", ""),
        "xxTACxx": form_data.get("xxTACxx", ""),
    }

    # ---------------- FILE OPS ----------------
    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "ESS_Template" / "ESS_AWS_Template.txt"
    
    output_dir = BASE_DIR / "Output"
    output_dir.mkdir(exist_ok=True)

    with open(template_path, "r") as f:
        content = f.read()

    # LTE
    for i, val in enumerate(ltecellnames, start=1):
        content = content.replace(f"{{LTECELLNAME{i}}}", val)

    for i, val in enumerate(ltescs, start=1):
        content = content.replace(f"{{LTESC{i}}}", val)

    # NR
    for i, val in enumerate(nrcellnames, start=1):
        content = content.replace(f"{{NRCELLNAME{i}}}", val)

    # Common replacements
    for k, v in replacements.items():
        content = content.replace(f"{{{k}}}", v)

    # ---------------- OUTPUT FILE ----------------
    output_file = output_dir / f"{xxNodeIDxx}_ESS_AWS_Final.txt"

    with open(output_file, "w") as f:
        f.write(content)

    print("✅ AWS ESS FILE GENERATED:", output_file)
    return output_file
