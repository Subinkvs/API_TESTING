from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Temporary storage
students = [
    {"id": 1, "name": "Rahul", "age": 21},
    {"id": 2, "name": "Anu", "age": 22}
]


# Data model
class Student(BaseModel):
    name: str
    age: int


@app.get('/')
def greeting():
    return f'This is a FASTAPI'

# CREATE
@app.post("/students")
def create_student(student: Student):

    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)

    return new_student


# READ - Get all students
@app.get("/students")
def get_students():
    return students


# READ - Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for existing_student in students:

        if existing_student["id"] == student_id:

            existing_student["name"] = student.name
            existing_student["age"] = student.age

            return existing_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
