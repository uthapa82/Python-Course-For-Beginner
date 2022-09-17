favorite_place = {
    'Anu': ['pokhara', 'Banepa'],
    'Anup': ['bhaktapur', 'kathmandu'],
    'Anuhsa': ['mustang', 'Manang'],
    }
for name, place in favorite_place.items():
    print(name + " likes following places:")
    for location in place:
        print("\t * " + location)