# save as build_faiss.py
# run: python build_faiss.py
# Output:
#   faiss.index
#   metadata.pkl

import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# ==================================================
# FILE PATHS
# ==================================================
CHUNK_FILE = "chunks.pkl"
INDEX_FILE = "faiss.index"
META_FILE = "metadata.pkl"

# ==================================================
# LOAD CLEAN CHUNKS
# ==================================================
with open(CHUNK_FILE, "rb") as f:
    chunks = pickle.load(f)

# ==================================================
# REMOVE GARBAGE / EMPTY / DUPLICATES
# ==================================================
clean_chunks = []
seen = set()

for item in chunks:

    topic = item["topic"].strip()
    text = item["content"].strip()

    # skip empty
    if not text:
        continue

    # skip very small junk
    if len(text) < 20:
        continue

    # remove duplicates
    key = text.lower()
    if key in seen:
        continue

    seen.add(key)

    clean_chunks.append({
        "topic": topic,
        "content": text
    })

print("Clean Chunks:", len(clean_chunks))


# ==================================================
# LOAD EMBEDDING MODEL
# ==================================================
model = SentenceTransformer("BAAI/bge-base-en-v1.5")


# ==================================================
# EMBEDDINGS
# ==================================================
texts = [x["content"] for x in clean_chunks]

embeddings = model.encode(
    texts,
    normalize_embeddings=True,
    show_progress_bar=True
)

embeddings = np.array(embeddings).astype("float32")


# ==================================================
# BUILD FAISS INDEX (COSINE via INNER PRODUCT)
# ==================================================
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

print("Vectors Added:", index.ntotal)


# ==================================================
# SAVE FILES
# ==================================================
faiss.write_index(index, INDEX_FILE)

with open(META_FILE, "wb") as f:
    pickle.dump(clean_chunks, f)

print("faiss.index created successfully")
print("metadata.pkl created successfully")