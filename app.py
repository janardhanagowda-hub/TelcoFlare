from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import subprocess
import re
import os


app = FastAPI()

# ---------------- STATIC & TEMPLATES ----------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------------- LOGIN (TEMP HARD CODED) ----------------
USERNAME = "admin"
PASSWORD = "admin123"


# ---------------- LOGIN ----------------
@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == USERNAME and password == PASSWORD:
        return RedirectResponse("/dashboard", status_code=302)
    return RedirectResponse("/", status_code=302)


# ---------------- DASHBOARD ----------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


# ====================================================
# ================ AWS ESS (FASTAPI) =================
# ====================================================

@app.get("/tool/aws_ess", response_class=HTMLResponse)
async def aws_ess_page(request: Request):
    return templates.TemplateResponse(
        "aws_ess.html",
        {"request": request}
    )


from Fetching_Templates.ESS_Template.ESS_AWS_Tool import generate_aws_ess

@app.post("/tool/aws_ess", response_class=HTMLResponse)
async def aws_ess_submit(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxENBIDxx: str = Form(...),
    xxB66SSBxx: str = Form(...),
    xxB66AlphaCellIDxx: str = Form(...),
    xxB66BetaCellIDxx: str = Form(...),
    xxB66GammaCellIDxx: str = Form(...),
    xxB66AlphaPCIxx: str = Form(...),
    xxB66BetaPCIxx: str = Form(...),
    xxB66GammaPCIxx: str = Form(...),
    xxTACxx: str = Form(...),
    ltecellnames: str = Form(...),
    ltescs: str = Form(...),
    nrcellnames: str = Form(...)
):
    form_data = locals()   # 👈 zero logic, just pass data
    form_data.pop("request")

    output_file = generate_aws_ess(form_data)

    return templates.TemplateResponse(
        "aws_ess.html",
        {
            "request": request,
            "message": "✅ AWS ESS file generated successfully",
            "output_file": output_file
        }
    )



# ====================================================
# ================ PCS ESS (FASTAPI) =================
# ====================================================

@app.get("/tool/pcs_ess", response_class=HTMLResponse)
async def pcs_ess_page(request: Request):
    return templates.TemplateResponse(
        "pcs_ess.html",
        {"request": request}
    )


from Fetching_Templates.ESS_Template.ESS_PCS_Tool import generate_pcs_ess

@app.post("/tool/pcs_ess", response_class=HTMLResponse)
async def pcs_ess_submit(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxENBIDxx: str = Form(...),
    xxB2SSBxx: str = Form(...),
    xxB2AlphaCellIDxx: str = Form(...),
    xxB2BetaCellIDxx: str = Form(...),
    xxB2GammaCellIDxx: str = Form(...),
    xxB2AlphaPCIxx: str = Form(...),
    xxB2BetaPCIxx: str = Form(...),
    xxB2GammaPCIxx: str = Form(...),
    xxTACxx: str = Form(...),
    ltecellnames: str = Form(...),
    ltescs: str = Form(...),
    nrcellnames: str = Form(...)
):
    form_data = locals()   # 👈 zero logic, just pass data
    form_data.pop("request")

    output_file = generate_pcs_ess(form_data)

    return templates.TemplateResponse(
        "pcs_ess.html",
        {
            "request": request,
            "message": "✅ PCS ESS file generated successfully",
            "output_file": output_file
        }
    )

# ======================================================
# ================ GUTRA 850 (FASTAPI) =================
# ======================================================
@app.get("/tool/gutra_850", response_class=HTMLResponse)
async def gutra_850_page(request: Request):
    return templates.TemplateResponse(
        "gutra_850.html",
        {"request": request}
    )

from Fetching_Templates.Gutra_Template.GUTRA_5G_850 import generate_gutra_850

@app.post("/tool/gutra_850", response_class=HTMLResponse)
async def gutra_850_submit(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxgNodebIDxx: str = Form(...),
    xxgNbIDxx: str = Form(...),
    xxNrIPxx: str = Form(...),
    xx5G850SSBxx: str = Form(...),
    xx5G850AlphaCellIDxx: str = Form(...),
    xx5G850BetaCellIDxx: str = Form(...),
    xx5G850GammaCellIDxx: str = Form(...),
    cellnames: str = Form(...)
):
    form_data = locals()
    form_data.pop("request")

    output_file = generate_gutra_850(form_data)

    return templates.TemplateResponse(
        "gutra_850.html",
        {
            "request": request,
            "message": "✅ 5G 850 GUTRA file generated successfully",
            "output_file": output_file
        }
    )


# ============================================================
# ================ GUTRA CBAND_DOD (FASTAPI) =================
# ============================================================


@app.get("/tool/gutra_cband_dod", response_class=HTMLResponse)
def gutra_cband_dod_page(request: Request):
    return templates.TemplateResponse(
        "gutra_cband_dod.html",
        {"request": request}
    )

from Fetching_Templates.Gutra_Template.Cband_DOD_GUTRA import generate_gutra_cband_dod

@app.post("/tool/gutra_cband_dod", response_class=HTMLResponse)
async def gutra_cband_dod_generate(request: Request,
    xxNodeIDxx: str = Form(...),
    xxgNodebIDxx: str = Form(...),
    xxgNbIDxx: str = Form(...),
    xxNrIPxx: str = Form(...),
    xxCbandSSBxx: str = Form(...),
    xxDODSSBxx: str = Form(...),
    xxCbandAlphaCellIDxx: str = Form(...),
    xxCbandBetaCellIDxx: str = Form(...),
    xxCbandGammaCellIDxx: str = Form(...),
    xxDODAlphaCellIDxx: str = Form(...),
    xxDODBetaCellIDxx: str = Form(...),
    xxDODGammaCellIDxx: str = Form(...),
    cellnames: str = Form(...)
):
    # Gather all form data into a dict
    form_data = {
        "xxNodeIDxx": xxNodeIDxx,
        "xxgNodebIDxx": xxgNodebIDxx,
        "xxgNbIDxx": xxgNbIDxx,
        "xxNrIPxx": xxNrIPxx,
        "xxCbandSSBxx": xxCbandSSBxx,
        "xxDODSSBxx": xxDODSSBxx,
        "xxCbandAlphaCellIDxx": xxCbandAlphaCellIDxx,
        "xxCbandBetaCellIDxx": xxCbandBetaCellIDxx,
        "xxCbandGammaCellIDxx": xxCbandGammaCellIDxx,
        "xxDODAlphaCellIDxx": xxDODAlphaCellIDxx,
        "xxDODBetaCellIDxx": xxDODBetaCellIDxx,
        "xxDODGammaCellIDxx": xxDODGammaCellIDxx,
        "cellnames": cellnames
    }

    # Call the tool, which now handles replacements + file ops
    output_file = generate_gutra_cband_dod(form_data)

    return templates.TemplateResponse(
        "gutra_cband_dod.html",
        {
            "request": request,
            "message": "✅ File generated successfully",
            "output_file": output_file
        }
    )


# ============================================================
# ================ 4port_4x4 (FASTAPI) =======================
# ============================================================

@app.get("/tool/4port_4x4", response_class=HTMLResponse)
def port4_4x4(request: Request):
    return templates.TemplateResponse(
        "4port_4x4.html",
        {"request": request}
    )


from Fetching_Templates.Radio_Script_Template.port4_4x4 import generate_port4_4x4


@app.post("/tool/4port_4x4", response_class=HTMLResponse)
async def generate_port4_4x4_route(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxAntennaUnitGroupxx: str = Form(...),
    xxAntennaUnitxx: str = Form(...),
    xxAntennaSubunitxx: str = Form(...),
    xxRRUxx: str = Form(...),
    xxrfb1xx: str = Form(...),
    xxrfb2xx: str = Form(...),
    xxrfb3xx: str = Form(...),
    xxrfb4xx: str = Form(...),
    xxAttenuationxx: str = Form(...),
    xxTrafficDelayxx: str = Form(...),
    xxSectorEquipmentFunctionxx: str = Form(...),
):
    output_file = generate_port4_4x4(
        xxNodeIDxx,
        xxAntennaUnitGroupxx,
        xxAntennaUnitxx,
        xxAntennaSubunitxx,
        xxRRUxx,
        xxrfb1xx,
        xxrfb2xx,
        xxrfb3xx,
        xxrfb4xx,
        xxAttenuationxx,
        xxTrafficDelayxx,
        xxSectorEquipmentFunctionxx,
    )

    return templates.TemplateResponse(
        "4port_4x4.html",
        {
            "request": request,
            "message": "✅ File generated successfully",
            "output_file": output_file,
        }
    )


# ===============================================================
# ================ C_D port_4x4 (FASTAPI) =======================
# ===============================================================

@app.get("/tool/cd_add_4x4", response_class=HTMLResponse)
def cd_add_4x4(request: Request):
    return templates.TemplateResponse(
        "cd_add_4x4.html",
        {"request": request}
    )


from Fetching_Templates.Radio_Script_Template.C_D_Add_4x4 import generate_cd_add_4x4


@app.post("/tool/cd_add_4x4", response_class=HTMLResponse)
async def cd_add_4x4_submit(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxAntennaUnitGroupxx: str = Form(...),
    xxAntennaUnitxx: str = Form(...),
    xxAntennaSubunitxx: str = Form(...),
    xxRRUxx: str = Form(...),
    xxrfb1xx: str = Form(...),
    xxrfb2xx: str = Form(...),
    xxrfb3xx: str = Form(...),
    xxrfb4xx: str = Form(...),
    xxAttenuationxx: str = Form(...),
    xxTrafficDelayxx: str = Form(...),
    xxSectorEquipmentFunctionxx: str = Form(...),
    xxSectorCarrierxx: str = Form(...),
    xxconfiguredMaxTxPowerxx: str = Form(...)
):
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
        "xxSectorCarrierxx": xxSectorCarrierxx,
        "xxconfiguredMaxTxPowerxx": xxconfiguredMaxTxPowerxx,
    }

    output_file = generate_cd_add_4x4(
        xxNodeIDxx,
        xxAntennaUnitGroupxx,
        replacements
    )

    return templates.TemplateResponse(
        "cd_add_4x4.html",
        {
            "request": request,
            "message": "✅ File generated successfully",
            "output_file": output_file
        }
    )

# ===============================================================
# ================ 8 port_4x4 (FASTAPI) =========================
# ===============================================================

@app.get("/tool/radio_8_port_4x4", response_class=HTMLResponse)
def radio_8_port_4x4(request: Request):
    return templates.TemplateResponse(
        "radio_8_port_4x4.html",
        {"request": request}
    )


from Fetching_Templates.Radio_Script_Template.port8_4x4 import generate_8_port_4x4


@app.post("/tool/radio_8_port_4x4", response_class=HTMLResponse)
async def radio_8_port_4x4_submit(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxAntennaUnitGroupxx: str = Form(...),
    xxAntennaUnitxx: str = Form(...),
    xxAntennaSubunitxx: str = Form(...),
    xxRRUxx: str = Form(...),
    xxrfb1xx: str = Form(...),
    xxrfb2xx: str = Form(...),
    xxrfb3xx: str = Form(...),
    xxrfb4xx: str = Form(...),
    xxrfb5xx: str = Form(...),
    xxrfb6xx: str = Form(...),
    xxrfb7xx: str = Form(...),
    xxrfb8xx: str = Form(...),
    xxAttenuationxx: str = Form(...),
    xxTrafficDelayxx: str = Form(...),
    xxSectorEquipmentFunctionxx: str = Form(...)
):
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
        "xxrfb5xx": xxrfb5xx,
        "xxrfb6xx": xxrfb6xx,
        "xxrfb7xx": xxrfb7xx,
        "xxrfb8xx": xxrfb8xx,
        "xxAttenuationxx": xxAttenuationxx,
        "xxTrafficDelayxx": xxTrafficDelayxx,
        "xxSectorEquipmentFunctionxx": xxSectorEquipmentFunctionxx,
    }

    output_file = generate_8_port_4x4(
        xxNodeIDxx=xxNodeIDxx,
        replacements=replacements
    )

    return templates.TemplateResponse(
        "radio_8_port_4x4.html",
        {
            "request": request,
            "message": "✅ File generated successfully",
            "output_file": output_file
        }
    )


# ===============================================================
# ================ 8 port_8x4 (FASTAPI) =========================
# ===============================================================


@app.get("/tool/radio_8_port_8x4", response_class=HTMLResponse)
def radio_8_port_8x4(request: Request):
    return templates.TemplateResponse(
        "radio_8_port_8x4.html",
        {"request": request}
    )


from Fetching_Templates.Radio_Script_Template.port8_8x4 import generate_8_port_8x4


@app.post("/tool/radio_8_port_8x4", response_class=HTMLResponse)
async def radio_8_port_8x4_submit(
    request: Request,
    xxNodeIDxx: str = Form(...),
    xxAntennaUnitGroupxx: str = Form(...),
    xxAntennaUnitxx: str = Form(...),
    xxAntennaSubunitxx: str = Form(...),
    xxRRUxx: str = Form(...),
    xxrfb1xx: str = Form(...),
    xxrfb2xx: str = Form(...),
    xxrfb3xx: str = Form(...),
    xxrfb4xx: str = Form(...),
    xxrfb5xx: str = Form(...),
    xxrfb6xx: str = Form(...),
    xxrfb7xx: str = Form(...),
    xxrfb8xx: str = Form(...),
    xxAttenuationxx: str = Form(...),
    xxTrafficDelayxx: str = Form(...),
    xxSectorEquipmentFunctionxx: str = Form(...)
):
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
        "xxrfb5xx": xxrfb5xx,
        "xxrfb6xx": xxrfb6xx,
        "xxrfb7xx": xxrfb7xx,
        "xxrfb8xx": xxrfb8xx,
        "xxAttenuationxx": xxAttenuationxx,
        "xxTrafficDelayxx": xxTrafficDelayxx,
        "xxSectorEquipmentFunctionxx": xxSectorEquipmentFunctionxx,
    }

    output_file = generate_8_port_8x4(
        xxNodeIDxx=xxNodeIDxx,
        replacements=replacements
    )

    return templates.TemplateResponse(
        "radio_8_port_8x4.html",
        {
            "request": request,
            "message": "✅ File generated successfully",
            "output_file": output_file
        }
    )
