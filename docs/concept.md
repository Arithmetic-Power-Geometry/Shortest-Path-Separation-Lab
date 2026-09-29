# Finalized concept

## Observable equivalence

For connected simple unweighted graphs on a common labeled vertex set with source s, compare

```
S+(G,s) = (d_s, SPDAG_s, sigma_s, deg_G).
```

Equality means identical source distances, identical complete source shortest-path DAG, identical source shortest-path multiplicities, and identical degree at every labeled vertex.

## Degree-preserving failure-response separation

For L>=1 construct a common edge s-r, three length-L branches from r ending at t,x,y, and an independent length-(L+1) path from s ending at b. The graphs differ only by a degree-preserving same-layer 2-switch:

```
G: {b-t, x-y}
H: {b-x, t-y}.
```

Because b,t,x,y all lie at source distance L+1, the switched edges are non-tight and absent from the intact source SPDAG. They do not alter d_s or sigma_s.

For e=(s,r):

```
n = 4L+3
d_{G-e}(s,t) = L+2
d_{H-e}(s,t) = 3L+2
gap = 2L = (n-3)/2.
```

Thus the family gives a finite Omega(n) separation while preserving S+ exactly.

## Extremal order

Whenever both post-failure distances are finite in an n-vertex simple unweighted graph, each shortest replacement path is simple and has length at most n-1. Hence any finite pairwise response difference is O(n). Together with the construction, the maximum possible order of finite separation under the stated equivalence is Theta(n).

## Sufficiency endpoint

The complete labeled all-pairs distance matrix determines a simple unweighted graph, because uv is an edge exactly when d(u,v)=1. Therefore complete all-pairs distances determine all single-edge replacement responses. This is a sufficiency endpoint, not a novelty claim.
