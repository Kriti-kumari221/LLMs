from typing import TypedDict
class Person(TypedDict):
    name:str
    age: int
new_person: Person={"name":'kriti','age':35}
print(new_person)
#it just tells us that this shuld be this type of data 
