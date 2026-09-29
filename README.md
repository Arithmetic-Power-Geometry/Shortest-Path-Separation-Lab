# Shortest-Path Separation Lab

A reproducible graph-algorithm laboratory for studying how strongly two graphs can agree before a single edge failure reveals different shortest-path behavior.

## Frozen concept

For a connected simple unweighted graph G with source s, define the intact observable

```
S+(G,s) = (d_s, SPDAG_s, sigma_s, deg_G)
```

where d_s is the complete source-distance vector, SPDAG_s is the complete directed tight-edge shortest-path DAG, sigma_s gives the number of source shortest paths to every vertex, and deg_G is the labeled degree vector.

The lab studies pairs G,H on the same labeled vertex set with equal edge count and S+(G,s)=S+(H,s), but with different finite source-target distances after deletion of the same common edge.

## Degree-preserving finite-gap family

For L>=1, use a common edge s-r, three length-L branches from r ending at t,x,y, and an independent length-(L+1) backup path from s ending at b. Apply the same-layer degree-preserving 2-switch

```
G: {b-t, x-y}
H: {b-x, t-y}.
```

All four endpoints have the same intact source distance, so the switched edges are absent from the source SPDAG. Every labeled vertex has the same degree in G and H.

After failure e=(s,r):

```
d_{G-e}(s,t) = L+2
d_{H-e}(s,t) = 3L+2
gap = 2L.
```

The family has n=4L+3, hence gap=(n-3)/2=Theta(n). The workflow verifies the invariant equalities and formulas mechanically.

## Reproduce

```bash
pip install -r requirements.txt
python -m experiments.run_family
python -m experiments.search_small
python -m experiments.make_artifacts
```

Artifacts include theorem checks, family results, a small-instance search, comparison table, gap figure, and explicit witness diagrams.

## Research status

The repository validates the construction and reproducibility claims. It does not treat replacement paths, distance-sensitivity oracles, fault-tolerant BFS/preservers, or degree-preserving 2-switches themselves as novel. The research question is the failure-response separation that remains after the listed intact observables are fixed.

## License

Copyright © 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License, Version 2.0.
