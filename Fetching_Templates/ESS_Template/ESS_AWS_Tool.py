import os

def generate_aws_ess(form_data: dict):
    """
    form_data: dict containing all raw form inputs
    """

    print("✅ AWS ESS TOOL STARTED")

    # ---------------- PARSE INPUTS ----------------
    xxNodeIDxx = form_data["xxNodeIDxx"]

    ltecellnames = [
        x.strip() for x in form_data["ltecellnames"].splitlines() if x.strip()
    ]
    ltescs = [
        x.strip() for x in form_data["ltescs"].splitlines() if x.strip()
    ]
    nrcellnames = [
        x.strip() for x in form_data["nrcellnames"].splitlines() if x.strip()
    ]

    replacements = {
        "xxNodeIDxx": xxNodeIDxx,
        "xxENBIDxx": form_data["xxENBIDxx"],
        "xxB66SSBxx": form_data["xxB66SSBxx"],
        "xxB66AlphaCellIDxx": form_data["xxB66AlphaCellIDxx"],
        "xxB66BetaCellIDxx": form_data["xxB66BetaCellIDxx"],
        "xxB66GammaCellIDxx": form_data["xxB66GammaCellIDxx"],
        "xxB66AlphaPCIxx": form_data["xxB66AlphaPCIxx"],
        "xxB66BetaPCIxx": form_data["xxB66BetaPCIxx"],
        "xxB66GammaPCIxx": form_data["xxB66GammaPCIxx"],
        "xxTACxx": form_data["xxTACxx"],
    }

    # ---------------- FILE OPS ----------------
    template_path = r"C:\TelcoFlare\Fetching_Templates\ESS_Template\ESS_AWS_Template.txt"
    output_dir = r"C:\TelcoFlare\Output"
    os.makedirs(output_dir, exist_ok=True)

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

    output_file = os.path.join(
        output_dir,
        f"{xxNodeIDxx}_ESS_AWS_Final.txt"
    )

    with open(output_file, "w") as f:
        f.write(content)

    print("✅ AWS ESS FILE GENERATED:", output_file)
    return output_file
