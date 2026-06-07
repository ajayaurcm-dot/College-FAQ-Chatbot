from typing import Dict, Any, List


class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    # ---------------------------
    # Create session
    # ---------------------------
    def create_session(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "data": {},        # 🔹 existing key-value
                "history": []      # 🔥 NEW: conversation memory
            }

    # ---------------------------
    # Set value (existing)
    # ---------------------------
    def set(self, session_id: str, key: str, value: Any):
        self.create_session(session_id)
        self.sessions[session_id]["data"][key] = value

    # ---------------------------
    # Get value (existing)
    # ---------------------------
    def get(self, session_id: str, key: str, default=None):
        return self.sessions.get(session_id, {}).get("data", {}).get(key, default)

    # ---------------------------
    # 🔥 Add message (NEW)
    # ---------------------------
    def add_message(self, session_id: str, role: str, content: str):
        self.create_session(session_id)

        self.sessions[session_id]["history"].append({
            "role": role,
            "content": content
        })

        # 🔥 keep last 6 messages only
        self.sessions[session_id]["history"] = self.sessions[session_id]["history"][-6:]

    # ---------------------------
    # 🔥 Get history (NEW)
    # ---------------------------
    def get_history(self, session_id: str) -> List[Dict]:
        return self.sessions.get(session_id, {}).get("history", [])

    # ---------------------------
    # Clear session
    # ---------------------------
    def clear(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]