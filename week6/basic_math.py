def even_number(n):
    numb = int(input("Enter a number "))
    for numb in range(1, n):

        if numb %2 == 0:
            print("The number " + str(numb) + " is even")
        else:
            print("The number " + str(numb) + " is odd")

def all_sum(n):
    print("please enter the number: ")

        

def main():
    even_number(22)
    
if __name__ == "__main__":
    main()