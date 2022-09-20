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
    
    return magicians

magicians = ['David', 'Porter', 'Luke']
show_magicians(magicians)

print("\n Modified list (added great ):")
great_magician = make_great(magicians[:])
show_magicians(great_magician)

print("\n Original:")
show_magicians(magicians)
