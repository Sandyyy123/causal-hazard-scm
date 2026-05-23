"""
SCM construction using DoWhy CausalModel.
DAG reflects wildfire hazard pathways with cascading risk.
"""
import dowhy
from dowhy import CausalModel
import networkx as nx


WILDFIRE_DAG = """
digraph {
    fuel_moisture -> fire_intensity;
    wind_speed -> fire_intensity;
    fuel_load -> fire_intensity;
    fire_intensity -> debris_flow_prob;
    slope_pct -> debris_flow_prob;
    fire_intensity -> asset_damage;
    debris_flow_prob -> asset_damage;
    asset_proximity -> asset_damage;
    fuel_moisture -> asset_damage;
}
"""


def build_wildfire_scm(data):
    """
    Build and return a DoWhy CausalModel for wildfire hazard.
    Designed hazard-agnostic: swap DAG string to model flood, wind, or earthquake.
    """
    model = CausalModel(
        data=data,
        treatment="fuel_moisture",
        outcome="asset_damage",
        graph=WILDFIRE_DAG
    )
    return model


def get_dag_summary():
    """Return DAG node and edge count for reporting."""
    G = nx.DiGraph()
    edges = [
        ("fuel_moisture", "fire_intensity"),
        ("wind_speed", "fire_intensity"),
        ("fuel_load", "fire_intensity"),
        ("fire_intensity", "debris_flow_prob"),
        ("slope_pct", "debris_flow_prob"),
        ("fire_intensity", "asset_damage"),
        ("debris_flow_prob", "asset_damage"),
        ("asset_proximity", "asset_damage"),
        ("fuel_moisture", "asset_damage"),
    ]
    G.add_edges_from(edges)
    return {"nodes": G.number_of_nodes(), "edges": G.number_of_edges()}
