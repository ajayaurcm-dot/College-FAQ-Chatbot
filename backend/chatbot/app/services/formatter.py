class ResponseFormatter:

    def base(self, answer, options=None, source="system", status="success", data=None):
        return {
            "status": status,
            "answer": answer,
            "options": options or [],
            "source": source,
            "data": data or {}
        }

    # 👋 Greeting
    def greeting(self):
        return self.base(
            answer="Hello! How can I help you today?",
            source="system"
        )

    # 🔵 Dynamic (DB)
    def format_dynamic(self, data, query):
        if not data:
            return self.fallback()
            print("form workinng")

        answer = f"The fee for {data.get('department')} is ₹{data.get('fee')}."

        return self.base(
            answer=answer,
            source="db",
            data=data
        )

    # 🧠 Logical
    def format_logical(self, data):
        if not data:
            return self.fallback()

        return self.base(
            answer=str(data),
            source="logic"
        )

    # 🟢 RAG
    def format_rag(self, answer, context):
        return self.base(
            answer=answer,
            source="rag",
            data={"context": context}
        )

    # ⚠️ Fallback
    def fallback(self, message="Sorry, I couldn't understand your query."):
        return self.base(
            answer=message,
            source="system",
            status="error"
        )

    # ❌ Error
    def error(self, message):
        return self.base(
            answer=message,
            source="system",
            status="error"
        )
    def format_options(self, answer, options):
        return {
            "status": "success",
            "answer": answer,
            "options": options,
            "source": "system"
         }

    # 🤖 LLM Wrapper (VERY IMPORTANT 🔥)
    def format_llm(self, llm_response):
        """
        Ensures LLM output is always structured
        """
        if isinstance(llm_response, dict):
            return self.base(
                answer=llm_response.get("answer", ""),
                options=llm_response.get("options", []),
                source="llm"
            )

        # If LLM returns plain string
        return self.base(
            answer=str(llm_response),
            source="llm"
        )
    def format_ui(self, answer, confidence="high", used_llm=True, options=None):
         return {
            "answer": answer,
            "confidence": confidence,
            "used_llm": used_llm,
           
    }
    