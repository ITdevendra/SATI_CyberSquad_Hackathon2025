from similarity import detect_text_similarity

# Sample data
posts = [
    {"account": "user001", "text": "No Hindi in Maharashtra!"},
    {"account": "user002", "text": "Say no to Hindi in Maharashtra!"},
    {"account": "user003", "text": "Boycott Bollywood movies!"},
    {"account": "user004", "text": "Reject Hindi language imposition."}
]

results = detect_text_similarity(posts, threshold=0.5)

print("Similar Post Pairs:")
for pair in results:
    print(pair)
