try:
    first = int(input("enter first number: "))

    second = int(input("Enter second number: "))

except ValueError:
    print("sorry, Enter number only")

else:
    sum = first + second
    print("The sum is " + str(first) + " and " + str(second) + " is " + str(sum))