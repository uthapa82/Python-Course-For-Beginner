import json as j

def main():
    userinput = int(input("Enter a number : "))
    
    filename = 'number.json'
    with open (filename, 'w') as f:
        j.dump(userinput, f)

if __name__ == '__main__':
    main()