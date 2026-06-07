from fastapi import APIRouter
from app.services.dynamic_data import DynamicDataService

router = APIRouter()
db = DynamicDataService()


# ---------------------------
# Add Course Fee
# ---------------------------
@router.post("/add-course")
def add_course(department: str, fee: float):
    query = """
        INSERT INTO courses (department, fee)
        VALUES (:dept, :fee)
    """
    db.execute_query(query, {"dept": department, "fee": fee})
    return {"status": "success", "message": "Course added"}


# ---------------------------
# Update Fee
# ---------------------------
@router.put("/update-fee")
def update_fee(department: str, fee: float):
    query = """
        UPDATE courses
        SET fee = :fee
        WHERE department = :dept
    """
    db.execute_query(query, {"dept": department, "fee": fee})
    return {"status": "success", "message": "Fee updated"}


# ---------------------------
# Delete Course
# ---------------------------
@router.delete("/delete-course")
def delete_course(department: str):
    query = """
        DELETE FROM courses
        WHERE department = :dept
    """
    db.execute_query(query, {"dept": department})
    return {"status": "success", "message": "Course deleted"}