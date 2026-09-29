import csv
from pathlib import Path
import matplotlib.pyplot as plt

def main():
    Path("artifacts").mkdir(exist_ok=True)
    src = Path("artifacts/family_results.csv")
    if not src.exists():
        raise SystemExit("Run python -m experiments.run_family first")
    with src.open() as f:
        rows = list(csv.DictReader(f))
    accepted = [r for r in rows if r["accepted"] == "True" and r["gap"] not in ("", "None")]
    with open("artifacts/table_summary.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "m", "distance_G_minus_e", "distance_H_minus_e", "gap"])
        for r in accepted:
            w.writerow([r["n"], r["m_G"], r["distance_G"], r["distance_H"], r["gap"]])

    if accepted:
        xs = [int(r["n"]) for r in accepted]
        ys = [int(r["gap"]) for r in accepted]
        plt.figure()
        plt.plot(xs, ys, marker="o")
        plt.xlabel("Number of vertices n")
        plt.ylabel("Finite replacement-distance gap")
        plt.title("Failure-response separation under identical source structure")
        plt.tight_layout()
        plt.savefig("artifacts/gap_vs_n.png", dpi=180)
        plt.close()

    with open("artifacts/algorithm.txt", "w") as f:
        f.write(
            "Algorithm: Strict Separation Witness Verification\n"
            "1. Compute source distances, shortest-path DAG and shortest-path counts for G and H.\n"
            "2. Reject unless these observables and |V|, |E| are identical.\n"
            "3. Delete the same corresponding edge in both graphs.\n"
            "4. Recompute source-target distance in each surviving graph.\n"
            "5. Reject if either distance is infinite or if the distances are equal.\n"
            "6. Record the finite gap and the verified witness.\n"
        )
    print("artifact generation complete")

if __name__ == "__main__":
    main()
