"""
Causal Hazard SCM - Wildfire Phase 1 Demo
Runs in demo mode with synthetic data when real geospatial data is absent.
"""
import numpy as np
import pandas as pd
from scm_builder import build_wildfire_scm
from counterfactual import run_counterfactual, compute_ate


def generate_demo_data(n=500, seed=42):
    """Synthetic wildfire hazard dataset for demo purposes."""
    rng = np.random.default_rng(seed)
    data = pd.DataFrame({
        "fuel_moisture": rng.beta(2, 5, n),          # 0-1, lower = drier = riskier
        "wind_speed": rng.gamma(2, 5, n),             # mph
        "slope_pct": rng.exponential(15, n),          # percent grade
        "fuel_load": rng.uniform(0.2, 1.0, n),        # 0-1 normalized
        "asset_proximity": rng.exponential(0.3, n),   # km to asset
    })
    # Structural equations (simplified)
    data["fire_intensity"] = (
        0.6 * (1 - data["fuel_moisture"]) +
        0.2 * (data["wind_speed"] / 30) +
        0.2 * data["fuel_load"] +
        rng.normal(0, 0.05, n)
    ).clip(0, 1)
    data["debris_flow_prob"] = (
        0.5 * data["fire_intensity"] +
        0.3 * (data["slope_pct"] / 60) +
        rng.normal(0, 0.05, n)
    ).clip(0, 1)
    data["asset_damage"] = (
        0.5 * data["fire_intensity"] +
        0.2 * data["debris_flow_prob"] +
        0.3 * np.exp(-data["asset_proximity"]) +
        rng.normal(0, 0.05, n)
    ).clip(0, 1)
    return data


def main():
    print("=== Causal Hazard SCM - Wildfire Phase 1 ===")
    print("Running in DEMO MODE with synthetic data
")

    data = generate_demo_data(n=500)
    print(f"Generated {len(data)} synthetic asset observations")
    print(data.describe().round(3).to_string(), "
")

    model = build_wildfire_scm(data)
    print("SCM built and identified
")

    # Counterfactual: high vs low fuel moisture
    ate_result = compute_ate(model, data, treatment="fuel_moisture",
                              outcome="asset_damage",
                              t0=0.40, t1=0.15)
    print(f"ATE(fuel_moisture: 0.40 -> 0.15) on asset_damage: {ate_result:.4f}")
    print("  Interpretation: drought conditions increase expected damage by this amount
")

    # Asset-level counterfactual
    cf = run_counterfactual(model, data.head(5), "fuel_moisture", 0.15)
    print("Asset-level counterfactual (fuel_moisture forced to 0.15):")
    print(cf[["asset_damage", "asset_damage_cf", "counterfactual_delta"]].round(3).to_string())


if __name__ == "__main__":
    main()
