import os
import faiss

FAISS_PATH = "app/data/processed/faiss.index"


class VectorDB:
    def __init__(self):
        self.index = None
        self.load_index()

    # ---------------------------
    # Load FAISS index
    # ---------------------------
    def load_index(self):
        if not os.path.exists(FAISS_PATH):
            print("[FAISS ERROR] Index file not found")
            return

        try:
            self.index = faiss.read_index(FAISS_PATH)
            print("✅ FAISS index loaded successfully")
        except Exception as e:
            print(f"[FAISS LOAD ERROR] {e}")
            self.index = None

    # ---------------------------
    # Get index
    # ---------------------------
    def get_index(self):
        return self.index

    # ---------------------------
    # Reload index (if updated)
    # ---------------------------
    def reload(self):
        self.load_index()


# Singleton instance
vector_db = VectorDB()


# Helper function (used in rag.py)
def load_faiss_index():
    return vector_db.get_index()