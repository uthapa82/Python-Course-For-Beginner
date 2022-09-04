# list comprehension 
squares = [value**2 for value in range(1,11)]
print(squares)

list_1 = ["Nepal", "KTM", "NJ", "NY"]
for place in list_1[:]:
    print(place)
    
    
list_2 = [1, 2, 3, 4]
list_3 = list_2[:] + [5, 6, 7, 8, 9, 10]
print(list_3)

# tupples : immutable list 
price = ('$10', '$20', '$40')
print(price[0])

for i in price:
    print(i)
    
price = ('$30', '$50', '$60')
for j in price:
    print(j)