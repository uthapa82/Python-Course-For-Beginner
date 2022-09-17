prompt = ("Enter your age")
prompt += ("\n Enter 'q' to end the program")

while True:
    age = input(prompt)
   
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("ticket is free")
        
    elif age < 12:
        print("the ticket is $10")
    else:
        print("the ticket is $15")
