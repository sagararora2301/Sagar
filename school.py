import json

def load_data():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("students.json", "w") as file:
        json.dump(data, file)

def add_student():
    print("\nEnter student details:")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    new_student = {"Name": name, "Age": age, "Grade": grade}
    students.append(new_student)
    save_data(students)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\nList of students:")
    for index, student in enumerate(students, 1):
        print(f"{index}. Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")

def search_student():
    if not students:
        print("No students found.")
        return
    search_name = input("\nEnter student name to search: ")
    found = False
    for student in students:
        if student['Name'].lower() == search_name.lower():
            print(f"Student found - Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student():
    if not students:
        print("No students found.")
        return
    view_students()
    index = int(input("\nEnter the index of the student to delete: ")) - 1
    if 0 <= index < len(students):
        del students[index]
        save_data(students)
        print("Student deleted successfully!")
    else:
        print("Invalid index.")

def menu():
    print("\nSchool Admission System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

students = load_data()

while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from the menu.")
