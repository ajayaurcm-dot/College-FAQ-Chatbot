from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import chat, admin
from app.config import settings


# ---------------------------
# App Initialization
# ---------------------------
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

# ---------------------------
# Middleware (CORS)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Routes
# ---------------------------
app.include_router(chat.router, tags=["Chat"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])


# ---------------------------
# Health Check
# ---------------------------
@app.get("/")
def root():
    return {
        "status": "running",
        "app": settings.APP_NAME
    }


@app.get("/health")
def health():
    return {"status": "healthy"}