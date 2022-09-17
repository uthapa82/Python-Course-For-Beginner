favorite_place = {
    'Anu': ['pokhara'],
    'Anup': ['bhaktapur', 'kathmandu'],
    'Anuhsa': ['mustang', 'illam', 'chitwan'],
}
#favorite_place['Anu'] = "lakesite"
for name, place in favorite_place.items():
    print("\n" + name + "'s favorite place is: ")

    for location in place:
        print("\t" +"* " + location.title() + ".")