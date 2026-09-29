from .structure import source_structure
from .replacement import distance_without_edge

def verify_pair(G, H, source, failed_edge, target, require_equal_degree_sequence=False):
    checks = {
        "same_vertices": tuple(sorted(G)) == tuple(sorted(H)),
        "same_edge_count": G.number_of_edges() == H.number_of_edges(),
        "same_source_structure": source_structure(G, source) == source_structure(H, source),
    }
    if require_equal_degree_sequence:
        checks["same_labeled_degrees"] = all(G.degree(v) == H.degree(v) for v in G)

    dg = distance_without_edge(G, source, target, failed_edge)
    dh = distance_without_edge(H, source, target, failed_edge)
    checks["finite_G"] = dg is not None
    checks["finite_H"] = dh is not None
    checks["separated"] = dg != dh
    accepted = all(checks.values())
    return {
        "accepted": accepted,
        "checks": checks,
        "distance_G": dg,
        "distance_H": dh,
        "gap": None if dg is None or dh is None else abs(dg-dh),
    }
