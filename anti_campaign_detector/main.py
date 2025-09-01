from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from retriever.rag_pipeline import retrieve
from detector.frequency import detect_frequent_hashtags, detect_top_accounts
from detector.similarity import detect_text_similarity
from detector.spread_analysis import score_spreaders
from detector.timeburst import detect_time_bursts
from detector.graph_detect import detect_graph_clusters

app = FastAPI()

# Allow React frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/detect")
def detect_campaign(query: str = "#khalistan"):
    posts = retrieve(query)
    # print(posts)
    return {
        "retrievedPosts": posts,
        "topHashtags": detect_frequent_hashtags(posts),
        "topAccounts": detect_top_accounts(posts),
        "similarPosts": detect_text_similarity(posts),
        "timeBursts": detect_time_bursts(posts),
        "graphClusters": detect_graph_clusters(posts),
        "topSpreaders": score_spreaders(posts),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
