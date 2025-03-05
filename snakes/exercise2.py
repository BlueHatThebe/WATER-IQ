student_mark = int(input("Please enter student mark: "))
pass_mark = 50

def get_result():
    if student_mark < pass_mark and student_mark > 0:
        print("Fail")
    elif student_mark >= pass_mark and student_mark <= 59:
        print("Average pass")
    elif student_mark >= 60 and student_mark <= 100:
        print("Pass")
    elif student_mark < 0:
        print("Mark cannot be below zero")
    elif student_mark > 100:
        print("Mark cannot be above 100")

get_result()