"""Make a list of the multiples of 3 fromo 3 to 30. use for loop to print the no in your list"""
mul_no = []
for no in range(1, 11):
    no = no * 3
    mul_no.append(no)
    
print(mul_no)

# way 2
multiples_numbers = [value*3 for value in range(1,11)]
print(multiples_numbers)