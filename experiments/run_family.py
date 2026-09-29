import csv
from pathlib import Path
from src.constructions import finite_gap_family
from src.verify import verify_pair

def main():
    Path("artifacts").mkdir(exist_ok=True)
    rows = []
    for L in range(1, 41):
        G, H, s, e, t, meta = finite_gap_family(L)
        result = verify_pair(G, H, s, e, t)
        n = G.number_of_nodes()
        expected_G = meta["k"] + 1
        expected_H = meta["k"] + 1 + 2 * L
        rows.append({
            "L": L,
            "n": n,
            "n_formula": meta["n_formula"],
            "m_G": G.number_of_edges(),
            "m_H": H.number_of_edges(),
            "accepted": result["accepted"],
            "distance_G": result["distance_G"],
            "distance_H": result["distance_H"],
            "gap": result["gap"],
            "theoretical_gap": meta["theoretical_gap"],
            "expected_distance_G": expected_G,
            "expected_distance_H": expected_H,
            "formula_n_ok": n == meta["n_formula"],
            "formula_gap_ok": result["gap"] == meta["theoretical_gap"],
            "formula_G_ok": result["distance_G"] == expected_G,
            "formula_H_ok": result["distance_H"] == expected_H,
            **result["checks"],
        })

    out = Path("artifacts/family_results.csv")
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    failures = [r for r in rows if not (
        r["accepted"] and r["formula_n_ok"] and r["formula_gap_ok"]
        and r["formula_G_ok"] and r["formula_H_ok"]
    )]
    if failures:
        raise AssertionError(f"family verification failed: {failures[:3]}")

    print(f"verified {len(rows)} family instances")
    print("first:", rows[0])
    print("last:", rows[-1])

if __name__ == "__main__":
    main()
