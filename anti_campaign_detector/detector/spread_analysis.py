import networkx as nx
from detector.similarity import detect_text_similarity
from detector.timeburst import detect_time_bursts
from collections import Counter
import pandas as pd

def find_seeds(posts, top_n=5):
    sorted_posts = sorted(posts, key=lambda x: x["createdAt"])
    return [p["user_id"] for p in sorted_posts[:top_n]]

def find_amplifiers(posts, interval="30min"):
    df = pd.DataFrame(posts)
    df["timestamp"] = pd.to_datetime(df["createdAt"])
    burst_counts = df.groupby(pd.Grouper(key="timestamp", freq=interval)).size()
    burst_windows = burst_counts[burst_counts > burst_counts.mean()].index

    amplifiers = []
    for post in posts:
        ts = pd.to_datetime(post["createdAt"])
        if any(abs((ts - bw).total_seconds()) < 1800 for bw in burst_windows):
            amplifiers.append(post["user_id"])
    return list(set(amplifiers))

def find_influencers(posts):
    G = nx.Graph()
    for post in posts:
        acc = post["user_id"]
        for tag in post.get("hashtags", []):
            G.add_edge(acc, tag)
    centrality = nx.degree_centrality(G)
    return dict(sorted(centrality.items(), key=lambda x: x[1], reverse=True))

def cluster_similar_accounts(posts, threshold=0.7):
    pairs = detect_text_similarity(posts, threshold)
    clusters = {}
    for pair in pairs:
        clusters.setdefault(pair["post_1"], []).append(pair["post_2"])
    return clusters

def score_spreaders(posts):
    seeds = find_seeds(posts)
    amplifiers = find_amplifiers(posts)
    centrality = find_influencers(posts)
    similarity_clusters = cluster_similar_accounts(posts)

    all_accounts = set(p["user_id"] for p in posts)
    scores = {}

    for acc in all_accounts:
        is_seed = 1 if acc in seeds else 0
        is_amplifier = 1 if acc in amplifiers else 0
        graph_score = centrality.get(acc, 0)
        similarity_cluster_size = len(similarity_clusters.get(acc, []))

        score = (
            2 * is_seed +
            2 * is_amplifier +
            3 * graph_score +
            1 * similarity_cluster_size
        )
        scores[acc] = round(score, 2)

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
