#is  data validation library for python it ensure that the data you work with is correct structured and type-safe 
from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name: str="Kriti"
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0, lt=10)
new_student={"age": '32','email': 'abc@gmail.com','cgpa':5, description=" A decimal value representing the cgpa of the student "}
student=Student(**new_student)
print(student)
#it do type ocnversion also like "34" it will convert to 32