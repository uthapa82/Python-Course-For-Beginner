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
