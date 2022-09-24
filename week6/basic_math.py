def even_number(n):
    numb = int(input("Enter a number "))
    for numb in range(1, n):

        if numb % 2 == 0:
            print("The number " + str(numb) + " is even")

def odd_number(n):
    num = int(input("enter a number "))
    for num in range(1, n):
        
        if num %2 != 0:
            print(str(num) + " is odd number ")

def all_sum(n):
    print("please enter the number: ")
    a = int(input("Current Number :"))
    b = int(input("Previous Number: "))
    sum = a + b
    print("sum :" + str(sum))

def make_list(n):

    original_list = [1, 2, 2, 4, 4, 6, 8, 2]
    print(original_list)

    new_list = original_list
    new_list.append(4)
    new_list.insert(0,9)
    new_list.remove(4)
    new_list.remove(4)
    new_list.remove(2)
    new_list.remove(2)
    new_list.remove(2)
    new_list.remove(1)
    print(new_list)

def main():
    even_number(22)
    odd_number(23)
    all_sum(6)
    make_list(8)
    
if __name__ == "__main__":
    main()