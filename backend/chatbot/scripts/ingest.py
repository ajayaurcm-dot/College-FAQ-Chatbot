import os
import pickle
from typing import List

import faiss
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# ---------------------------
# Config
# ---------------------------
RAW_DATA_PATH = "app/data/raw/"
PROCESSED_PATH = "app/data/processed/"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


# ---------------------------
# Load Documents
# ---------------------------
def load_documents() -> List[str]:
    texts = []

    for file in os.listdir(RAW_DATA_PATH):
        path = os.path.join(RAW_DATA_PATH, file)

        if file.endswith(".pdf"):
            reader = PdfReader(path)
            for page in reader.pages:
                texts.append(page.extract_text())

        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    return texts


# ---------------------------
# Chunking
# ---------------------------
def chunk_text(text: str) -> List[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def process_documents(docs: List[str]) -> List[str]:
    all_chunks = []

    for doc in docs:
        if doc:
            chunks = chunk_text(doc)
            all_chunks.extend(chunks)

    return all_chunks


# ---------------------------
# Embedding + FAISS
# ---------------------------
def build_faiss(chunks: List[str]):
    model = SentenceTransformer("BAAI/bge-base-en")

    print("🔄 Generating embeddings...")
    embeddings = model.encode(chunks, show_progress_bar=True, normalize_embeddings=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # cosine similarity

    index.add(embeddings)

    return index


# ---------------------------
# Save Outputs
# ---------------------------
def save_outputs(index, chunks):
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # Save FAISS index
    faiss.write_index(index, os.path.join(PROCESSED_PATH, "faiss.index"))

    # Save chunks
    with open(os.path.join(PROCESSED_PATH, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)

    print("✅ FAISS index and chunks saved!")


# ---------------------------
# Main Pipeline
# ---------------------------
def run_ingestion():
    print("📥 Loading documents...")
    docs = load_documents()

    print("✂️ Chunking...")
    chunks = process_documents(docs)

    print(f"📊 Total chunks: {len(chunks)}")

    print("🧠 Building FAISS index...")
    index = build_faiss(chunks)

    print("💾 Saving...")
    save_outputs(index, chunks)

    print("🚀 Ingestion completed successfully!")


if __name__ == "__main__":
    run_ingestion()