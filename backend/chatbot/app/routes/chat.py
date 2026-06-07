from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.json_service import JSONService
from app.services.category_detector import CategoryDetector
from app.services.intent import IntentDetector
from app.services.dynamic_data import DynamicDataService
from app.services.logic_engine import LogicEngine
from app.services.rag import RAGService
from app.services.reranker import RerankerService
from app.services.llm import LLMService
from app.services.formatter import ResponseFormatter
from app.services.option_generator import OptionGenerator
from app.utils.spell import SpellCorrector
from app.utils.session import SessionManager
from app.services.data_loader import DataLoader
from app.services.list_parser import ListParser
from app.utils.number_selector import NumberSelector
from app.services.link_loader import LinkLoader

router = APIRouter()

# ---------------------------
# Initialize services
# ---------------------------
intent_detector = IntentDetector()
link_loader = LinkLoader()
selector = NumberSelector()
parser = ListParser()
detector = CategoryDetector()
data_loader = DataLoader()
json_service = JSONService()
db_service = DynamicDataService()
logic_engine = LogicEngine()
rag_service = RAGService()
reranker = RerankerService()
llm = LLMService()
formatter = ResponseFormatter()
option_gen = OptionGenerator()
spell = SpellCorrector()
session = SessionManager()



# ---------------------------
# Chat Endpoint
# ---------------------------
@router.post("/chat")
def chat(request: ChatRequest):
    
    session_id = request.session_id or "default"

    try: 


        query = request.query
        history = session.get_history(session_id)

        # 🔥 STEP 0: Number selection logic
        selection = selector.handle(query, history)

        if selection:
            if "error" in selection:
                return formatter.fallback(selection["error"])

    # 🔥 Replace query with selected item
            corrected_query = selection["query"]
            print("🔢 Number detected → New Query:", corrected_query)
            print("Corrected Query:", corrected_query)

        else:
            corrected_query = spell.correct(query)
        
        
        

        # 🎯 Step 2: Intent detection
        intent = intent_detector.detect(corrected_query)
        print("🧠 Intent:", intent)
        

        # ---------------------------
        # 🚫 Out of domain
        # ---------------------------
        if intent == "out_of_domain":
            return formatter.fallback(
                message="I can only answer college-related queries."
            )


        # ---------------------------
        # 🔗 Link Intent
        # ---------------------------
        if intent == "link":
            print("🔗 Routing to Links File")

            context = link_loader.load()

            if not context:
                return formatter.fallback("Links not available")

            answer = llm.generate(
            query=corrected_query,
            context=context,
            history=history
            )
            print("Answer",answer)

            session.add_message(session_id, "user", corrected_query)
            session.add_message(session_id, "assistant", answer)

            return formatter.format_llm(answer)
        # ---------------------------
        # 🔗 Link Intent
        # ---------------------------
        if intent == "link":
            print("🔗 Routing to Links File")

            context = link_loader.load()

            if not context:
                return formatter.fallback("Links not available")

            answer = llm.generate(
                query=corrected_query,
                context=context,
                history=history
            )

            session.add_message(session_id, "user", corrected_query)
            session.add_message(session_id, "assistant", answer)

            return formatter.format_llm(answer)

        # ---------------------------
        # 👋 Greeting
        # ---------------------------
        if intent == "greeting":
             llm_output = llm.generate(corrected_query, context=None)
             session.add_message(session_id, "user", corrected_query)
             session.add_message(session_id, "assistant", llm_output)
             result = formatter.format_llm(llm_output)
             print("FINAL API RESPONSE:", result)
             return result

        # ---------------------------
        # 🟡 Clarification / General / Logical fallback to LLM
        # ---------------------------
        if intent in ["clarification", "general_category", "logical"]:
            llm_output = llm.generate(corrected_query, context=None,history=history)
            session.add_message(session_id, "user", corrected_query)
            session.add_message(session_id, "assistant", llm_output)
            return formatter.format_llm(llm_output)
        # ---------------------------
        # 🔵 DYNAMIC ROUTING (UPDATED)
        # ---------------------------
        if intent == "dynamic":
            print("📊 Routing to TXT + LLM")

            try:
                 # 🔹 STEP 1: Load full college data
                context = data_loader.load()
                print(context)

                if not context:
                    print("❌ No context loaded")
                    return formatter.fallback("Data not available right now")

                print("📄 Context Loaded Successfully")

                 # 🔹 STEP 2: Send query + context to LLM
                answer = llm.generate(
                    query=corrected_query,
                    context=context,
                    history=history
                )

                print("💬 LLM Answer:", answer)

        # 🔹 STEP 3: Safety check (avoid undefined)
                if not answer or answer.strip() == "":
                    return formatter.fallback("I couldn't find the answer. Please try again.")

        # 🔹 STEP 4: Return formatted response
                session.add_message(session_id, "user", corrected_query)
                session.add_message(session_id, "assistant", answer)
                print(session.get_history(session_id))
               
          

                return formatter.format_llm(answer)

            except Exception as e:
                print("[DYNAMIC ERROR]", e)
                return formatter.error("Something went wrong while processing your request")
        # ---------------------------
        # 🟢 Static → Vector DB (RAG)
        # ---------------------------
        if intent == "static":
            print("📚 Routing to Vector DB")

            retrieved = rag_service.retrieve(corrected_query, k=10)
            print("Rag",retrieved)
            context = reranker.build_context(corrected_query, retrieved, top_k=3)
            print("Rerank",context)
            answer = llm.generate(corrected_query, context,history=history)
            session.add_message(session_id, "user", corrected_query)
            session.add_message(session_id, "assistant", answer)
            parsed = parser.parse(answer)
            
            return formatter.format_rag(answer, context)

        # ---------------------------
        # ❓ Final fallback (safe LLM)
        # ---------------------------
        llm_output = llm.generate(corrected_query, context=None,history=history)
        session.add_message(session_id, "user", corrected_query)
        session.add_message(session_id, "assistant", llm_output)
        return formatter.format_llm(llm_output)

    except Exception as e:
        print(f"[CHAT ERROR] {e}")
        return formatter.error("Something went wrong")