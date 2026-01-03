import os

def generate_pcs_ess(form_data: dict):
    """
    form_data: dict containing all raw form inputs
    """

    print("✅ PCS ESS TOOL STARTED")

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
        "xxB2SSBxx": form_data["xxB2SSBxx"],
        "xxB2AlphaCellIDxx": form_data["xxB2AlphaCellIDxx"],
        "xxB2BetaCellIDxx": form_data["xxB2BetaCellIDxx"],
        "xxB2GammaCellIDxx": form_data["xxB2GammaCellIDxx"],
        "xxB2AlphaPCIxx": form_data["xxB2AlphaPCIxx"],
        "xxB2BetaPCIxx": form_data["xxB2BetaPCIxx"],
        "xxB2GammaPCIxx": form_data["xxB2GammaPCIxx"],
        "xxTACxx": form_data["xxTACxx"],
    }

    # ---------------- FILE OPS ----------------
    template_path = r"C:\TelcoFlare\Fetching_Templates\ESS_Template\ESS_PCS_Template.txt"
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
        f"{xxNodeIDxx}_ESS_PCS_Final.txt"
    )

    with open(output_file, "w") as f:
        f.write(content)

    print("✅ PCS ESS FILE GENERATED:", output_file)
    return output_file
