from pathlib import Path
import tempfile

def generate_pcs_ess(form_data: dict):
    print("✅ PCS ESS TOOL STARTED")

    xxNodeIDxx = form_data["xxNodeIDxx"]

    ltecellnames = [x.strip() for x in form_data["ltecellnames"].splitlines() if x.strip()]
    ltescs = [x.strip() for x in form_data["ltescs"].splitlines() if x.strip()]
    nrcellnames = [x.strip() for x in form_data["nrcellnames"].splitlines() if x.strip()]

    replacements = {
        "xxNodeIDxx": xxNodeIDxx,
        "xxENBIDxx": form_data.get("xxENBIDxx", ""),
        "xxB2SSBxx": form_data.get("xxB2SSBxx", ""),
        "xxB2AlphaCellIDxx": form_data.get("xxB2AlphaCellIDxx", ""),
        "xxB2BetaCellIDxx": form_data.get("xxB2BetaCellIDxx", ""),
        "xxB2GammaCellIDxx": form_data.get("xxB2GammaCellIDxx", ""),
        "xxB2AlphaPCIxx": form_data.get("xxB2AlphaPCIxx", ""),
        "xxB2BetaPCIxx": form_data.get("xxB2BetaPCIxx", ""),
        "xxB2GammaPCIxx": form_data.get("xxB2GammaPCIxx", ""),
        "xxTACxx": form_data.get("xxTACxx", ""),
    }

    BASE_DIR = Path(__file__).resolve().parents[2]
    template_path = BASE_DIR / "Fetching_Templates" / "ESS_Template" / "ESS_PCS_Template.txt"

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    for i, val in enumerate(ltecellnames, start=1):
        content = content.replace(f"{{LTECELLNAME{i}}}", val)

    for i, val in enumerate(ltescs, start=1):
        content = content.replace(f"{{LTESC{i}}}", val)

    for i, val in enumerate(nrcellnames, start=1):
        content = content.replace(f"{{NRCELLNAME{i}}}", val)

    for k, v in replacements.items():
        content = content.replace(f"{{{k}}}", v)

    temp_dir = Path(tempfile.gettempdir())
    safe_node = xxNodeIDxx.replace(" ", "_").replace("/", "_")
    file_path = temp_dir / f"{safe_node}_PCS_ESS.txt"
    file_path.write_text(content, encoding="utf-8")

    print("✅ PCS ESS FILE GENERATED:", file_path)
    return file_path
