def language_poll(name, language, age=''):
    
    person = {
        name: language
    }
    if age:
        person['age'] = age
  
    
    return person

example = language_poll('Anu', 'Python')
example1 = language_poll('Anup', 'C', age=16)
print(example)

# using function with a while loop 
def get_fromatted_name(first_name, last_name):
    full_name = first_name + ' '  + last_name
    
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("\nEnter 'q' at any time to quit ")
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    if f_name == 'q' or l_name == 'q':
        break
    else:
        formatted_name = get_fromatted_name(f_name, l_name)
        print("\nHello , " + formatted_name + "!")

# Passing a list 
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)

def main():
    username = ['Anu', 'Anusha', 'Anup']
    greet_users(username)
    
if __name__ == "__main__":
    main()
