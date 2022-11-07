from lesson4 import get_formatted_name

def main():
    print("Enter 'q' to quit: ")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        
        last = input("\nPlease give me a last name: ")
        if last == 'q':
            break
        
        formatted_name = get_formatted_name(first, last)
        print("\tNeatly formatted name: " + formatted_name + '.')

if __name__ == "__main__":
    main()