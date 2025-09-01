import os

folders = ["retriever", "detector", "data", "utils"]

for f in folders:
    os.makedirs(f, exist_ok=True)
    print(f"Folder '{f}' created")
