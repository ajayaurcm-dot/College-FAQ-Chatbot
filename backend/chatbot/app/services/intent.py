from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import Literal


IntentType = Literal[
    "dynamic",
    "static",
    "logical",
    "greeting",
    "clarification",
    "general_category",
    "out_of_domain"
]


class IntentDetector:

    def __init__(self):

        # 🔹 Load BGE model
        self.model = SentenceTransformer("BAAI/bge-base-en")

        # 🔹 Your intent dataset (CODE 1 integrated)
        self.intent_data = {
            "dynamic": [
                "What is the semester fee?",
                "How much is hostel fee?",
                "fees"
                "Exam date",
                "Last date for fee payment",
                "Semester start date",
                "Fee details",
                "When will college reopen?",
                "Important dates",
                "What events are happening now?",
                "Is there any upcoming fest?",
                "What is the mess fee?",
                "Is hostel fee refundable?",
                "What is the tuition fee?",
                
            ],

            "static": [
                "What courses are offered?",
                "companies visiting AURCM for placements"
                "Top Recruiters of AURCM"
                "Syllabus for AI",
                "Curriculum details",
                "What is the credit system?",
                "What are lab subjects?",
                "Is there any hackathon?",
                "What is placement percentage?",
                "What scholarships are available?",
                "Is campus safe?",
                "What is transport facility?",
                "how to apply scholarship",
                "first graduate",
                "transport",
                "safety measurements",
                "hostel infrastructure",
                "hotel warden",
                "college location",
                "hostel food",
                "Location of AURCM",
                "Mails and supportdesk"
               
            ],

            "logical": [

                "addition",
                "subtraction"
               
                
            ],

            "greeting": [
                "hi", "hello", "hey",
                "good morning", "good evening",
                "what's up", "hey chatbot"
            ],

            "clarification": [
                "I don’t understand",
                "Explain clearly",
                "Can you simplify this?",
                "Explain step by step",
                "Give more details",
                "What do you mean?"
            ],
           "link": [
                 "link", "Fee Payment Portal", "Result Portal", "College Website",
                 "Feedback Portal"]

        }

        # 🔹 Build embeddings
        self.intent_embeddings = {}
        self.intent_centroids = {}
        self.intent_names = list(self.intent_data.keys())

        for intent, examples in self.intent_data.items():
            emb = self.model.encode(examples, normalize_embeddings=True)

            self.intent_embeddings[intent] = emb
            self.intent_centroids[intent] = np.mean(emb, axis=0)

    # ----------------------------------------------------
    # 🔥 MAIN DETECTION FUNCTION
    # ----------------------------------------------------
    def detect(self,
               query: str,
               threshold: float = 0.65,
               gap_threshold: float = 0.08) -> IntentType:

        query_emb = self.model.encode(query, normalize_embeddings=True)

        scores = {}

        # 🔹 score each intent
        for intent in self.intent_names:

            max_sim = cosine_similarity(
                [query_emb],
                self.intent_embeddings[intent]
            )[0].max()

            centroid_sim = cosine_similarity(
                [query_emb],
                [self.intent_centroids[intent]]
            )[0][0]

            final_score = 0.7 * max_sim + 0.3 * centroid_sim
            scores[intent] = final_score

        # 🔹 sort intents
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        best_intent, best_score = sorted_scores[0]
        second_intent, second_score = sorted_scores[1]

        # ------------------------------------------------
        # 🚨 RULE 1: OUT OF DOMAIN
        # ------------------------------------------------
        if best_score < threshold:
            return "General category"

        # ------------------------------------------------
        # 🚨 RULE 3: RETURN CLARIFICATION INTENT
        # ------------------------------------------------
        if best_intent == "clarification":
            return "clarification"

        # ------------------------------------------------
        # FINAL
        # ------------------------------------------------
        return best_intent

