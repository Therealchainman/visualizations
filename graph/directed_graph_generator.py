import networkx as nx
from pyvis.network import Network
from itertools import combinations
import numpy as np

options_str = """
var options = {
  "physics": {
    "barnesHut": {
      "theta": 0.95,
      "gravitationalConstant": -385161,
      "centralGravity": 0,
      "springLength": 635,
      "damping": 0.81
    },
    "minVelocity": 0.75
  }
}
"""

N = 5
nodes = list(range(N))
edges = []
for u in range(N):
    for v in range(u):
        edges.append((u, v))
cnt = 0
def search(src):
    stk = [src]
    while stk:
        u = stk.pop()
        reachable[src][u] = 1
        for v in adj[u]:
            stk.append(v)
def check(i, j, k):
    return reachable[j][i] or reachable[k][i] or reachable[k][j]
def is_valid():
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if not check(i, j, k): return False
    return True
for len_ in range(2, len(edges) + 1):
    for edge_set in combinations(range(len(edges)), len_):
        cur_edges = [edges[j] for j in edge_set]
        adj = [[] for _ in range(N)]
        for u, v in cur_edges:
            adj[u].append(v)
        reachable = [[0] * N for _ in range(N)]
        for i in range(N):
            search(i)
        if not is_valid(): continue
        reach = np.array(reachable)
        np.save(f"vis_matrices/reach_{str(cnt).zfill(4)}.npy", reach)
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(cur_edges)
        net = Network(directed = True)
        net.from_nx(G)
        # Add labels to the nodes
        for node in net.nodes:
            node["size"] = 30
            node["font"] = {"size": 50}
            node["label"] = str(node["label"])
        net.set_options(options_str)
        # net.show_buttons(filter_ = ["physics"])
        net.write_html(f"vis_htmls/graph_{str(cnt).zfill(4)}.html")
        if cnt % 100 == 0: print(cnt)
        cnt += 1
print(cnt)