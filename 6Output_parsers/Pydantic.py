# def insert_patient_data(name: str,age:int):
#     if(type(name)==str and type(name)==int):
#         print(name)
#         print(age)
#         print("inserted into database")
#     else:
#         raise TypeError("Incorrect data type")
# insert_patient_data('nitish', 30)

# #it wont give error if i passed string insted of interger 
# # so we need to use Pydantic to make more clear 
# # # in python we don't have type validation, and in data validation wont disturb solve this kind of problem in pydantic 
# # Pydantic 
# # Define pyndantic model ideal schema 
# # initiate the model with raw input data 
# # pass validation model object 

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="NAME of he person",description='Give the name of the patient in less that 50 char ',examples=['kriti','amit'])]
    age:int=Field(gt=0 , lt=120)
    email:EmailStr
    linkedin_url:AnyUrl
    weight:float=Field(gt=0)
    allergies:Optional[List[str]]=Field(max_length=5)
    contact_details:Dict[str,str]
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("instrected")

def update_patient_data(patient:Patient):
     print(patient.name)
     print(patient.age)
     print("Updated")
patient_info={'name':'kriti','email':'abc@gmail.com','linkedin_url':'https://linkedin.com/123','age':30,'weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':342342}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)
    
