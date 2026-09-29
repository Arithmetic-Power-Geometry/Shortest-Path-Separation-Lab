import csv
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx
from src.constructions import finite_gap_family

COMPARISON_ROWS = [
    {
        "method": "Source distances",
        "pre_failure_information": "d_s(v) for every vertex",
        "failure_aware": "No",
        "distinguishes_family": "No",
        "role": "Baseline observable",
    },
    {
        "method": "Source shortest-path DAG",
        "pre_failure_information": "All tight source-oriented edges",
        "failure_aware": "No",
        "distinguishes_family": "No",
        "role": "Strong intact shortest-path structure",
    },
    {
        "method": "Shortest-path multiplicities",
        "pre_failure_information": "sigma_s(v) for every vertex",
        "failure_aware": "No",
        "distinguishes_family": "No",
        "role": "Counts intact shortest paths",
    },
    {
        "method": "Replacement-path recomputation",
        "pre_failure_information": "Full graph",
        "failure_aware": "Yes",
        "distinguishes_family": "Yes",
        "role": "Exact post-failure baseline",
    },
    {
        "method": "Distance-sensitivity oracle",
        "pre_failure_information": "Failure-aware preprocessed structure",
        "failure_aware": "Yes",
        "distinguishes_family": "Yes",
        "role": "Known fault-aware data-structure paradigm",
    },
    {
        "method": "Fault-tolerant BFS/preserver",
        "pre_failure_information": "Additional replacement-path information/subgraph",
        "failure_aware": "Yes",
        "distinguishes_family": "Yes",
        "role": "Known fault-tolerant preservation paradigm",
    },
]

def draw_witness(L=5):
    G, H, s, e, t, _ = finite_gap_family(L)
    # deterministic hand-positioned layout emphasizing identical visible tree
    pos = {s: (0, 0), "r": (1, 0)}
    for i in range(1, L):
        pos[f"t{i}"] = (1 + i, 1)
        pos[f"x{i}"] = (1 + i, -1)
    pos["t"] = (L + 1, 1)
    pos["x"] = (L + 1, -1)
    for i in range(1, L + 1):
        pos[f"b{i}"] = (i, 2.5)
    pos["b"] = (L + 1, 2.5)

    for name, X in [("G", G), ("H", H)]:
        plt.figure(figsize=(9, 4.8))
        nx.draw_networkx(X, pos=pos, with_labels=True, node_size=650, font_size=8)
        nx.draw_networkx_edges(X, pos=pos, edgelist=[e], width=3)
        plt.title(f"{name}: common shortest-path structure, different hidden same-level edge")
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(f"artifacts/witness_{name}.png", dpi=180)
        plt.close()

def main():
    Path("artifacts").mkdir(exist_ok=True)
    src = Path("artifacts/family_results.csv")
    if not src.exists():
        raise SystemExit("Run python -m experiments.run_family first")

    with src.open() as f:
        rows = list(csv.DictReader(f))

    accepted = [r for r in rows if r["accepted"] == "True"]

    with open("artifacts/table_summary.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "L", "n", "m", "distance_G_minus_e", "distance_H_minus_e",
            "observed_gap", "theoretical_gap", "all_invariants_equal"
        ])
        for r in accepted:
            w.writerow([
                r["L"], r["n"], r["m_G"], r["distance_G"], r["distance_H"],
                r["gap"], r["theoretical_gap"], r["same_source_structure"]
            ])

    with open("artifacts/comparison_existing.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COMPARISON_ROWS[0].keys())
        w.writeheader()
        w.writerows(COMPARISON_ROWS)

    xs = [int(r["n"]) for r in accepted]
    ys = [int(r["gap"]) for r in accepted]
    theory = [2 * (x - 3) / 3 for x in xs]
    plt.figure()
    plt.plot(xs, ys, marker="o", label="verified gap")
    plt.plot(xs, theory, linestyle="--", label="2(n-3)/3")
    plt.xlabel("Number of vertices n")
    plt.ylabel("Finite replacement-distance gap")
    plt.title("Linear failure-response separation under identical source structure")
    plt.legend()
    plt.tight_layout()
    plt.savefig("artifacts/gap_vs_n.png", dpi=180)
    plt.close()

    draw_witness()

    with open("artifacts/algorithm.txt", "w") as f:
        f.write(
            "Algorithm: Strict Finite Separation Verification\n"
            "Input: connected unweighted graphs G,H; common source s; common failed edge e; target t.\n"
            "1. Verify identical labeled vertex sets and equal edge counts.\n"
            "2. Compute d_s, the complete source shortest-path DAG, and sigma_s for both graphs.\n"
            "3. Reject unless all three intact source observables are exactly equal.\n"
            "4. Delete the same edge e from both graphs.\n"
            "5. Recompute d_{G-e}(s,t) and d_{H-e}(s,t).\n"
            "6. Reject if either distance is infinite or if the distances are equal.\n"
            "7. Record the finite gap and verify it against the family formula when applicable.\n"
        )

    with open("artifacts/theorem_check.txt", "w") as f:
        f.write(
            "Verified family claim\n"
            "For parameter L>=1, the construction has n=3L+3 vertices.\n"
            "The intact source-distance vector, source shortest-path DAG, and source shortest-path counts coincide.\n"
            "The graphs have equal edge counts.\n"
            "After deletion of e=(s,r), d_G(s,t)=L+2 and d_H(s,t)=3L+2.\n"
            "Therefore the finite replacement-distance gap is 2L = 2(n-3)/3 = Theta(n).\n"
        )

    print("artifact generation complete")

if __name__ == "__main__":
    main()
