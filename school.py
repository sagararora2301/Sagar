students=[]



def add_student():
    print("\nEnter student details:")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    new_student = {"Name": name, "Age": age, "Grade": grade}
    students.append(new_student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\nList of students:")
    for index, student in enumerate(students, 1):
        print(f"{index}. Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")


def delete_student():
    if not students:
        print("No students found.")
        return
    view_students()
    index = int(input("\nEnter the index of the student to delete: ")) - 1
    if 0 <= index < len(students):
        del students[index]
        print("Student deleted successfully!")
    else:
        print("Invalid index.")

def menu():
    print("\nSchool Admission System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from the menu.")
