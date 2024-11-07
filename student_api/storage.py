from typing import Dict, List, Optional
from threading import Lock
from .models import Student, StudentCreate

class StudentStore:
    def __init__(self):
        self._students: Dict[int, Student] = {}
        self._lock = Lock()
        self._counter = 0
    
    def create(self, student: StudentCreate) -> Student:
        with self._lock:
            self._counter += 1
            new_student = Student(
                id=self._counter,
                name=student.name,
                age=student.age,
                email=student.email
            )
            self._students[new_student.id] = new_student
            return new_student
    
    def get_all(self) -> List[Student]:
        with self._lock:
            return list(self._students.values())
    
    def get_by_id(self, student_id: int) -> Optional[Student]:
        with self._lock:
            return self._students.get(student_id)
    
    def update(self, student_id: int, student_data: StudentCreate) -> Optional[Student]:
        with self._lock:
            if student_id not in self._students:
                return None
            updated_student = Student(
                id=student_id,
                name=student_data.name,
                age=student_data.age,
                email=student_data.email
            )
            self._students[student_id] = updated_student
            return updated_student
    
    def delete(self, student_id: int) -> bool:
        with self._lock:
            if student_id not in self._students:
                return False
            del self._students[student_id]
            return True