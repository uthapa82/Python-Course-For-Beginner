<<<<<<< HEAD
#conditional test.
prompt = ("\nenter a series of pizza topping")
prompt += ("\n Enter 'quit' to end the program" )
message = ""
while message != 'quit':
    message = input(prompt)
    print("message")

 #active variable.
prompt = ("\nenter a series of pizza topping")
prompt += ("\n Enter 'quit' to end the program" )
active = True
while True:
    message = input(prompt)

    if message == 'quit':
        print(active)
    else:
        print(message)

#break statement.
#prompt = ("\nenter a series of pizza topping")
#prompt += ("\n Enter 'quit' to end the program" )

#while True:

prompt = ("Enter your age")
prompt += ("\n Enter 'q' to end the program")
=======
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
>>>>>>> 3b740624c11e34b36699d1862baf4277f0659bf1
