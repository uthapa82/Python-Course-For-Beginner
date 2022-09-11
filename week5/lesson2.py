# user_command = ""
# while user_command != 'end':
#     user_command = input("Please give me command: ")
#     print(f"I am {user_command}....")
active = True
while active:
    correct_answer = 1152
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Please Guess a number: "))
        guess_count += 1 
        if guess == correct_answer:
            print("Congratulation !!! YOU WON :)")
            break
        else:
            print("Sorry that's not right")
            active = False 
