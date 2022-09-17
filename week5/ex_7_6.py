prompt = ("Enter your age: (3 times max) ")

counter = 0
while counter < 3:
    age = int(input(prompt))
    
    if age < 3:
        print("ticket is free")
    elif age < 12:
        print("the ticket is $10")
    else:
            print("the ticket is $15")
        
    counter += 1
