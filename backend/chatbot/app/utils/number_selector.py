import re


class NumberSelector:

    def handle(self, query: str, history: list):
        """
        Handles numeric input like:
        User: 2 → selects item 2 from last list
        """

        # 🔹 Step 1: Check if input is a number
        if not query.strip().isdigit():
            return None

        number = int(query.strip())

        if not history:
            return {"error": "No previous list found."}

        # 🔥 Step 2: Find MOST RECENT list in history
        latest_list_msg = None

        for msg in reversed(history):
            if msg["role"] == "assistant":
                if self._has_list(msg["content"]):
                    latest_list_msg = msg["content"]
                    break  # ✅ stop at most recent list

        if not latest_list_msg:
            return {
                "error": "Could you please clarify your request which help me give you the exact information."
            }

        print("\n📄 Latest List Message:\n", latest_list_msg)

        # 🔥 Step 3: Parse list line-by-line (STRICT PARSING)
        items = {}

        lines = latest_list_msg.split("\n")

        for line in lines:
            line = line.strip()

            match = re.match(r'^(\d+)\.\s+(.+)', line)

            if match:
                num = int(match.group(1))
                text = match.group(2).strip()
                items[num] = text

        print("\n📌 Parsed Items:", items)

        # ❌ No valid list found
        if not items:
            return {
                "error": "Could you please clarify your request which help me give you the exact information."
            }

        # ❌ Invalid selection
        if number not in items:
            return {
                "error": "Could you please clarify your request which help me give you the exact informationc." 
            }

        # 🔹 Step 4: Get selected line
        selected_line = items[number]

        print("\n👉 Selected Line:", selected_line)

        # 🔥 Step 5: Build meaningful query
        final_query = f"{selected_line}"

        

        print("\n🚀 Final Query:", final_query)

        return {
            "success": True,
            "query": final_query
        }

    # 🔹 Helper: detect if text contains numbered list
    def _has_list(self, text: str):
        return bool(re.search(r'\d+\.\s+', text))