filename = 'responses_2.txt'

responses = []

while True:
    user_response = input("\nWhy do you like programming? ")
    responses.append(user_response)
    
    user_action = input("Do you like to answer again ? (y/n) ")
    if user_action == 'n':
        break

with open(filename, 'a') as f:
    for i in responses:
        f.write(i + "\n")