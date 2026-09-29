import csv
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx
from src.constructions import finite_gap_family

COMPARISON_ROWS = [
    {"method":"Source distances","pre_failure_information":"d_s(v) for every vertex","failure_aware":"No","distinguishes_family":"No","role":"Baseline observable"},
    {"method":"Source shortest-path DAG","pre_failure_information":"All tight source-oriented edges","failure_aware":"No","distinguishes_family":"No","role":"Strong intact shortest-path structure"},
    {"method":"Shortest-path multiplicities","pre_failure_information":"sigma_s(v) for every vertex","failure_aware":"No","distinguishes_family":"No","role":"Counts intact shortest paths"},
    {"method":"Labeled degree vector","pre_failure_information":"deg(v) for every labeled vertex","failure_aware":"No","distinguishes_family":"No","role":"Additional intact structural invariant"},
    {"method":"Replacement-path recomputation","pre_failure_information":"Full graph","failure_aware":"Yes","distinguishes_family":"Yes","role":"Exact post-failure baseline"},
    {"method":"Distance-sensitivity oracle","pre_failure_information":"Failure-aware preprocessed structure","failure_aware":"Yes","distinguishes_family":"Yes","role":"Known fault-aware data-structure paradigm"},
    {"method":"Fault-tolerant BFS/preserver","pre_failure_information":"Additional replacement-path information/subgraph","failure_aware":"Yes","distinguishes_family":"Yes","role":"Known fault-tolerant preservation paradigm"},
]

def draw_witness(L=4):
    G,H,s,e,t,_=finite_gap_family(L)
    pos={s:(0,0),"r":(1,0)}
    levels={"t":1.2,"x":-1.2,"y":-2.4}
    for endpoint,ycoord in levels.items():
        for i in range(1,L):
            pos[f"{endpoint}{i}"]=(1+i,ycoord)
        pos[endpoint]=(L+1,ycoord)
    for i in range(1,L+1):
        pos[f"b{i}"]=(i,2.6)
    pos["b"]=(L+1,2.6)
    for name,X in [("G",G),("H",H)]:
        plt.figure(figsize=(10,5.5))
        nx.draw_networkx(X,pos=pos,with_labels=True,node_size=600,font_size=8)
        nx.draw_networkx_edges(X,pos=pos,edgelist=[e],width=3)
        plt.title(f"{name}: degree-preserving hidden same-layer switch")
        plt.axis("off"); plt.tight_layout()
        plt.savefig(f"artifacts/witness_{name}.png",dpi=180); plt.close()

def main():
    Path("artifacts").mkdir(exist_ok=True)
    with open("artifacts/family_results.csv") as f:
        rows=list(csv.DictReader(f))
    accepted=[r for r in rows if r["accepted"]=="True"]
    with open("artifacts/table_summary.csv","w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["L","n","m","distance_G_minus_e","distance_H_minus_e","observed_gap","theoretical_gap","same_source_structure","same_labeled_degrees"])
        for r in accepted:
            w.writerow([r["L"],r["n"],r["m_G"],r["distance_G"],r["distance_H"],r["gap"],r["theoretical_gap"],r["same_source_structure"],r["same_labeled_degrees"]])
    with open("artifacts/comparison_existing.csv","w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=COMPARISON_ROWS[0].keys()); w.writeheader(); w.writerows(COMPARISON_ROWS)
    xs=[int(r["n"]) for r in accepted]; ys=[int(r["gap"]) for r in accepted]
    theory=[(x-3)/2 for x in xs]
    plt.figure(); plt.plot(xs,ys,marker="o",label="verified gap"); plt.plot(xs,theory,linestyle="--",label="(n-3)/2")
    plt.xlabel("Number of vertices n"); plt.ylabel("Finite replacement-distance gap")
    plt.title("Degree-preserving failure-response separation"); plt.legend(); plt.tight_layout()
    plt.savefig("artifacts/gap_vs_n.png",dpi=180); plt.close()
    draw_witness()
    with open("artifacts/algorithm.txt","w") as f:
        f.write("Algorithm: Strict Degree-Preserving Separation Verification\n1. Verify identical labeled vertices, equal edge counts, and equal labeled degree at every vertex.\n2. Compute d_s, complete source SPDAG, and sigma_s in both graphs.\n3. Reject unless all intact observables are exactly equal.\n4. Delete the same common edge e.\n5. Compute both source-target replacement distances.\n6. Reject if either is infinite or equal.\n7. Verify the observed gap against the family formula.\n")
    with open("artifacts/theorem_check.txt","w") as f:
        f.write("Verified degree-preserving family claim\nFor L>=1, n=4L+3.\nThe labeled degree vector, source-distance vector, complete source SPDAG, source shortest-path counts, and edge count coincide.\nAfter e=(s,r), d_G(s,t)=L+2 and d_H(s,t)=3L+2.\nThus the finite gap is 2L=(n-3)/2=Theta(n).\n")
    print("artifact generation complete")

if __name__=="__main__":
    main()
