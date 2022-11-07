import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """prompt for a new username."""
    username = input("What is your name??")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "?" + "y/n")
        if correct == 'y':
            print("welcomeback, " + username)
        else:
            username = get_new_username()
            print("we will remembers when you come back back again, " + username)

    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username)

greet_user()