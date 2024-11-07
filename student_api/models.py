from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class StudentBase(BaseModel):
    name: constr(min_length=1, max_length=100) # type: ignore
    age: int
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 20,
                "email": "john.doe@example.com"
            }
        }

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int