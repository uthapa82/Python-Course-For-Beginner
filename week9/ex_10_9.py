filename = ['cat.txt', 'dog.txt', 'cow.txt']

for i in filename:
    print("\nOpening file: " + i)
    try:
        with open (i) as f_obj:
            contents = f_obj.read()
            print(contents)

    except FileNotFoundError:
        pass
