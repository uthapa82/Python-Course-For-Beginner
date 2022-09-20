responses = {}

#set flag 
polling_active = True

while polling_active:
    name = input("\nPlease enter your name: ")
    answer = input("Which language you want to learn ?: ")
    
    # store the responses 
    responses[name] = answer 
    
    repeat = input("would you like to add another person ? (y for Yes , n for No): ")
    if repeat == 'n' or 'no' or 'No':
        polling_active = False
    
print("\n Polling Result----------------* ")

for name, answer in responses.items():
    print(name + " would like to learn " + answer + ".")
    