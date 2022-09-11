# nesting multiple dictionary 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# using range 
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# Show the first 5 aliens:
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] == 'red' 
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# using list in dictionary 
print("\n List in dictionary")
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

for topping in pizza['toppings']:
    print("\t" + topping)
    
    
favorite_languages = {
'jen':  ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n"+ name.title() + "'s favorite language are: ")
    
    for language in languages:
        print("\t" + language.title())

# dictionary in a dictionary 
users = {
   'aeinstein':{
       'first': 'albert',
       'last': 'einstein',
       'location': 'princeton',
   } ,
   'mcurie':{
       'first': 'marie',
       'last': 'curie',
       'location': 'paris',
   },
   'abhi':{
       'first': 'abhishek',
       'last': 'lamichhance',
       'location': 'nepal'
   }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())


# taking user input 
riders_age = int(input("Please enter your age: "))

if riders_age == 21:
    print('you are 21 years old')
elif riders_age == 10:
    print("you are 10 years old ")
else:
    print('Any value')
    
    
list_eg = [1, 2, 3, 4]
i = 0
while i < len(list_eg):
    print(list_eg[i])
    i += 1
