"""
Ocular Electrooculography (EOG) & Arden Ratio (LP/DT) Client.
Zero-mock pure Python standard library implementation.
Calculates Dark Trough (DT in uV), Light Peak (LP in uV), Arden Ratio (LP / DT),
Arden Percentage Index, and Retinal Pigment Epithelium (RPE) functional integrity (ISCEV standards).
"""

import math
from typing import Dict, Any, Optional


class ElectrooculographyClient:
    """
    Evaluates the standing transepithelial potential of the Retinal Pigment Epithelium (RPE):
    - Dark Trough DT (uV): minimum resting potential in dark (normal: 200 - 600 uV)
    - Light Peak LP (uV): maximum generated standing potential in light (normal: 400 - 1200 uV)
    - Arden Ratio: LP / DT (normal >= 1.80)
    - Arden Percentage: (LP / DT) * 100% (normal >= 180%)
    - Interocular Arden Symmetry: |OD - OS| <= 0.25
    - Crucial differential diagnostic tool for Best Vitelliform Dystrophy, RPE atrophy, and chloroquine toxicity.
    """

    def __init__(self):
        pass

    def evaluate_eog(
        self,
        od_light_peak_uv: float,
        od_dark_trough_uv: float,
        os_light_peak_uv: Optional[float] = None,
        os_dark_trough_uv: Optional[float] = None,
        dark_adaptation_duration_minutes: Optional[int] = 15,
        light_adaptation_duration_minutes: Optional[int] = 15,
        patient_age_years: Optional[int] = 40
    ) -> Dict[str, Any]:
        """
        Calculates EOG Arden ratios and RPE transepithelial potential kinetics.
        od_light_peak_uv: Right eye Light Peak (LP) in uV (e.g. 850.0 uV).
        od_dark_trough_uv: Right eye Dark Trough (DT) in uV (e.g. 380.0 uV).
        """
        if od_light_peak_uv <= 0 or od_dark_trough_uv <= 0:
            raise ValueError("OD Light peak and dark trough must be strictly positive.")
        if os_light_peak_uv is not None and os_light_peak_uv <= 0:
            raise ValueError("OS Light peak must be strictly positive.")
        if os_dark_trough_uv is not None and os_dark_trough_uv <= 0:
            raise ValueError("OS Dark trough must be strictly positive.")

        od_arden_ratio = round(od_light_peak_uv / od_dark_trough_uv, 2)
        od_arden_pct = round(od_arden_ratio * 100.0, 1)

        os_arden_ratio = None
        os_arden_pct = None
        interocular_delta = None
        if os_light_peak_uv and os_dark_trough_uv:
            os_arden_ratio = round(os_light_peak_uv / os_dark_trough_uv, 2)
            os_arden_pct = round(os_arden_ratio * 100.0, 1)
            interocular_delta = round(abs(od_arden_ratio - os_arden_ratio), 2)

        # ISCEV Clinical Classification Standards:
        # Normal: Arden ratio >= 1.80 (>= 180%)
        # Subnormal / Borderline: 1.65 to 1.79 (165% - 179%)
        # Pathological / Abnormal: < 1.65 (< 165%)
        # Severely Extinguished / Flat: <= 1.15 (<= 115%)
        min_ratio = min(od_arden_ratio, os_arden_ratio) if os_arden_ratio is not None else od_arden_ratio

        if min_ratio <= 1.15:
            eog_status = "Extinguished Light Peak / Flat Electrooculogram"
            pathophysiology = "Complete or near-total absence of light-induced RPE depolarization; classic hallmark of Best Vitelliform Macular Dystrophy (BEST1 mutation) or end-stage panretinal atrophy."
        elif min_ratio < 1.65:
            eog_status = "Pathological / Abnormal Arden Ratio (< 1.65)"
            pathophysiology = "Marked disruption of RPE basolateral chloride channels and transepithelial potential; seen in generalized RPE degeneration, Best disease, or chloroquine retinopathy."
        elif min_ratio < 1.80:
            eog_status = "Subnormal / Borderline Arden Ratio (1.65 - 1.79)"
            pathophysiology = "Mild attenuation of light rise; monitor for early toxic retinopathy, carrier state, or subclinical maculopathy."
        else:
            eog_status = "Normal Physiological Electrooculogram (Intact RPE)"
            pathophysiology = "Robust light peak generation reflecting healthy photoreceptor outer segments and synchronized RPE ionic transport."

        # Interocular asymmetry alert
        asymmetry_alert = (interocular_delta is not None and interocular_delta > 0.25)

        return {
            "status": "success",
            "eog_metrics": {
                "od_right_eye": {
                    "light_peak_uv": round(od_light_peak_uv, 1),
                    "dark_trough_uv": round(od_dark_trough_uv, 1),
                    "arden_ratio": od_arden_ratio,
                    "arden_percentage": od_arden_pct
                },
                "os_left_eye": {
                    "light_peak_uv": round(os_light_peak_uv, 1),
                    "dark_trough_uv": round(os_dark_trough_uv, 1),
                    "arden_ratio": os_arden_ratio,
                    "arden_percentage": os_arden_pct
                } if os_arden_ratio is not None else None,
                "interocular_comparison": {
                    "interocular_arden_delta": interocular_delta,
                    "clinically_significant_asymmetry": asymmetry_alert
                } if os_arden_ratio is not None else None
            },
            "recording_context": {
                "dark_adaptation_duration_minutes": dark_adaptation_duration_minutes,
                "light_adaptation_duration_minutes": light_adaptation_duration_minutes,
                "normal_arden_lower_limit": 1.80,
                "patient_age_years": patient_age_years
            },
            "clinical_assessment": {
                "eog_functional_status": eog_status,
                "pathophysiology_summary": pathophysiology
            }
        }
