def calculate_gpa(student, sub1, sub2, sub3, sub4, sub5):
    total_score = sub1 + sub2 + sub3 + sub4 + sub5
    average_score = total_score/5
    
    if average_score >= 90 and average_score <= 100:
        print(f"{student} got a grade of A")
    elif average_score >= 80 and average_score <= 89:
        print(f"{student} got a grade of B")
    elif average_score >= 70 and average_score <= 79:
        print(f"{student} got a grade of C")
    elif average_score >= 60 and average_score <= 69:
        print(f"{student} got a grade of D")
    else:
        print(f"{student} got a grade of F")
        
def main():
    student_name = input("Enter the name of Student: ")
    print("\n*******Enter score for following subjects (0-100)**********")
    sub1 = int(input("Math: "))
    sub2 = int(input("Science: "))
    sub3 = int(input("English: "))
    sub4 = int(input("Computer Science: "))
    sub5 = int(input("Account: "))
               
    calculate_gpa(student_name, sub1, sub2, sub3, sub4, sub5)

if __name__ == '__main__':
    main()