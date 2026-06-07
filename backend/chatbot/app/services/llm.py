from groq import Groq
from app.config import settings


class LLMService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)

        # ✅ Use supported model
        self.model = settings.LLM_MODEL

    def generate(self, query: str, context: str = "", history=None) -> str:
        try:
            messages = []

             # 1️⃣  System prompt
            messages.append({
                "role": "system",
                "content": self._system_prompt()
            })

            # 2️⃣ History (VERY IMPORTANT FIX)
            history_text = ""
            if history:
                last_msgs = history[-6:]  # 🔥 only last 6 messages

                for msg in last_msgs:
                    role = "User" if msg["role"] == "user" else "Assistant"
                    history_text += f"{role}: {msg['content']}\n"

              # 3️⃣ Current query with context
            messages.append({
                "role": "user",
                "content": f"""
                You are answering a college-related question.

                Conversation Context:
               - Use previous messages to understand references like "this course", "that", "it"
                
                Conversation History:
                {history_text}

                Knowledge Base:
               {context}

               Current Question:
              {query}

              Instructions:
               - Resolve references like "this course", "that", "it" using Conversation History.
               - If user previously mentioned a course (e.g., "cse"), then "this course" = that course.
               - DO NOT mention "conversation history" in the answer
               - DO NOT explain how you got the answer
               - Do NOT ask the user again if the answer can be inferred from history.
               - Answer ONLY using the Knowledge Base.
               - If still unclear, ask a short clarification.
               - Keep the answer concise.
               """
              })

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=512
            )

            content = response.choices[0].message.content
            print("\nLLM RAW OUTPUT:\n", content)

            return content.strip()

        except Exception as e:
            print(f"[LLM ERROR] {e}")
            return "I'm having trouble generating a response right now."

    def _system_prompt(self) -> str:
        return (
            
                "You are a professional college(Anna University Regional Campus Madurai) assistant chatbot.\n\n"

                "Your job:\n"
                "- Answer student questions about the college\n"
                "- Use conversation history to understand references\n\n"
                "if any question related to anna university regional campus come you our database doesn't have that data you can explain it if you know it"
                "Rules:\n"
                "Answer Greetings only in English"
                "for list based answers should be listed with numbers"
                "dont list any points with - instead use *"
                "for list based answers should be listed with numbers if its retrived from college_data.txt file"
                "- If answer not found and its related to college answer it as general\n"
                "if question is not about college answer it maturly"
                "- If user says 'this course', use previous messages\n"
                "- If query is unclear → ask a clarification question\n"
                "- Keep answers short, clear, and professional\n"
                " If context contains links:"
                "Answer shortly"
                "Mention purpose"
                "if multiple words come in single line like this(income,adhaar,nativity,birth certificate) list then with numbers and word by word in new line"
                "Always include full URL"
                "dont generate any words or line after link "
                " Return plain text only"
    )
       

        

    def _build_prompt(self, query: str, context: str) -> str:
        return f"""
       Context:
{context}

Question:
{query}

Answer:
"""