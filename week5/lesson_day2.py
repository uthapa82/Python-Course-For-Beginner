# function body 
# information ==> parameters 

def sample_function():
    # docstring
    """Sample function example """
    print("Hello, I am a function")

# function call 
# information ==> arguments   
sample_function() 

# with argument
# (a^2-b^2) = (a-b)(a+b)
def simplify_eqn(a, b):
    print("Function with arguments")
    result =  (a - b) * (a + b)
    #display 
    #display = print(result)
    return result

print(simplify_eqn(4, 3))

# positional arguments 
def animal_human(human, animal):
    """Display information"""
    print("\nPositional Arguments :")
    print(human + " have " + animal + " in his house.")

# multiple function call 
# order matters --> no mismatch   
animal_human("Dog", "Abhishek")
animal_human("Anup", "Cat")
animal_human(human="Anu", animal="Mouse")  # keyword arguments, name-value pair 

# default value format ==> two_table(second, first_no = '2')
def multiplication_table(number):
    print("\nMultiplication table of " + str(number))
    
    for num in range(1, 11):
        result = number * num
        print(str(number) + ' X ' + str(num) + " = " + str(result))
 
multiplication_table(5)

# return function
def calculate_sum(a, b):
    sum = a + b
    return sum

#print("Sum is :", calculate_sum(2, 3))
# x = 3(a + b) - 2ab 

def simplify_eq(a, b):
    result = 3 * calculate_sum(a, b) - 2*a*b
    print("x is :", result)

simplify_eq(5, 8)
    
# making an argument optional 
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
        
    return full_name.title()

print("\nOptional Argument Example: ")
print(get_formatted_name("Bijula", "Lamichhance"))
print(get_formatted_name("Ram", "Lamichhance", "Bahadur"))
