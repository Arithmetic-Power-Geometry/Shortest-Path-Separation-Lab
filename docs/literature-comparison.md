# Literature comparison

The repository tests a representation-separation question; it is not positioned as a replacement-path algorithm.

## Closest established areas

1. **Replacement paths / shortest-path restoration.** These problems compute shortest paths after one or more failures. Recent work continues to improve algorithms and structural representations for replacement paths.

2. **Distance-sensitivity oracles (DSOs).** A DSO preprocesses the graph so failure-conditioned distance queries can be answered efficiently. This is explicitly failure-aware information.

3. **Fault-tolerant BFS, preservers and spanners.** These structures retain additional edges/information so distances or reachability remain available after failures.

## Separation tested here

This repository fixes the intact observable

```
S(G,s) = (d_s, SPDAG_s, sigma_s)
```

and asks whether equality of this observable, together with equal graph size, forces equality of single-edge replacement response.

The verified family answers **no** with a linear finite gap.

This distinction matters:

- replacement paths ask **how to compute** the changed distance;
- DSOs ask **what to preprocess/store** for fast failure queries;
- fault-tolerant preservers ask **what substructure preserves** failure-aware behavior;
- this lab asks **whether complete intact single-source shortest-path structure determines failure response at all**.

## Representative references used for comparison

- Afek et al. (PODC 2001), shortest-path restoration after edge failures; discussed in Choudhary & Dhiman, *A Deterministic Approach to Shortest Path Restoration in Edge Faulty Graphs*, STACS 2025.
- Bodwin, Grandoni, Parter, and Vassilevska Williams, *Preserving Distances in Very Faulty Graphs*, ICALP 2017, DOI: 10.4230/LIPIcs.ICALP.2017.73.
- Gupta and Khan, *Multiple Source Dual Fault Tolerant BFS Trees*, ICALP 2017, DOI: 10.4230/LIPIcs.ICALP.2017.127.
- Chechik and Zhang, *Faster Algorithms for Dual-Failure Replacement Paths*, ICALP 2024, DOI: 10.4230/LIPIcs.ICALP.2024.41.
- Chi, Duan, Wang, and Xie, *Undirected 3-Fault Replacement Path in Nearly Cubic Time*, ICALP 2025, DOI: 10.4230/LIPIcs.ICALP.2025.57.

## Novelty status

The exact finite-gap indistinguishability theorem validated here was not located in the targeted search used to build the lab. That is encouraging but is **not a proof of literature novelty**. A manuscript should still include a broader systematic review before claiming priority.
