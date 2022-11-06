print("Enter 'q' to quit" )

while True:
    try:
        first = int(input("enter first number: "))
        if first == 'q':
            break
        
        second = int(input("Enter second number: "))
        if second == 'q':
            break

    except ValueError:
        print("Invalid input, enter number only")
    
    else:
       sum = first + second
       print("\nThe sum is " + str(first) + " and " + str(second) + " is " + str(sum) + "\n")