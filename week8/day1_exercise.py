#------------------------------------------------------------------------------------------
# Day 1 Exercise                                                                          #
# 10/17/2022                                                                              #
#                                                                                         #            
# 1. Print the following pattern using loop (function name => pattern_print())            #
#   $ python3 day1_exercise.py                                                            #
#      1                                                                                  #
#      2 2                                                                                #
#      3 3 3                                                                              #
#      4 4 4                                                                              #
#                                                                                         #
# 2. Ask a user for a number store it in a list and find the length of the list           #
#   function name :- list_length(user_list)                                               #
#                                                                                         #
#                                                                                         #
# 3. Write a function to reverse a user string. function name reverse_string(user_string) #
#      Sample: user input:thapa output: apaht                                             #
#------------------------------------------------------------------------------------------

"""
__summary__
program that includes function to print pattern, 
reverse string and return the length of the string 

"""

def pattern_print(num):
    """
    takes a integer input and prints a pattern till num
    Args:
        num (_type_): integer
    """    
    for i in range(1, num):
        print(str(i) * i)

def list_length(user_lst):
    """takes user list and prints the length of the list 

    Args:
        user_lst (_list_): user list 
    """    
    print("length of the list is ", len(user_lst))

def reverse_string(user_string):
    """takes string from user and prints the reverse of it 

    Args:
        user_string (string): _description_
    """    
    print(user_string[::-1])

def main():

    #user input pattern_print
    print("Print Pattern......")
    number = int(input("Enter number to print pattern till: "))
    pattern_print(number)

    #user_list input 
    ("Length of the list: ")
    user_input = input("Enter the numbers separated by spaces: ")
    # for i in range(0, userinput):
    #     value = int(input('Enter a number: '))
    #     user_list.append(value)
    user_list = user_input.split()
    list_length(user_list)

    #user string input
    print("Reverse the string....")
    user_string = input("Please Enter a Word to reverse: ")
    reverse_string(user_string)


if __name__ =='__main__':
    main()