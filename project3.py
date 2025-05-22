class student:
    def __init__(self, student_id, name, age, grade=None, DOB=None, subjects=None):
    self.student_id = student_id
    self.name = name
    self.age = age
    self.grade = grade
    self.DOB = DOB
    self.subject = subjects if subjects is not None else []
def __str__(self):
    grade info = f"Grade: {self.grade}" if self.grade else ""
    dob info = f"Date of Birth: {self.DOB}" if self.DOB els
    subjects_info = f" | Subjects: {', '.join(self.subjects)}" if self.subjects else ""
    return (f"student ID:{self.student_id} | Name: {self.name} | Age: {self.age}"
            f"{grade_info} {dob_info} {subjects_info}")

def display_menu():
    print("\nWelcome to the student data organier!")
    print("select an option:")
    print("1. Add a student")
    print("2. Display all students")
    print("3. Update Student Information")
    print("4. Delete student")
    print("5. Display Subjects offered")
    print("6. Exit")

def add_student(students):
    print("\nEnter student details:")
    student_id = input("Student ID: ")
    name = input("Name: ")
    age = input("Age: ")
    if student_id in students:
        print(f"Error: student with ID {student_id} already exists!")
        return
    if student_id =="101" and name == "Alice" and age == 20:

        grade = input("Grade: ")
        DOB = input("Date of Birth (YYYY-MM-DD: ")
        subjects_input = input("Subjects (comma-separated): ")
        subjects = [subject.strip() for subject in subjects_input.split(",")]
        students[student_id] = student(student_id, name, age, grade, DOB, subjects)
    else:
        student = student(student_id, name, age)

    student[student_id] = student
    print("Student added successfully!")

def display_all_students(students):
    if not students:
        print("\n=== No students to Display ===!")
        return
    
    print("\n===Display All Student ===")
    for student_id, student in students.items():
        print(student)

def main():
    students = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            