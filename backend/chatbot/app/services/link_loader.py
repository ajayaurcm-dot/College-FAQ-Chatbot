import os

class LinkLoader:

    def __init__(self):
        self.file_path = os.path.join("app", "data", "links.txt")

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print("LINK LOAD ERROR:", e)
            return ""