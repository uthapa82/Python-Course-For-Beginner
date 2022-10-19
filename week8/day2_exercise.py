#------------------------------------------------------------------------------------------
# Day 2 Exercise                                                                          #
# 10/19/2022                                                                              #
#                                                                                         #            
# 1. Take a list as a user input, first and last number, change the first and last element#
#  of the list                                                                            #
#   function name ==> swap_element(user_list, first, last)                                #
#                                                                                         #
#                                                                                         #
# 2. Write a function which takes two numbers and find the maximum and minimum numbers    #
#     function name ==> max_min(num1, num2)                                               #                                       
#                                                                                         #
# 3. Write a function that takes a word as input from user and prints 'the word is even'  #
#    if the word contains even number of character, else print 'the word is odd           #
#      funtion name ==>  odd_even(user_string )                                           #
#                                                                                         #
# Sample output:                                                                          #
#    $ python3 day2_exercise.py                                                           #
#         Exercise 1 ......                                                               #
#         Please enter number separated by spaces: 0 2 3 4 6                              #
#         Original List: [0 2 3 4 6]                                                      #
#         Changed List: [1 2 3 4 5]                                                       #
#         
#         Exercise 2...........                                                           #
#         Maximim number is : 9                                                           #
#         Minimum number is : 6                                                           #
#                                                                                         #
#         Exercise 3 ...........                                                          #
#         Please enter a word: Anu                                                        #
#         The word is odd (because Anu is three character 'a', 'n', 'u')                  #
#------------------------------------------------------------------------------------------
def swap_element(user_list, first, last):
    first = [0, 2, 3, 4, 6]
    first[0] = 1
    first[4] = 5
    first = last
    print(last)
    
def max_min(num1, num2):
    num1 = int(input("enter a number "))
    numb2 = int(input("enter a number "))

    if num1 > numb2:
        print("maximum number is " + num1)

    else:
        print("minimum number is " + num2)

def odd_even(user_string):
    if user_string == 2:
        print("The word is even ")
    else:
        print("The word is odd ")

def main():
    user_list = input("please enternumber seperaely by space ") 

    #exercise 3
    user_input = input("please enter a word: ")

if __name__ == '__main__':
    main()
