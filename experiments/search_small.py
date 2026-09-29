import itertools
import csv
from pathlib import Path
import networkx as nx
from src.structure import source_structure
from src.replacement import distance_without_edge

def graph_from_mask(n, mask):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    edges = list(itertools.combinations(range(n), 2))
    for i, e in enumerate(edges):
        if mask & (1 << i):
            G.add_edge(*e)
    return G

def main(max_n=6):
    Path("artifacts").mkdir(exist_ok=True)
    witness = None

    for n in range(3, max_n + 1):
        edges_n = n * (n - 1) // 2
        buckets = {}
        for mask in range(1 << edges_n):
            G = graph_from_mask(n, mask)
            if not nx.is_connected(G):
                continue
            s = 0
            key = (G.number_of_edges(), repr(source_structure(G, s)))
            buckets.setdefault(key, []).append((mask, G))

        for key, members in buckets.items():
            if len(members) < 2:
                continue
            for i in range(len(members)):
                mask_g, G = members[i]
                for j in range(i + 1, len(members)):
                    mask_h, H = members[j]
                    common_edges = sorted(set(G.edges()) & set(H.edges()))
                    for e in common_edges:
                        for t in range(n):
                            dg = distance_without_edge(G, s, t, e)
                            dh = distance_without_edge(H, s, t, e)
                            if dg is not None and dh is not None and dg != dh:
                                witness = {
                                    "n": n,
                                    "m": G.number_of_edges(),
                                    "mask_G": mask_g,
                                    "mask_H": mask_h,
                                    "failed_u": e[0],
                                    "failed_v": e[1],
                                    "target": t,
                                    "distance_G": dg,
                                    "distance_H": dh,
                                    "gap": abs(dg - dh),
                                    "edges_G": repr(sorted(G.edges())),
                                    "edges_H": repr(sorted(H.edges())),
                                }
                                break
                        if witness:
                            break
                    if witness:
                        break
                if witness:
                    break
            if witness:
                break
        if witness:
            break

    out = Path("artifacts/small_search.csv")
    fields = [
        "n", "m", "mask_G", "mask_H", "failed_u", "failed_v", "target",
        "distance_G", "distance_H", "gap", "edges_G", "edges_H"
    ]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        if witness:
            w.writerow(witness)

    if witness:
        print("smallest finite-vs-finite strict collision found:", witness)
    else:
        print(f"no finite-vs-finite strict collision found through n={max_n}")

if __name__ == "__main__":
    main()
