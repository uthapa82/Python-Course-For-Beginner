#Practice.
#prompt = ("tell me who your are")
#prompt = ("what is your name." )
#name = input(prompt)
#print("hello" + name)

#Pizza topping.
prompt = ("\nenter a series of pizza topping")
prompt += ("\n Enter 'quit' to end the program" )
#message = " "

while True:#message != 'quit':
    message = input(prompt)
   
    if message == 'quit':
         break

    else:
        print("you'll add topping to your pizza")