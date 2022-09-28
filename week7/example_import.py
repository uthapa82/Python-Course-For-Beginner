import os 

print(os.getcwd())

# print(os.chdir('/Desktop/Abhishek Fall 2022/Abhishek Python/Python-Course-For-Beginner/week7'))
user_command = input("Please enter the command: ")
if user_command == 'ls':
    print(os.listdir())

elif user_command == 'mkdir':
    file_name1 = input("Enter file name: ")
    print(os.mkdir(file_name1))

elif user_command == 'rmdir':
    file_name = input("Please enter which file you want to delete: ")
    user_input = input("Are you sure ? (Y/N) ")
    if user_input == 'Y':
        print('week7/'+ file_name)
        print(os.rmdir(file_name))
    else:
        print("OK I don't delete it ")

else:
    print("No command found")