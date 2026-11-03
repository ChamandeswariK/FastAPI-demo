from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give the name of the patient in less than 50 characters', examples=['Chamandeswari', 'Amit'])]
    age: int = Field(gt=0, lt=100)
    # email : EmailStr
    linkdin_url : AnyUrl
    # weight : float = Field(gt=0)
    weight : Annotated[float, Field(gt=0, strict=True)]
    married : Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies : Annotated[Optional[List[str]],Field(default=None, max_length=5)]
    # allergies : Optional[List[str]] = Field(max_length=5)
    contact_details: Dict[str, str]

patient_info = {'name':'chamandeswari', 'age' :'76','linkdin_url':'http://linkdin.com/231', 'weight':90.3, 'married': True, 'allergies':['dust'], 'contact_details':{'email':'xyz@sasd.com','phone':'12341'}}

def insert_patient_data(Patient1: Patient):
    print(Patient1.name)
    print(Patient1.age)
    print(type(Patient1.age))
    print("Inserted")


Patient1 = Patient(**patient_info) # unpack the dictionary

insert_patient_data(Patient1)