from collections import deque

def bfs_distances(G, source):
    dist = {v: None for v in G}
    dist[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for v in G[u]:
            if dist[v] is None:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def shortest_path_dag(G, source):
    dist = bfs_distances(G, source)
    arcs = []
    for u, v in G.edges():
        du, dv = dist[u], dist[v]
        if du is None or dv is None:
            continue
        if dv == du + 1:
            arcs.append((u, v))
        elif du == dv + 1:
            arcs.append((v, u))
    return tuple(sorted(arcs)), dist

def shortest_path_counts(G, source):
    arcs, dist = shortest_path_dag(G, source)
    preds = {v: [] for v in G}
    for u, v in arcs:
        preds[v].append(u)
    order = sorted(G, key=lambda v: (dist[v] is None, dist[v] if dist[v] is not None else 10**18, v))
    sigma = {v: 0 for v in G}
    sigma[source] = 1
    for v in order:
        if v == source or dist[v] is None:
            continue
        sigma[v] = sum(sigma[u] for u in preds[v])
    return sigma, arcs, dist

def source_structure(G, source):
    sigma, arcs, dist = shortest_path_counts(G, source)
    return {
        "dist": tuple((v, dist[v]) for v in sorted(G)),
        "spdag": arcs,
        "sigma": tuple((v, sigma[v]) for v in sorted(G)),
    }
