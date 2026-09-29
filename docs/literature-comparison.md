# Literature comparison

This repository supports a representation-separation study; it is not presented as a new replacement-path algorithm, distance-sensitivity oracle, fault-tolerant BFS structure, or degree-sequence transformation method.

## Intact observable tested here

For a connected simple unweighted graph `G` with source `s`, the verified software fixes

```text
S+(G,s) = (d_s, SPDAG_s, sigma_s, deg_G)
```

where `d_s` is the complete source-distance vector, `SPDAG_s` is the complete source shortest-path DAG of tight edges, `sigma_s` is the exact source-to-vertex shortest-path multiplicity vector, and `deg_G` is the labeled degree vector.

The degree-preserving family uses a same-layer 2-switch. For `L >= 1`, the two graphs have identical `S+(G,s)`, equal edge counts, and finite post-failure distances after deletion of the same edge `e=(s,r)`, but

```text
d_G-e(s,t) = L + 2
d_H-e(s,t) = 3L + 2
gap          = 2L
n            = 4L + 3
```

so the verified family realizes `gap = (n-3)/2 = Theta(n)`.

## Closest established areas

1. **Replacement paths and shortest-path restoration.** These problems compute or restore shortest paths after one or more failures. They assume access to the full graph or to explicitly failure-aware information.
2. **Distance-sensitivity oracles.** These preprocess a graph so failed-edge or failed-vertex distance queries can be answered efficiently.
3. **Fault-tolerant BFS, preservers, and spanners.** These retain additional substructure so distances or reachability survive failures.
4. **Degree-preserving 2-switches.** The switch operation used by the construction is classical; its role here is to keep every labeled vertex degree fixed while changing same-layer adjacencies.
5. **Metric dimension and distance-based graph reconstruction.** These ask when distance observations identify vertices or reconstruct topology. They provide a useful sufficiency-side comparison but address a different information problem.

## Separation question

The question tested here is whether a rich intact single-source representation already determines a finite single-edge replacement response. The verified family answers **no**: two graphs can agree on source distances, every tight source edge, all source shortest-path multiplicities, every labeled vertex degree, and graph size, while the same edge failure exposes a linearly different finite source-target distance.

## Representative references

- Chechik, S., & Cohen, S. (2019). *Near Optimal Algorithms for the Single Source Replacement Paths Problem*. SODA 2019. DOI: 10.1137/1.9781611975482.126.
- Dey, D., & Gupta, M. (2022). *Near Optimal Algorithm for Fault Tolerant Distance Oracle and Single Source Replacement Path Problem*. ESA 2022. DOI: 10.4230/LIPIcs.ESA.2022.42.
- Harada, K., Kitamura, N., Izumi, T., & Masuzawa, T. (2024). *A Nearly Linear Time Construction of Approximate Single-Source Distance Sensitivity Oracles*. ESA 2024. DOI: 10.4230/LIPIcs.ESA.2024.65.
- Chechik, S., & Zhang, T. (2024). *Faster Algorithms for Dual-Failure Replacement Paths*. ICALP 2024. DOI: 10.4230/LIPIcs.ICALP.2024.41.
- Choudhary, K., & Dhiman, R. (2025). *A Deterministic Approach to Shortest Path Restoration in Edge Faulty Graphs*. STACS 2025. DOI: 10.4230/LIPIcs.STACS.2025.24.
- Chi, S., Duan, R., Wang, B., & Xie, T. (2025). *Undirected 3-Fault Replacement Path in Nearly Cubic Time*. ICALP 2025. DOI: 10.4230/LIPIcs.ICALP.2025.57.
- Parter, M., & Peleg, D. (2016). *Sparse Fault-Tolerant BFS Structures*. ACM Transactions on Algorithms, 13(1). DOI: 10.1145/2976741.
- Barrus, M. D. (2012). *On 2-switches and isomorphism classes*. Discrete Mathematics, 312(15), 2217-2222. DOI: 10.1016/j.disc.2012.04.014.
- Bereg, S., & Ito, H. (2017). *Transforming Graphs with the Same Graphic Sequence*. Journal of Information Processing, 25, 627-633. DOI: 10.2197/ipsjjip.25.627.
- Mahindre, G. S., & Jayasumana, A. P. (2022). *Link dimension and exact construction of graphs from distance vectors*. Discrete Applied Mathematics, 309, 160-171. DOI: 10.1016/j.dam.2021.11.013.
- Tillquist, R. C., Frongillo, R. M., & Lladser, M. E. (2023). *Getting the Lay of the Land in Discrete Space: A Survey of Metric Dimension and Its Applications*. SIAM Review, 65(4), 919-962. DOI: 10.1137/21M1409512.

## Novelty status

The repository validates the construction, formulas, and computational checks. It does not treat the classical mechanisms or surrounding problem classes above as new. The exact degree-preserving finite-gap separation statement was not located in the targeted literature audit used for this project; that is evidence for differentiation, not a claim of exhaustive priority.
