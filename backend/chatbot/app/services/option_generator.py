from typing import List, Dict
from app.services.dynamic_data import DynamicDataService


class OptionGenerator:
    def __init__(self):
        self.db = DynamicDataService()

    # ---------------------------
    # Get all departments
    # ---------------------------
    def get_departments(self) -> List[str]:
        query = "SELECT DISTINCT department FROM courses"
        result = self.db.execute_query(query)
        return [row["department"] for row in result]

    # ---------------------------
    # Suggest departments
    # ---------------------------
    def suggest_departments(self, query: str) -> List[str]:
        departments = self.get_departments()
        q = query.lower()

        # Basic filtering (can upgrade to embedding later)
        matches = [d for d in departments if d.lower() in q]

        # If no direct match → return all (limit later)
        return matches if matches else departments[:5]

    # ---------------------------
    # Generate options response
    # ---------------------------
    def generate_options(self, query: str, intent: str) -> Dict:
        try:
            # 🎯 Dynamic queries without department
            if intent == "dynamic":
                options = self.suggest_departments(query)
                print("opt gen")

                return {
                    "type": "options",
                    "message": "Please select a department:",
                    "options": options
                }

            # 🎯 Logical queries (optional)
            if intent == "logical":
                return {
                    "type": "options",
                    "message": "What would you like to know?",
                    "options": [
                        "Highest fee",
                        "Lowest fee",
                        "Average fee",
                        "Top courses"
                    ]
                }

            return {
                "type": "none",
                "options": []
            }

        except Exception as e:
            print(f"[OPTION ERROR] {e}")
            return {
                "type": "error",
                "options": []
            }