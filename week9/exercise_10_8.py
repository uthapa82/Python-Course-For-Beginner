filename = ['cat.txt', 'dog.txt']

for i in filename:
    try:
        with open (filename) as f_obj:
            contents = f_obj.read()

    except TypeError:
        print("sorry, file not found")