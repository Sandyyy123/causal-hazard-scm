"""
Counterfactual inference over the wildfire SCM.
Implements do-calculus interventions and ATE computation via DoWhy.
"""
import numpy as np
import pandas as pd
from dowhy import CausalModel
from scm_builder import build_wildfire_scm, WILDFIRE_DAG


def compute_ate(model, data, treatment, outcome, t0, t1):
    """
    Compute Average Treatment Effect (ATE) via do-calculus.
    ATE = E[Y | do(X=t1)] - E[Y | do(X=t0)]
    """
    identified = model.identify_effect(proceed_when_unidentifiable=True)
    estimator = model.estimate_effect(
        identified,
        method_name="backdoor.linear_regression",
        control_value=t0,
        treatment_value=t1,
        confidence_intervals=False,
    )
    return estimator.value


def run_counterfactual(model, data_subset, intervention_var, intervention_val):
    """
    Asset-level counterfactual: force intervention_var to intervention_val,
    predict counterfactual outcome for each row.
    Returns DataFrame with observed and counterfactual asset_damage.
    """
    result = data_subset.copy()
    # Simplified counterfactual via structural equations
    # In production: use DoWhy twin-network or StructuralCausalModel.do()
    cf_data = data_subset.copy()
    cf_data[intervention_var] = intervention_val

    # Recompute downstream nodes using learned structural equations
    cf_data["fire_intensity"] = (
        0.6 * (1 - cf_data["fuel_moisture"]) +
        0.2 * (cf_data["wind_speed"] / 30) +
        0.2 * cf_data["fuel_load"]
    ).clip(0, 1)
    cf_data["debris_flow_prob"] = (
        0.5 * cf_data["fire_intensity"] +
        0.3 * (cf_data["slope_pct"] / 60)
    ).clip(0, 1)
    cf_data["asset_damage_cf"] = (
        0.5 * cf_data["fire_intensity"] +
        0.2 * cf_data["debris_flow_prob"] +
        0.3 * np.exp(-cf_data["asset_proximity"])
    ).clip(0, 1)

    result["asset_damage_cf"] = cf_data["asset_damage_cf"].values
    result["counterfactual_delta"] = result["asset_damage_cf"] - result["asset_damage"]
    return result


def portfolio_counterfactual_ranking(model, data, intervention_var, t0, t1):
    """
    Rank assets by counterfactual damage delta for capital allocation.
    Returns DataFrame sorted by risk reduction potential.
    """
    cf = run_counterfactual(model, data, intervention_var, t1)
    cf["baseline_damage"] = data["asset_damage"]
    ranking = cf[["baseline_damage", "asset_damage_cf", "counterfactual_delta"]].copy()
    ranking["risk_reduction_pct"] = (-ranking["counterfactual_delta"] / ranking["baseline_damage"] * 100).round(1)
    return ranking.sort_values("counterfactual_delta")
