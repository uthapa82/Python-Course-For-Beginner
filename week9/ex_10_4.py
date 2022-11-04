filename = 'guest_book.txt'

print("enter 'q' to quit ")

while True:
    name = input("\nEnter your name ")
    
    if  name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')
        print("hello " + name + " you are invited")