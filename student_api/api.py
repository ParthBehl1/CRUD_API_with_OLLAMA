from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from typing import List
from .models import Student, StudentCreate
from .storage import StudentStore
from .ollama import generate_student_summary

app = FastAPI(
    title="Student Management API",
    description="An interactive and AI-enhanced API for managing student records, including CRUD operations and AI-powered summaries.",
    version="1.0.0",
    contact={
        "name": "Support",
        "email": "support@example.com",
    },
)

# Initialize the student store (in-memory or database)
store = StudentStore()

# Redirect root to /docs
@app.get("/")
async def redirect_to_docs():
    """Redirect to the FastAPI documentation"""
    return RedirectResponse(url="/docs")
async def validate_student_exists(student_id: int) -> Student:
    student = store.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students", response_model=Student, status_code=201, tags=["Student Operations"])
async def create_student(student: StudentCreate):
    """
    Create a new student profile.

    - **name**: Full name of the student
    - **age**: Age of the student
    - **email**: Contact email for the student
    """
    return store.create(student)

@app.get("/students", response_model=List[Student], tags=["Student Operations"])
async def get_students():
    """Retrieve all student profiles."""
    return store.get_all()

@app.get("/students/{student_id}", response_model=Student, tags=["Student Operations"])
async def get_student(student: Student = Depends(validate_student_exists)):
    """Retrieve a student profile by ID."""
    return student

@app.put("/students/{student_id}", response_model=Student, tags=["Student Operations"])
async def update_student(student_id: int, student_data: StudentCreate):
    """
    Update a student profile by ID.

    - **student_id**: ID of the student to update
    - **student_data**: New data for the student profile
    """
    updated_student = store.update(student_id, student_data)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}", status_code=204, tags=["Student Operations"])
async def delete_student(student: Student = Depends(validate_student_exists)):
    """Delete a student profile by ID."""
    store.delete(student.id)
    return JSONResponse(content={"message": "Student deleted successfully"}, status_code=204)

@app.get("/students/{student_id}/summary", tags=["AI-Powered Summary"])
async def get_student_summary(student: Student = Depends(validate_student_exists)):
    """
    Generate a brief AI-powered summary of a student's profile.

    Uses the Llama language model to create a professional summary.
    """
    try:
        summary = await generate_student_summary(student)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating summary: {str(e)}"
        )

