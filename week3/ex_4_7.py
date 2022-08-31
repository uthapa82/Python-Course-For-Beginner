"""Maake a list of the multiples of 3 fromo 3 to 30. use for loop to print the no in your list"""
mul_no = range(1,11)
for mul_no in range(1*3,1,11):
    print(mul_no)

multiples_numbers = [value*3 for value in range(1,11)]
print(multiples_numbers)