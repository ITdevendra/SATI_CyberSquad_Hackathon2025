from collections import Counter

def detect_frequent_hashtags(posts):
    hashtags = []
    for post in posts:
        hashtags.extend(post.get("hashtags", []))
    return Counter(hashtags).most_common(5)

def detect_top_accounts(posts, top_n=5):
    """
    Detect top accounts by number of posts.
    
    Args:
        posts (list): List of post dicts with 'user_id' and 'username'.
        top_n (int): Number of top accounts to return.

    Returns:
        list of dict: Top accounts with user_id, username, and count.
    """
    account_counter = Counter()

    # Count posts per user_id
    for post in posts:
        account_counter[(post["user_id"], post["username"])] += 1

    # Get top N
    top_accounts = []
    for (user_id, username), count in account_counter.most_common(top_n):
        top_accounts.append({
            "user_id": user_id,
            "username": username,
            "post_count": count
        })

    return top_accounts

