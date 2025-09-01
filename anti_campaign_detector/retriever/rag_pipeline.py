import json
from pathlib import Path

def load_data():
    """Load raw data from https://social-media-gab1.onrender.com/share api."""
    API_URL = "https://social-media-gab1.onrender.com/share"  # External API
    try:
        import requests
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"{len(data)} users fetched from API")
        return data
    except Exception as e:
        print(f"❌ Error fetching API data: {e}")
        data = []

def retrieve(query: str):
    data = load_data()   # data is dict like {"user1": {...}, "user2": {...}}

    results = []
    for user_id, user_info in data.items():
        username = user_info.get("username", "")
        for post in user_info.get("posts", []):
            if (
                query.lower() in username.lower()
                or query.lower() in post.get("content", "").lower()
                or any(query.lower() in h.lower() for h in post.get("hashtags", []))
            ):
                results.append({
                    "user_id": user_id,
                    "username": username,
                    "content": post.get("content", ""),
                    "hashtags": post.get("hashtags", []),
                    "createdAt": post.get("createdAt", "")
                })
    return results


if __name__ == "__main__":
    query = "#Khalistan"
    results = retrieve(query)
    print(f"Retrieved {len(results)} posts for query '{query}':")
    print(json.dumps(results, indent=2))
    print(results)
# API_URL = "https://social-media-gab1.onrender.com/share"  # External API

# def load_data():
#     """
#     Fetch posts from external API.
#     API should return either a list or a dict { "posts": [...] }.
#     """
#     try:
#         response = requests.get(API_URL, timeout=10)
#         response.raise_for_status()
#         data = response.json()

#         # If wrapped in dict
#         if isinstance(data, dict) and "posts" in data:
#             data = data["posts"]

#         normalized = []
#         for p in data:
#             normalized.append({
#                 "account": p.get("account", "unknown"),
#                 "text": p.get("text", ""),
#                 "hashtags": p.get("hashtags", []),
#                 "timestamp": p.get("timestamp", ""),
#             })
#         return normalized
#     except Exception as e:
#         print(f"❌ Error fetching API data: {e}")
#         return []

# def retrieve(query: str):
#     """
#     Simple retriever: filter posts by query in text.
#     Later replace with vector DB + LLM pipeline.
#     """
#     posts = load_data()
#     return [p for p in posts if query.lower() in p["text"].lower()]
