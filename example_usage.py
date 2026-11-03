"""
Example usage for Ocular Electrooculography (EOG) & Arden Ratio Skill.
"""

from client import ElectrooculographyClient


def main():
    client = ElectrooculographyClient()

    print("--- Case 1: Normal Physiological Electrooculogram ---")
    normal_case = client.evaluate_eog(
        od_light_peak_uv=920.0,
        od_dark_trough_uv=420.0,
        os_light_peak_uv=890.0,
        os_dark_trough_uv=410.0,
        patient_age_years=30
    )
    print("OD Arden Ratio:", normal_case["eog_metrics"]["od_right_eye"]["arden_ratio"])
    print("OS Arden Ratio:", normal_case["eog_metrics"]["os_left_eye"]["arden_ratio"])
    print("Interocular Delta:", normal_case["eog_metrics"]["interocular_comparison"]["interocular_arden_delta"])
    print("Functional Status:", normal_case["clinical_assessment"]["eog_functional_status"])
    print("Pathophysiology:", normal_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Best Vitelliform Macular Dystrophy (Pathognomonic Flat EOG) ---")
    best_case = client.evaluate_eog(
        od_light_peak_uv=340.0,
        od_dark_trough_uv=310.0,
        os_light_peak_uv=330.0,
        os_dark_trough_uv=300.0,
        patient_age_years=14
    )
    print("OD Arden Ratio:", best_case["eog_metrics"]["od_right_eye"]["arden_ratio"])
    print("OS Arden Ratio:", best_case["eog_metrics"]["os_left_eye"]["arden_ratio"])
    print("Functional Status:", best_case["clinical_assessment"]["eog_functional_status"])
    print("Pathophysiology:", best_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Hydroxychloroquine Retinopathy (Subnormal Light Rise) ---")
    hcq_case = client.evaluate_eog(
        od_light_peak_uv=610.0,
        od_dark_trough_uv=360.0,
        os_light_peak_uv=600.0,
        os_dark_trough_uv=355.0,
        patient_age_years=58
    )
    print("OD Arden Ratio:", hcq_case["eog_metrics"]["od_right_eye"]["arden_ratio"])
    print("Functional Status:", hcq_case["clinical_assessment"]["eog_functional_status"])
    print("Pathophysiology:", hcq_case["clinical_assessment"]["pathophysiology_summary"])


if __name__ == "__main__":
    main()
