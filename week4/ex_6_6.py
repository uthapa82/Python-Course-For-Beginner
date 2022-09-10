favorite_language = {
    "Anu": "C",
    "Abhishek": "Pyhton",
    "Anusha": "Java"
    }
for name, language in favorite_language.items():
    print(name.title() +"'s favorite language is " + language.title() + ".")
    
print("\n")
people_list = ['Ayushma', 'John', 'Harry', 'Anu', 'Anusha']
for people in people_list:
    if people in favorite_language.keys():
        print("Thankyou for taking the poll, " + people.title() + ":)")
    else:
        print(people.title() + ", What is your favorite programming language ?")
