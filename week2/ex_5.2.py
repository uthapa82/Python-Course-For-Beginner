#equality and inequality
car = 'BMW'
print("\n Is car == 'BMW'? I predict True")

#lowercase function
print("\n Is car == 'bmw'? I predict false")
car = car.lower()
print("\n Is car == 'bmw'? I predict True")

#Numerical test
3 != 5
6 != 8
'BMW' != 'bmw'

#greater than
age_1 = 7
age_2 = 8
if age_1 > 10:
    print(age_1)
if age_2 < 5:
    print(age_2)

fruits = ["apple", "banana"]
if fruits == "apple":
    print(fruits)
if'apple' in fruits:
    print("apple")