user_name = input("what is your name ?")
filename = 'guest.txt'

with open (filename, 'w') as file_object:
    file_object.write(user_name)