import csv
from pathlib import Path
from src.constructions import path_with_detour_pair
from src.verify import verify_pair

def main():
    Path("artifacts").mkdir(exist_ok=True)
    rows = []
    for k in range(5, 41):
        G, H, s, e, t = path_with_detour_pair(k)
        result = verify_pair(G, H, s, e, t)
        rows.append({
            "k": k,
            "n": G.number_of_nodes(),
            "m_G": G.number_of_edges(),
            "m_H": H.number_of_edges(),
            "accepted": result["accepted"],
            "distance_G": result["distance_G"],
            "distance_H": result["distance_H"],
            "gap": result["gap"],
            **result["checks"],
        })
    with open("artifacts/family_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print("wrote artifacts/family_results.csv")
    for r in rows:
        if r["accepted"]:
            print("accepted witness", r)
            break

if __name__ == "__main__":
    main()
