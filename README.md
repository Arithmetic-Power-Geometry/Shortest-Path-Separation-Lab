# Shortest-Path Separation Lab

A reproducible graph-algorithm laboratory for testing how much **single-edge failure response** can differ between graphs that are indistinguishable under a strong intact single-source shortest-path observable.

## Frozen concept

For a connected unweighted graph `G) with source `s`, define

```
S(G,s) = (d_s, SPDAG_s, sigma_s)
```

where:

- `d_s(v)` is the exact distance from `s` to every vertex;
- `SPDAG_s` contains every directed tight edge `u -> v` with `d_s(v)=d_s(u)+1`;
- `sigma_s(v)` is the exact number of shortest paths from `s` to `v`.

The lab studies pairs `G,H` with the same labeled vertex set, the same edge count, and

```
S(G,s) = S(H,s),
```

but whose distances after deletion of the **same common edge** differ.

## Explicit finite-gap family

For parameter `L>=1`:

1. add a common edge `s-r`;
2. from `r`, create two length-`L` branches ending at `t` and `x`;
3. independently create a backup path of length `L+1` from `s` ending at `b`;
4. in `G`, add the same-level edge `b-t`;
5. in `H`, add the same-level edge `b-x`.

The differing edge is absent from the intact source shortest-path DAG because `b,t,x` all lie at the same source distance.

After failure of the common edge `e=(s,r)`:

```
d_{G-e}(s,t) = L + 2
d_{H-e}(s,t) = 3L + 2
gap            = 2L
```

The construction has

```
n = 3L + 3,
```

hence

```
gap = 2(n-3)/3 = Theta(n).
```

The workflow verifies these identities mechanically; the formulas are not accepted merely because they appear in this README.

## Comparison with existing paradigms

The project is intentionally not presented as a new replacement-path algorithm. Classical replacement paths compute shortest routes after failures; distance-sensitivity oracles preprocess a graph to answer failure-conditioned distances; fault-tolerant BFS/preserver structures explicitly retain additional failure-aware information.

This lab asks a different separation question: **how different can failure response be when the intact source shortest-path structure is exactly the same?** The generated `comparison_existing.csv` records this distinction operationally.

## Reproduce

```bash
pip install -r requirements.txt
python -m experiments.run_family
python -m experiments.search_small
python -m experiments.make_artifacts
```

Generated outputs:

- `family_results.csv` — row-by-row theorem checks
- `small_search.csv` — smallest strict finite-vs-finite collision found by exhaustive search within the configured range
- `table_summary.csv` — publication-ready numeric summary
- `comparison_existing.csv` — comparison against standard intact/fault-aware paradigms
- `gap_vs_n.png` — empirical/theoretical linear-gap figure
- `witness_G.png`, `witness_H.png` — explicit witness visualization
- `algorithm.txt` — verification algorithm
- `theorem_check.txt` — machine-generated theorem statement and formulas

GitHub Actions runs the full workflow on every push and uploads the artifact bundle.

## Research status

The repository validates the mathematics and produces reproducible artifacts. It does **not** by itself establish literature novelty. The closest established areas include replacement paths, distance-sensitivity oracles, and fault-tolerant shortest-path preservers.

## License

Copyright © 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License, Version 2.0.
