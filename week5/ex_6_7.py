main_list = []
people_list_1 = {
    'first_name': 'Abhishek', 
    'last_name': 'Lamichhane',
    'age': '19', 
    'city': 'kathmandu',
    }
#main_list.append(people_list_1)

people_list_2 = {
    'first_name': 'anu',
    'last_name': 'thapa',
    'age': 22,
    'city': 'bhaktapur',
}
#main_list.append(people_list_2)

people_list_3 = {
    'first_name': 'abhi',
    'last_name': 'guragai',
    'age': 16,
    'city': 'kathmandu',
}
#main_list.append(people_list_3)
people_list = [people_list_1, people_list_2, people_list_3]

for people in people_list:
    full_name = people['first_name'].title() + " " + people['last_name'].title()
    people_age = people['age']
    people_city = people['city'].title()
    print(full_name + " is " + str(people_age) + " years old " +
     " lives in " + people_city) 

    
    