def generate_result():
    student_name = input("enter the name of the student ")
    maths = int(input("maths : "))
    science = int(input("science : "))
    english = int(input("English : "))
    computer_science = int(input("computer science : "))
    account = int(input("Account : "))

    total = maths + science + english + computer_science + account
    per = total / 5

    if per >= 90:
        print(student_name + " got grade of A ")
    elif per >= 85:
        print(student_name + " got grade of B")
    elif per >= 75:
        print(student_name + " got grade of C")
    elif per >= 65:
        print(student_name + " got grade of D")
    else:
        print(student_name + " got grade of F ")
