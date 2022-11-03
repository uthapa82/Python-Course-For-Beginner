filename = 'guest_book.txt'
#with open(filename, 'a') as file_object:
 #   file_object.write("what is your name")
print("enter 'q' to quit ")

while True:
    name = input("Enter your name ")
    if  name == 'q':
        print("hello " + name + " you are added to guestbook")
    else:
        print()

    with open(filename, 'a') as file_object:
        file_object.write("what is your name")

    print("hello " + name + " you are invited")