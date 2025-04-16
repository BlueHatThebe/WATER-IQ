class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = []  

    def enroll_course(self, course_name, grade):
        if not course_name or not grade:
            print("Error: Course name and grade cannot be empty")
            return False
        self.courses.append((course_name, grade))
        return True

    def display_details(self):
        print(f"\nStudent Details:")
        print(f"Name: {self.student_name}")
        print(f"ID: {self.student_id}")
        if self.courses:
            print("Courses and Grades:")
            for course, grade in self.courses:
                print(f"  {course}: {grade}")
        else:
            print("No courses enrolled yet")


class StudentManagementSystem:
    def __init__(self):
        self.students = []  

    def add_student(self, student_name, student_id):
        if not student_name or not student_id:
            print("Error: Student name and ID cannot be empty")
            return
         
        for student in self.students:
            if student.student_id == student_id:
                print("Error: Student ID already exists")
                return
        new_student = Student(student_name, student_id)
        self.students.append(new_student)
        print(f"Confirmation: Student {student_name} (ID: {student_id}) added successfully")

    def enroll_student(self, student_id, course_name, grade):
        student = self._find_student(student_id)
        if student:
            if student.enroll_course(course_name, grade):
                print(f"Confirmation: Enrolled {student.student_name} in {course_name} with grade {grade}")
        else:
            print("Error: Student not found")

    def view_student_details(self, student_id):
        student = self._find_student(student_id)
        if student:
            student.display_details()
        else:
            print("Error: Student not found")

    def list_all_students(self):
        if not self.students:
            print("No students registered in the system")
            return
        print("\nAll Registered Students:")
        for student in self.students:
            print(f"Name: {student.student_name}, ID: {student.student_id}")

    def _find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add a new student")
        print("2. Enroll student in a course")
        print("3. View student details")
        print("4. List all students")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            sms.add_student(name, student_id)
            
        elif choice == "2":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = input("Enter grade: ")
            sms.enroll_student(student_id, course_name, grade)
            
        elif choice == "3":
            student_id = input("Enter student ID: ")
            sms.view_student_details(student_id)
            
        elif choice == "4":
            sms.list_all_students()
            
        elif choice == "5":
            print("Thank you for using the Student Record Management System. Goodbye!")
            break
            
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 5")


if __name__ == "__main__":
    main()