from sentence_transformers import SentenceTransformer, util

def detect_text_similarity(posts, threshold=0.7):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = [p["content"] for p in posts]
    accounts = [p["user_id"] for p in posts]

    embeddings = model.encode(texts, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embeddings, embeddings)

    similar_pairs = []
    for i in range(len(posts)):
        for j in range(i + 1, len(posts)):
            score = cosine_scores[i][j].item()
            if score >= threshold:
                similar_pairs.append({
                    "post_1": accounts[i],
                    "post_2": accounts[j],
                    "similarity": round(score, 2)
                })

    return similar_pairs
