from flask import Flask, render_template, jsonify
from retriever.rag_pipeline import retrieve
from detector.frequency import detect_frequent_hashtags, detect_top_accounts
from detector.similarity import detect_text_similarity
from detector.timeburst import detect_time_bursts
from detector.graph_detect import detect_graph_clusters

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect")
def detect():
    query = "No Hindi"
    posts = retrieve(query)

    result = {
        "retrieved_posts": posts,
        "top_hashtags": detect_frequent_hashtags(posts),
        "top_accounts": detect_top_accounts(posts),
        "similar_posts": detect_text_similarity(posts),
        "Frequency":detect_frequent_hashtags(posts),
        "time_bursts": {str(k): v for k, v in detect_time_bursts(posts).items()},
        "graph_clusters": [list(c) for c in detect_graph_clusters(posts)]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
