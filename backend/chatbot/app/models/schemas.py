from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


# ---------------------------
# Chat Request
# ---------------------------
class ChatRequest(BaseModel):
    query: str = Field(..., example="What is CSE fee?")
    session_id: Optional[str] = Field(None, example="user123")


# ---------------------------
# Chat Response
# ---------------------------
class ChatResponse(BaseModel):
    status: str = Field(..., example="success")
    response: str = Field(..., example="The fee for CSE is ₹120000.")
    data: Optional[Dict[str, Any]] = None
    source: str = Field(..., example="db")


# ---------------------------
# Option Response (when clarification needed)
# ---------------------------
class OptionResponse(BaseModel):
    type: str = "options"
    message: str
    options: List[str]


# ---------------------------
# Error Response
# ---------------------------
class ErrorResponse(BaseModel):
    status: str = "error"
    response: str
    data: Optional[Any] = None
    source: str = "system"


# ---------------------------
# Admin Schemas (Basic)
# ---------------------------

class Course(BaseModel):
    department: str
    fee: float


class Admission(BaseModel):
    start_date: str
    end_date: str


class Seat(BaseModel):
    department: str
    total_seats: int
    available_seats: int


class Event(BaseModel):
    event_name: str
    event_date: str
    fee: Optional[float] = 0.0