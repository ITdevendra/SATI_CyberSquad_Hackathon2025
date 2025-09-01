import pandas as pd

def detect_time_bursts(posts, interval="1h"):
    df = pd.DataFrame(posts)

    # Defensive check: normalize timestamp column
    if "createdAt" not in df.columns:
        raise KeyError("Missing 'createdAt' column in input data")

    # Convert to datetime safely
    df["timestamp"] = pd.to_datetime(df["createdAt"], errors="coerce")

    # Drop rows with invalid timestamps
    df = df.dropna(subset=["timestamp"])

    # Group by time interval
    counts = df.groupby(pd.Grouper(key="timestamp", freq=interval)).size()

    return counts.to_dict()
