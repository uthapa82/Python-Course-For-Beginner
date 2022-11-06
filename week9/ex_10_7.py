print("Enter 'q' to quit")

while True:
    first = int(input("enter first number: "))
    if first == 'q':
        break
    
    second = int(input("Enter second number: "))
    if second == 'q':
        break
        
    try:
        sum = first + second

    except ValueError:
        print("sorry cant add")

    print(sum)