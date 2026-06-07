import json
import os

class JSONService:

    def __init__(self):
        self.base_path = os.path.join(os.getcwd(), "app", "data")

    def load_json(self, filename):
        path = os.path.join(self.base_path, filename)

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # ---------------------------
    # ADMISSION DATA
    # ---------------------------
    def get_admission_dates(self, level="ug"):
        data = self.load_json("admission_dates.json")
        return data.get(level)

    # ---------------------------
    # COLLEGE TIMING
    # ---------------------------
    def get_timing(self, level="ug"):
        data = self.load_json("college_timing.json")
        return data.get(level)

    # ---------------------------
    # FEES
    # ---------------------------
    def get_fee(self, level, dept):
        data = self.load_json("fees.json")
        return data.get(level, {}).get(dept)

    # ---------------------------
    # EVENTS
    # ---------------------------
    def get_events(self, level="ug"):
        data = self.load_json("events.json")
        return data.get(level, [])