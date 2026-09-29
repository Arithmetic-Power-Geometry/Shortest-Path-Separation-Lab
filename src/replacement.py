from collections import deque

def distance_without_edge(G, source, target, failed_edge):
    a, b = failed_edge
    dist = {v: None for v in G}
    dist[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for v in G[u]:
            if (u == a and v == b) or (u == b and v == a):
                continue
            if dist[v] is None:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist[target]

def replacement_profile(G, source):
    out = {}
    for e in sorted(tuple(sorted(e)) for e in G.edges()):
        for t in sorted(G):
            out[(e, t)] = distance_without_edge(G, source, t, e)
    return out
