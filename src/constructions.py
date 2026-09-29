import networkx as nx

def path_with_detour_pair(k):
    """
    Candidate finite-gap family.

    Core path: 0-1-...-k, source=0, target=k.
    Both graphs have the same core shortest-path structure.
    Each receives the same number of extra vertices and edges, arranged
    so all added routes are longer than the original source shortest paths.

    The present construction is deliberately transparent and is verified
    by the strict checker before it is treated as a witness.
    """
    if k < 5:
        raise ValueError("k must be at least 5")

    G = nx.Graph()
    H = nx.Graph()
    core = list(range(k + 1))
    for X in (G, H):
        X.add_nodes_from(core)
        X.add_edges_from((i, i + 1) for i in range(k))

    # Same labeled auxiliary vertices in both graphs.
    aux = list(range(k + 1, 2 * k + 3))
    G.add_nodes_from(aux)
    H.add_nodes_from(aux)

    # Failed edge lies near the middle.
    j = k // 2
    failed = (j, j + 1)

    # G: a relatively short dormant bypass.
    # H: same number of auxiliary edges, but arranged as a longer bypass.
    # Both are checked to ensure they do not alter the original source structure.
    left, right = j, j + 1

    g_chain = aux[:4]
    G.add_edges_from([
        (left, g_chain[0]), (g_chain[0], g_chain[1]),
        (g_chain[1], g_chain[2]), (g_chain[2], g_chain[3]),
        (g_chain[3], right),
    ])

    # Remaining auxiliary vertices are attached identically as long leaves
    # so |V| and |E| stay matched without entering the source SPDAG.
    rem_g = aux[4:]
    for idx, v in enumerate(rem_g):
        anchor = max(0, left - 2)
        if idx == 0:
            G.add_edge(anchor, v)
        else:
            G.add_edge(rem_g[idx-1], v)

    h_chain = aux
    H.add_edge(left, h_chain[0])
    for a, b in zip(h_chain, h_chain[1:]):
        H.add_edge(a, b)
    H.add_edge(h_chain[-1], right)

    # Equalize edge count by adding G-side edges among auxiliary vertices only
    # if needed. The verifier still rejects the construction if any such edge
    # changes the source-shortest-path observable.
    next_pairs = [(aux[i], aux[i+2]) for i in range(max(0, len(aux)-2))]
    p = 0
    while G.number_of_edges() < H.number_of_edges() and p < len(next_pairs):
        G.add_edge(*next_pairs[p])
        p += 1

    return G, H, 0, failed, k
