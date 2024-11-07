from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class StudentBase(BaseModel):
    name: constr(min_length=1, max_length=100) # type: ignore
    age: int
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Parth Behl",
                "age": 20,
                "email": "parth.behl@example.com"
            }
        }

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int