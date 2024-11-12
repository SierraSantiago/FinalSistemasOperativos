from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from datetime import datetime
import uuid


class Person(BaseModel):
    name: str
    age: int
    profession: str

app = FastAPI()


data_folder = "./Request"

os.makedirs(data_folder, exist_ok=True)


@app.post("/add-person/")
async def add_person(person: Person):
    unique_filename = f"{uuid.uuid4()}.json"
    file_path = os.path.join(data_folder, unique_filename)
    
    with open(file_path, "w") as file:
        json.dump(person.dict(), file, indent=4)
    
    return {"message": "Person added", "file_path": file_path}
