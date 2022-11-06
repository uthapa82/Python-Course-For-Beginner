import json as j

def main():
    numbers =[2, 4, 6, 8]
    filename = 'numbers.json'
    with open(filename, 'w') as f:
        j.dump(numbers, f)

if __name__ == "__main__":
    main()