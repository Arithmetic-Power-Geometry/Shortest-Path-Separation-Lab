# Intact-observable separation

## Observable equivalence

For connected simple unweighted graphs on a common labeled vertex set with source (s), define

```text
S+(G,s) = (d_s, SPDAG_s, sigma_s, deg_G).
```

Equality of this observable means:

- identical complete source-distance vectors,
- identical full source shortest-path DAGs,
- identical source shortest-path multiplicities for every labeled vertex, and
- identical labeled degree vectors.

## Degree-preserving construction

For (L \ge 1), use a common edge (s-r), three length-(L) branches from (r) ending at (t,x,y), and an independent length-((L+1)) path from (s) ending at (b).

The two graphs differ only through a same-layer degree-preserving 2-switch:

```text
G: {b-t, x-y}
H: {b-x, t-y}.
```

Because (b,t,x,y) all lie at source distance (L+1), the switched edges are non-tight and absent from the intact source shortest-path DAG. The switch preserves every labeled vertex degree and leaves both (d_s) and `sigma_s` unchanged.

For the common failed edge (e=(s,r)) and target (t),

```text
n = 4L + 3
d_{G-e}(s,t) = L + 2
d_{H-e}(s,t) = 3L + 2
gap = 2L = (n - 3)/2.
```

Thus the family gives a finite linear separation while preserving the intact observable exactly.

## Extremal finite ambiguity

Let `Delta_n` denote the maximum finite replacement-response gap over (n)-vertex graph pairs that are equivalent under the intact observable, for a common source, target, and failed edge.

For arbitrary (n \ge 7), write

```text
n = 4L + 3 + k,
L = floor((n - 3)/4),
k in {0,1,2,3}.
```

Adding the same (k) pendant leaves to (s) in both graphs preserves the intact observable and the replacement distances. Therefore

```text
Delta_n >= (n - 6)/2.
```

Whenever both post-failure distances are finite in an (n)-vertex simple unweighted graph, each replacement path is simple and has length at most (n-1). Hence

```text
Delta_n <= n - 2.
```

Therefore

```text
Delta_n = Theta(n).
```

## Sufficiency endpoint

The complete labeled all-pairs distance matrix determines a simple unweighted graph because (uv) is an edge exactly when (d(u,v)=1). Consequently, full labeled all-pairs distances determine all single-edge replacement responses.

This observation is used as a sufficiency endpoint and is not presented as a novelty claim.
