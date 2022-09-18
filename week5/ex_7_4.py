#Pizza topping.
prompt = ("\nenter a series of pizza topping")
prompt += ("\n Enter 'quit' to end the program " )

while True:
    message = input(prompt)
   
    if message != 'quit':
        print("you'll add topping to your pizza")

    else:
        break