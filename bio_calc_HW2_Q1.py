"""
Dependencies:
    pip install networkx
    Python ≥ 3.8
"""
import networkx as nx
def all_connected_motifs(n: int):
    """Return a list of edge-lists, one per non-isomorphic connected digraph."""
    V = list(range(1, n + 1))
    all_edges = [(u, v) for u in V for v in V if u != v]      # make full graph
    motifs = []        # list[set[(u,v)] ] – one representative per isomorphism class

    for mask in range(1, 1 << len(all_edges)):                # check all subgraph
        edges = [all_edges[i] for i in range(len(all_edges)) if mask & (1 << i)] # get subgraph
        G = nx.DiGraph()
        G.add_nodes_from(V)
        G.add_edges_from(edges)

        if not nx.is_weakly_connected(G):                     # ensure “connected”
            continue

        # Check isomorphism against representatives already kept
        iso_found = False
        for rep_edges in motifs:
            R = nx.DiGraph()
            R.add_nodes_from(V)
            R.add_edges_from(rep_edges)
            if nx.algorithms.isomorphism.DiGraphMatcher(G, R).is_isomorphic():
                iso_found = True
                break

        if not iso_found:
            motifs.append(frozenset(edges))                    # store canonical rep

    return motifs

def write_output(motifs, n):
    name = f"motifs_n={n}.txt"
    with open(name, "w", encoding="utf-8") as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(motifs)}\n\n")
        for k, edges in enumerate(motifs, start=1):
            f.write(f"#{k}\n")
            for u, v in sorted(edges):
                f.write(f"{u} {v}\n")
            f.write("\n")
    print(f"Wrote {len(motifs)} motifs to {name}")

def q1(n):
    motifs = all_connected_motifs(n)
    write_output(motifs, n)

if __name__ == "__main__":
    n=3
    q1(n)
