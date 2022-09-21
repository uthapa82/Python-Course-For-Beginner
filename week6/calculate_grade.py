student_name = input("enter the name of the student ")
M = int(input("maths : "))
S = int(input("science : "))
E = int(input("English : "))
c_s = int(input("computer science : "))
A = int(input("Account : "))

total = M + S + E + c_s + A
per = total/ 5

if per >= 90:
    print(student_name + " got grade of A ")
elif per >= 85:
    print(student_name + " got grade of B")
elif per >= 75:
    print(student_name + " got grade of c")
elif per >= 65:
    print(student_name + " got grade of D")
else:
    print(student_name + " got grade of F ")