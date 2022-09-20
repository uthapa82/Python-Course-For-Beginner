def show_magicians (names):
    """Display magicians name"""
    for name in names:
        print(name)

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for mag in great_magicians:
        magicians.append(mag)

magicians = ['David', 'Porter', 'Luke']
make_great(magicians)
show_magicians(magicians)