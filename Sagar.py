from datetime import date, timedelta
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    attendance: dict[date, bool] = {}

class AttendanceSummary(BaseModel):
    total_students: int
    present_students: int
    absent_students: int
    attendance_percentage: float

def generate_attendance_summary(students: list[Student]) -> AttendanceSummary:
    total_students = len(students)
    present_students = sum(1 for student in students if student.attendance)
    absent_students = total_students - present_students
    attendance_percentage = (present_students / total_students) * 100

    return AttendanceSummary(
        total_students=total_students,
        present_students=present_students,
        absent_students=absent_students,
        attendance_percentage=attendance_percentage
    )

@app.get("/attendance_summary", response_model=AttendanceSummary)
def get_attendance_summary():
    # Replace this with your actual data retrieval logic
    students = [
        Student(id=1, name="Alice", attendance={date(2022, 1, 1): True, date(2022, 1, 2): False}),
        Student(id=2, name="Bob", attendance={date(2022, 1, 1): True, date(2022, 1, 2): True}),
        Student(id=3, name="Charlie", attendance={date(2022, 1, 1): False, date(2022, 1, 2): False}),
    ]

    return generate_attendance_summary(students)