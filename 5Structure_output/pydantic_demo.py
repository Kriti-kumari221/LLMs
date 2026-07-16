from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str = "Kriti"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        description="A decimal value representing the CGPA of the student."
    )
new_student = {
    "age": "32",
    "email": "abc@gmail.com",
    "cgpa": 5
}
student = Student(**new_student)
print(student)