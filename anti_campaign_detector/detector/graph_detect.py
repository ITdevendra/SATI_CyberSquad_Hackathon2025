import networkx as nx

def detect_graph_clusters(posts):
    G = nx.Graph()
    for post in posts:
        acc = post["user_id"]
        for tag in post.get("hashtags", []):
            G.add_edge(acc, tag)
    return list(nx.connected_components(G))
