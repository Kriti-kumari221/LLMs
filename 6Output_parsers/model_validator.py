#use for multiple data validatioon 
from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient older that 60 must have an emergency contact ")
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
patient_info={'name':'kriti','email':'abc@hdfc.com','linkedin_url':'https://linkedin.com/123','age':67,'weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':342342,'emergency':'34564645'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)
    
