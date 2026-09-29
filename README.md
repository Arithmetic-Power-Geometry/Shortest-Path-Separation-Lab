# Shortest-Path Separation Lab

Reproducible software and verification artifacts for the study:

**Intact Shortest-Path Structure Does Not Determine Failure Response: A Tight Degree-Preserving Separation**

Mohammad Amir Khusru Akhtar  
Usha Martin University, Ranchi, India

## Overview

This repository implements and verifies a graph family showing that a strong intact single-source shortest-path description can remain identical while the response to the same edge failure differs substantially.

For a connected simple unweighted graph (G) with source (s), define

```text
S+(G,s) = (d_s, SPDAG_s, sigma_s, deg_G)
```

where:

- `d_s` is the complete source-distance vector,
- `SPDAG_s` is the full source shortest-path DAG of tight edges,
- `sigma_s` is the exact number of shortest (s)-to-(v) paths for every vertex (v), and
- `deg_G` is the full labeled degree vector.

The construction gives graph pairs (G,H) on the same labeled vertex set with equal edge count and identical (S+(G,s)), but with different finite source-target replacement distances after deletion of the same common edge.

## Degree-preserving separation family

For (L \ge 1), the construction uses:

- a common edge (s-r),
- three length-(L) branches from (r) ending at (t,x,y), and
- an independent length-((L+1)) backup path from (s) ending at (b).

The two graphs differ only by a same-layer degree-preserving 2-switch:

```text
G: {b-t, x-y}
H: {b-x, t-y}
```

All four switched endpoints lie at the same intact source distance (L+1). The switched edges are therefore non-tight and absent from the source shortest-path DAG, while the complete distance vector, shortest-path multiplicities, and every labeled vertex degree remain unchanged.

For the common failed edge (e=(s,r)):

```text
d_{G-e}(s,t) = L + 2
d_{H-e}(s,t) = 3L + 2
gap          = 2L
n            = 4L + 3
```

Hence

```text
gap = (n - 3)/2 = Theta(n).
```

A padding construction extends the linear lower bound to every (n \ge 7), and the universal finite upper bound gives

```text
(n - 6)/2 <= Delta_n <= n - 2,
```

so the extremal finite ambiguity satisfies `Delta_n = Theta(n)`.

## Reproducibility

Install dependencies and run:

```bash
pip install -r requirements.txt
python -m experiments.run_family
python -m experiments.search_small
python -m experiments.make_artifacts
```

The software includes:

- construction of the degree-preserving graph family,
- exact source-distance computation,
- full source shortest-path DAG extraction,
- shortest-path multiplicity computation,
- failed-edge replacement-distance computation,
- strict invariant verification,
- exhaustive small-graph search,
- artifact generation, and
- automated reproducibility checks through GitHub Actions.

The family sweep verifies the construction over 40 parameter values and checks the stated formulas and invariant equalities mechanically.

## Scope

The repository does not present replacement paths, distance-sensitivity oracles, fault-tolerant BFS structures, shortest-path DAGs, or degree-preserving 2-switches as new concepts. The contribution studied here is the failure-response separation that persists even after the intact observable above is fixed exactly.

The complete labeled all-pairs distance matrix is a sufficiency endpoint: in a simple unweighted graph, (uv) is an edge exactly when (d(u,v)=1), so the full metric reconstructs the graph and therefore determines every single-edge replacement response.

## Citation

Please cite the associated preprint as:

Akhtar, M. A. K. (2026). *Intact Shortest-Path Structure Does Not Determine Failure Response: A Tight Degree-Preserving Separation* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23035855

## License

Copyright © 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License, Version 2.0.
