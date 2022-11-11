import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        userinput = json.load(f)
except FileNotFoundError:
    userinput = input("Enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(userinput, f)
        print("Thats nice number")
else:
    print("I know your favorite number its " + str(userinput))