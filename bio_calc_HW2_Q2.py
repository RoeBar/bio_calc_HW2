"""
Dependencies:
    pip install networkx
    Python ≥ 3.8
"""
import itertools
import networkx as nx

def all_connected_motifs(n: int):
    """Return one canonical representative (edge-set) per connected digraph
    of size n, up to isomorphism.  Vertices are always numbered 1…n."""
    V = list(range(1, n + 1))
    all_edges = [(u, v) for u in V for v in V if u != v]
    motifs = []                        # list[frozenset[(u,v)]]

    for mask in range(1, 2 << (len(all_edges) - 1)):
        edges = [all_edges[i] for i in range(len(all_edges)) if mask & (1 << i)]
        G = nx.DiGraph()
        G.add_nodes_from(V)
        G.add_edges_from(edges)
        if not nx.is_weakly_connected(G):
            continue

        # keep only one rep per isomorphism class
        if not any(nx.is_isomorphic(G, rep) for rep in
                   (nx.DiGraph(list(rep_edges)) for rep_edges in motifs)):
            motifs.append(frozenset(edges))

    return motifs

def count_motifs_in_graph(G: nx.DiGraph, motifs, n):
    """Return a list[int] where counts[i] is how many times motifs[i] occurs."""
    # Pre-build graph objects for the motif representatives once
    motif_graphs = []
    for edges in motifs:
        H = nx.DiGraph()
        H.add_nodes_from(range(1, n + 1))
        H.add_edges_from(edges)
        motif_graphs.append(H)

    counts = [0] * len(motifs)

    # Enumerate every induced n-vertex subgraph of G
    for S in itertools.combinations(G.nodes, n):
        H = G.subgraph(S).copy()
        if not nx.is_weakly_connected(H):
            continue

        # Relabel its vertices to 1…n so we can reuse the motif reps
        relabel_map = {old: i + 1 for i, old in enumerate(S)}
        H = nx.relabel_nodes(H, relabel_map, copy=True)

        # Find which motif it matches
        for idx, M in enumerate(motif_graphs):
            if nx.is_isomorphic(H, M):
                counts[idx] += 1
                break

    return counts

def read_graph(file):
    """Return a DiGraph read from a file-like object with 'u v' per line."""
    G = nx.DiGraph()
    for line in file:
        if not line.strip():
            continue
        u, v = map(int, line.split())
        G.add_edge(u, v)
    return G

def write_output_q2(motifs, counts, n):
    """Write motifs plus their occurrence counts in the required format."""
    out_name = f"motifs_instances_n={n}.txt"
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(motifs)}\n\n")
        for k, (edges, c) in enumerate(zip(motifs, counts), start=1):
            f.write(f"#{k}\n")
            f.write(f"count={c}\n")
            for u, v in sorted(edges):
                f.write(f"{u} {v}\n")
            f.write("\n")
    print(f"Wrote results to {out_name}")

def q2(n:int,file_name:str):
    # Read the input graph
    with open(file_name, encoding="utf-8") as f:
        G = read_graph(f)
    # Step 1 – generate motif dictionary (re-use Q 1)
    motifs = all_connected_motifs(n)
    # Step 2 – count occurrences in G
    counts = count_motifs_in_graph(G, motifs, n)
    # Step 3 – dump to file
    write_output_q2(motifs, counts, n)

if __name__ == "__main__":
    n=2
    file_name="input_graph.txt"
    q2(2,file_name)
