# Finalized concept

## Observable equivalence

For connected unweighted graphs with common labeled vertex set and source `s`, write

```
G ~_s H
```

descriptively when all of the following are identical:

- source-distance vector `d_s`;
- complete source shortest-path DAG `SPDAG_s`;
- source-to-vertex shortest-path multiplicities `sigma_s`;
- number of edges.

No new formal terminology is claimed by this notation.

## Failure-response separation

For a common edge `e` and target `t`, compare

```
d_{G-e}(s,t)
d_{H-e}(s,t).
```

The central validated statement is:

> There is an infinite family of connected unweighted graph pairs with identical intact source-shortest-path structure and equal edge counts, but with a finite single-edge replacement-distance gap linear in the number of vertices.

## Explicit family

For `L>=1`:

- common edge `s-r`;
- two length-`L` branches from `r` ending at `t` and `x`;
- an independent backup path of length `L+1` from `s` ending at `b`;
- `G` contains `b-t`;
- `H` contains `b-x`.

The differing edges join vertices at the same intact source distance, so neither appears in the source shortest-path DAG.

For the common failed edge `e=(s,r)`:

```
n = 3L + 3

d_{G-e}(s,t) = L + 2

d_{H-e}(s,t) = 3L + 2

gap = 2L = 2(n-3)/3.
```

Thus the verified lower-bound family gives a `Theta(n)` finite separation.

## Upper-bound context

For connected unweighted graphs with finite post-failure source-target distance, every simple replacement path has at most `n-1` edges. Consequently the absolute difference between two finite replacement distances is at most `n-2` (and trivially `O(n)`). Combined with the explicit family, the extremal order of growth is therefore `Theta(n)`.

The present repository verifies the lower-bound construction computationally; the upper bound is the elementary finite simple-path bound.
