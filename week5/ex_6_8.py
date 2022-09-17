suri = {
    'animal_kind': 'cat',
    'owner': 'Abhijeet',
    }
kali = {
    'animal_kind': 'rat',
    'owner': 'Anishma',
    }
khaire = {
    'animal_kind': 'dog',
    'owner': 'Anup',
    }

pets_list = [suri, kali, khaire]
#lopping through the list.
for animals in pets_list:
    print(animals['owner'] + " has a " + animals['animal_kind'])
    for k, v in animals.items():
        print("\t" + k + "have a " + v)

