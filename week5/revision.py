def animal(animal_name, animal_type, animal_age = ""):
    """Display information about animals"""
    print(animal_name.title() + " is the king of the jungle" + ".")
    print(animal_name.title() + " is " + animal_type.title() + " aniaml" + ".")

animal('lion', 'wild')  #positonal arguments.
animal('cow', 'domestic')#using multiple function call.
animal('dog', 'domestic')
animal(animal_name= 'lion', animal_type= 'wild') # Using keyword arguments.
