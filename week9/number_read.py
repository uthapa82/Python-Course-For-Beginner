import json

def main():

    filename = 'number.json'
    with open(filename) as f:
        number = json.load(f)

    print("i know your favorite number, it's " + str(number))

if __name__ == '__main__':
    main()