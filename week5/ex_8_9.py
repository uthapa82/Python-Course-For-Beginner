def show_magicians (names):
    """Display magicians name"""
    for name in names:
        megician = "hello, " + name.title() + "."
        print(megician)
magician = ["Abhi", "Anup", "Anup"]
show_magicians(magician)