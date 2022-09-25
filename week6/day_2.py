# *args and **kwargs 
def my_fun(*args):
    print(args)
  
my_fun('Anup', 'Thapa', 'Anu')

def my_fun1(**kwargs):
    print(kwargs)
    if 'book' in kwargs:
        print("My favorite book is {}".format(kwargs['book']))
    else:
        print("I did not find any books")
my_fun1(book='Presence', book2='harry potter')

def combine_arguments(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Favorite number: {} Favorite book: {}".format(args[0], kwargs['book'])) 
combine_arguments(10, book='Harry Potter2', fruit='apple', shoes='nike')