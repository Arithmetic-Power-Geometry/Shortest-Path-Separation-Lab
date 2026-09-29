# Shortest-Path Separation Lab

A reproducible graph-algorithm laboratory for testing whether identical **pre-failure source shortest-path structure** can coexist with substantially different **single-edge replacement-distance behavior**.

## Research question

For connected, unweighted graphs `G` and `H` on the same labeled vertex set with common source `s`, define the observable source-shortest-path structure

```
S(G,s) = (d_s, SPDAG_s, sigma_s)
```

where:

- `d_s(v)` is the shortest-path distance from `s` to `v`;
- `SPDAG_s` is the directed acyclic graph containing exactly the oriented edges `u -> v` satisfying `d_s(v)=d_s(u)+1`;
- `sigma_s(v)` is the number of shortest paths from `s` to `v`.

The primary experiment searches for pairs satisfying

```
|V(G)| = |V(H)|
|E(G)| = |E(H)|
S(G,s) = S(H,s)
```

but, for a corresponding failed edge `e` and target `t`, both post-failure distances are finite and

```
d_{G-e}(s,t) != d_{H-e}(s,t).
```

The extremal target is a family with a gap growing linearly with `n`.

## Why this repository exists

The repository is a theorem-validation lab. It does not assume novelty. Every accepted witness must pass mechanical checks showing that the requested pre-failure invariants are exactly equal before any post-failure separation is measured.

## Current comparison context

This project is adjacent to, but distinct from, classical replacement paths, distance-sensitivity oracles, and fault-tolerant BFS/preserver structures. Those lines of work compute or preserve failure-aware distances. This lab instead tests a separation question: how different can failure response be among graphs that are indistinguishable under a chosen complete source-shortest-path observable?

## Reproduce

```bash
python -m experiments.run_family
python -m experiments.search_small
python -m experiments.make_artifacts
```

Generated artifacts are written to `artifacts/`.

## Repository structure

- `src/structure.py` — source distances, shortest-path DAG, multiplicities
- `src/replacement.py` — single-edge replacement distances
- `src/verify.py` — strict pair validator
- `src/constructions.py` — explicit candidate families
- `experiments/run_family.py` — family sweep
- `experiments/search_small.py` — exact small-graph search
- `experiments/make_artifacts.py` — CSV/table/figure artifact generation
- `.github/workflows/reproduce.yml` — reproducible CI workflow

## License and copyright

Copyright © 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License, Version 2.0.
