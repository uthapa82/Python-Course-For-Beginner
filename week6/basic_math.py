def even_number(n):
    for numb in range(1, n):

        if numb % 2 == 0:
            print("The number " + str(numb) + " is even")

def odd_number(n):
    for num in range(1, n):
        
        if num %2 != 0:
            print(str(num) + " is odd number ")

def all_sum(n):
    previous_num = 0
    for num in range(n):
        result_sum = previous_num + num
        print(f"Current Number: {num} Previous number: {previous_num} Sum: {result_sum}".format(num, previous_num, result_sum))
        previous_num = num
        
def make_list(n):
    original_list = [value for value in range(n)]
    print(original_list)

    new_list = original_list
    new_list.append(4)
    new_list.insert(0,9)
    new_list.remove(4)
    print(new_list)
    

def main():
    user_input = int(input("Please enter the number: "))
    even_number(user_input)
    odd_number(user_input)
    all_sum(user_input)
    make_list(user_input)
    
if __name__ == "__main__":
    main()