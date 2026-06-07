import os
import pickle
import numpy as np
from typing import List, Dict
from sentence_transformers import SentenceTransformer

from app.db.vector_db import load_faiss_index


class RAGService:
    def __init__(self):
        # Load embedding model
        self.model = SentenceTransformer("BAAI/bge-base-en")

        # Load FAISS index
        self.index = load_faiss_index()

        # Load metadata (text chunks)
        self.texts = self._load_text_chunks()

    # ---------------------------
    # Load text chunks
    # ---------------------------
    def _load_text_chunks(self) -> List[str]:
        path = "app/data/processed/chunks.pkl"

        if not os.path.exists(path):
            print("[RAG ERROR] chunks.pkl not found")
            return []

        with open(path, "rb") as f:
            return pickle.load(f)

    # ---------------------------
    # Embed query
    # ---------------------------
    def embed_query(self, query: str) -> np.ndarray:
        return self.model.encode([query], normalize_embeddings=True)

    # ---------------------------
    # Retrieve top-k relevant chunks
    # ---------------------------
    def retrieve(self, query: str, k: int = 5) -> List[Dict]:
        if self.index is None or not self.texts:
            return []

        try:
            query_vector = self.embed_query(query)

            distances, indices = self.index.search(query_vector, k)

            results = []
            for i, idx in enumerate(indices[0]):
                if idx < len(self.texts):
                    results.append({
                        "text": self.texts[idx],
                        "score": float(distances[0][i])
                    })

            
            return results

        except Exception as e:
            print(f"[RAG ERROR] {e}")
            return []

    # ---------------------------
    # Build context for LLM
    # ---------------------------
    def build_context(self, query: str, k: int = 5) -> str:
        results = self.retrieve(query, k)

        if not results:
            return ""

        context = "\n\n".join([r["text"] for r in results])
        print(context)
        return context