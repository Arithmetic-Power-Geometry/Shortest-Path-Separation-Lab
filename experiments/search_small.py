import itertools
import csv
from pathlib import Path
import networkx as nx
from src.structure import source_structure
from src.replacement import replacement_profile

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
    hits = []
    for n in range(3, max_n + 1):
        edges_n = n * (n - 1) // 2
        buckets = {}
        for mask in range(1 << edges_n):
            G = graph_from_mask(n, mask)
            if not nx.is_connected(G):
                continue
            s = 0
            key = (G.number_of_edges(), repr(source_structure(G, s)))
            prof = replacement_profile(G, s)
            if key in buckets:
                H, hprof = buckets[key]
                if prof != hprof:
                    hits.append((n, G.number_of_edges(), mask))
                    print("separation found at n=", n)
                    break
            else:
                buckets[key] = (G, prof)
        if hits:
            break
    with open("artifacts/small_search.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "m", "graph_mask"])
        w.writerows(hits)
    print("wrote artifacts/small_search.csv")

if __name__ == "__main__":
    main()
