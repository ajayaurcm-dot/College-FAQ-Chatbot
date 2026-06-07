import os

class DataLoader:

    def __init__(self):
        self.file_path = os.path.join("app", "data", "college_data.txt")

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print("❌ DATA LOAD ERROR:", e)
            return ""