from typing import List, Dict
from sentence_transformers import CrossEncoder


class RerankerService:
    def __init__(self):
        self.model = CrossEncoder("BAAI/bge-reranker-base")

    # ---------------------------
    # Extract text safely
    # ---------------------------
    def extract_text(self, doc):
        txt = doc.get("text", "")

        # Old chunk = string
        if isinstance(txt, str):
            return txt

        # New chunk = dict
        elif isinstance(txt, dict):
            topic = txt.get("topic", "")
            content = txt.get("content", "")
            return f"{topic}\n{content}"

        return ""

    # ---------------------------
    # Rerank docs
    # ---------------------------
    def rerank(self, query: str, documents: List[Dict], top_k: int = 3):

        if not documents:
            return []

        try:
            pairs = [(query, self.extract_text(doc)) for doc in documents]

            scores = self.model.predict(pairs)

            for doc, score in zip(documents, scores):
                doc["rerank_score"] = float(score)

            ranked = sorted(
                documents,
                key=lambda x: x["rerank_score"],
                reverse=True
            )

            return ranked[:top_k]

        except Exception as e:
            print("[RERANK ERROR]", e)
            return documents[:top_k]

    # ---------------------------
    # Build context
    # ---------------------------
    def build_context(self, query, documents, top_k=3):

        ranked = self.rerank(query, documents, top_k)

        context = "\n\n".join(
            [self.extract_text(doc) for doc in ranked]
        )

        return context