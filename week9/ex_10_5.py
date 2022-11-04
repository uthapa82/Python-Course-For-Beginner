filename = 'response.txt'

while  True:
    response = input("\nWhy do you like programming ? ")
    print("Do you like to add response ? (y/n) " )

    if response == 'n':
        break

    else:
        with open(filename, 'a') as f:
            f.write(response + "\n")
        