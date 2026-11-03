"""
MCP Server implementation for Ocular Electrooculography (EOG) & Arden Ratio Skill.
Exposes standard FastMCP-compatible tools for retinal pigment epithelium (RPE) standing potential assessment.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import ElectrooculographyClient


def evaluate_electrooculogram_arden_ratio(
    od_light_peak_uv: float,
    od_dark_trough_uv: float,
    os_light_peak_uv: Optional[float] = None,
    os_dark_trough_uv: Optional[float] = None,
    dark_adaptation_duration_minutes: Optional[int] = 15,
    light_adaptation_duration_minutes: Optional[int] = 15,
    patient_age_years: Optional[int] = 40
) -> str:
    """
    Evaluates Electrooculography (EOG) light peak, dark trough, and Arden ratio (LP/DT).
    Returns structured analysis of RPE functional integrity.
    """
    client = ElectrooculographyClient()
    result = client.evaluate_eog(
        od_light_peak_uv=od_light_peak_uv,
        od_dark_trough_uv=od_dark_trough_uv,
        os_light_peak_uv=os_light_peak_uv,
        os_dark_trough_uv=os_dark_trough_uv,
        dark_adaptation_duration_minutes=dark_adaptation_duration_minutes,
        light_adaptation_duration_minutes=light_adaptation_duration_minutes,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_electrooculogram_arden_ratio",
                "description": "Calculates EOG Arden ratio (Light Peak / Dark Trough), percentage index, and interocular asymmetry to assess retinal pigment epithelium (RPE) health and detect Best vitelliform macular dystrophy.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "od_light_peak_uv": {"type": "number", "description": "Right eye (OD) light peak standing potential in uV (normal: 400 - 1200 uV)"},
                        "od_dark_trough_uv": {"type": "number", "description": "Right eye (OD) dark trough standing potential in uV (normal: 200 - 600 uV)"},
                        "os_light_peak_uv": {"type": "number", "description": "Optional left eye (OS) light peak in uV"},
                        "os_dark_trough_uv": {"type": "number", "description": "Optional left eye (OS) dark trough in uV"},
                        "dark_adaptation_duration_minutes": {"type": "integer", "description": "Dark phase duration in minutes (default: 15)"},
                        "light_adaptation_duration_minutes": {"type": "integer", "description": "Light phase duration in minutes (default: 15)"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 40)"}
                    },
                    "required": ["od_light_peak_uv", "od_dark_trough_uv"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = ElectrooculographyClient()
        test_res = client.evaluate_eog(
            od_light_peak_uv=880.0,
            od_dark_trough_uv=400.0,
            os_light_peak_uv=860.0,
            os_dark_trough_uv=390.0
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
