import networkx as nx

def finite_gap_family(L):
    """
    Explicit unweighted finite-gap separation family.

    Common visible source structure:
      s -- r, with two length-L branches from r ending at t and x;
      an independent backup path of length k=L+1 from s ending at b.

    G adds the same-level edge b--t.
    H adds the same-level edge b--x.

    Since b,t,x all have source distance k in the intact graph, the differing
    edge is non-tight and absent from the source shortest-path DAG in both
    graphs. Thus the source-distance vector, SPDAG, shortest-path counts,
    |V|, and |E| coincide.

    After failure of e=(s,r):
      d_{G-e}(s,t) = k + 1
      d_{H-e}(s,t) = k + 1 + 2L

    Hence the finite gap is 2L. The number of vertices is n=3L+3, so
    gap = 2(n-3)/3 = Theta(n).
    """
    if L < 1:
        raise ValueError("L must be at least 1")

    G = nx.Graph()
    H = nx.Graph()

    s = "s"
    r = "r"
    t = "t"
    x = "x"
    k = L + 1

    for X in (G, H):
        X.add_edge(s, r)

        # branch r -> ... -> t of length L
        prev = r
        for i in range(1, L):
            v = f"t{i}"
            X.add_edge(prev, v)
            prev = v
        X.add_edge(prev, t)

        # branch r -> ... -> x of length L
        prev = r
        for i in range(1, L):
            v = f"x{i}"
            X.add_edge(prev, v)
            prev = v
        X.add_edge(prev, x)

        # independent backup path s -> ... -> b of length k=L+1
        prev = s
        for i in range(1, k):
            v = f"b{i}"
            X.add_edge(prev, v)
            prev = v
        b = "b"
        X.add_edge(prev, b)

    G.add_edge("b", t)
    H.add_edge("b", x)

    failed_edge = (s, r)
    return G, H, s, failed_edge, t, {
        "L": L,
        "k": k,
        "theoretical_gap": 2 * L,
        "n_formula": 3 * L + 3,
    }
