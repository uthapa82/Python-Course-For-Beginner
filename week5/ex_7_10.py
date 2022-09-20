responses = {}
polling_active = True

while polling_active:
    user = input("What is your name? ")
    response = input("if you could visit one place in the world where would you go? ")

    responses[user] = response
    repeat = input("would you like to let another people respond? (yes/no)")

    if repeat == 'no':
        polling_active = False #break will also work

print("\n ----poll reasult----")
for user, response in responses.items():
    print(user.title() + " would you like to visit " + response)