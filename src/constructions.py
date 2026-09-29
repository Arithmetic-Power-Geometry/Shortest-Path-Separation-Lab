import networkx as nx

def finite_gap_family(L):
    """
    Degree-preserving finite-gap separation family.

    Common intact structure:
      s--r, with three length-L branches from r ending at t, x, y;
      an independent backup path of length L+1 from s ending at b.

    Hidden same-layer matching:
      G: b--t and x--y
      H: b--x and t--y

    This is a degree-preserving 2-switch. Every labeled vertex has the same
    degree in G and H. All four switched endpoints lie at source distance L+1,
    so the switched edges are absent from the intact source SPDAG and do not
    alter source distances or shortest-path multiplicities.

    After failure e=(s,r):
      d_{G-e}(s,t) = L+2
      d_{H-e}(s,t) = 3L+2
      gap = 2L

    The family has n=4L+3 vertices, hence gap=(n-3)/2=Theta(n).
    """
    if L < 1:
        raise ValueError("L must be at least 1")

    G = nx.Graph()
    H = nx.Graph()
    s, r = "s", "r"

    for X in (G, H):
        X.add_edge(s, r)

        for endpoint in ("t", "x", "y"):
            prev = r
            for i in range(1, L):
                v = f"{endpoint}{i}"
                X.add_edge(prev, v)
                prev = v
            X.add_edge(prev, endpoint)

        prev = s
        for i in range(1, L + 1):
            v = f"b{i}"
            X.add_edge(prev, v)
            prev = v
        X.add_edge(prev, "b")

    # Degree-preserving same-layer 2-switch.
    G.add_edges_from([("b", "t"), ("x", "y")])
    H.add_edges_from([("b", "x"), ("t", "y")])

    return G, H, s, (s, r), "t", {
        "L": L,
        "k": L + 1,
        "theoretical_gap": 2 * L,
        "n_formula": 4 * L + 3,
        "expected_G": L + 2,
        "expected_H": 3 * L + 2,
    }
