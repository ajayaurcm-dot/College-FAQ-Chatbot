import re

class ListParser:

    def parse(self, text: str):
        lines = text.split("\n")

        options = []

        for line in lines:
            line = line.strip()

            # ✅ Detect numbered list (1) or 1. or 1)
            match = re.match(r"^\d+[\).\-\s]+(.+)", line)

            if match:
                item = match.group(1).strip()
                options.append({
                    "label": item,
                    "value": item
                })
                continue

            # ✅ Detect bullet list
            if line.startswith("- ") or line.startswith("• "):
                item = line[2:].strip()
                options.append({
                    "label": item,
                    "value": item
                })

        # 🚨 STRICT CONDITION
        if len(options) >= 2:
            return {
                "answer": text.split("\n")[0],  # first line as title
                "options": options
            }

        return None