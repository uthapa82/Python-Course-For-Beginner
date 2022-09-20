def foo_bar(int_n):
    """print numbers"""
    print("\n" + str(int_n))
    
    if int_n % 3 == 0:
        print("foo")
    
    if int_n %5 == 0:
        print("bar")
    
    if int_n %3 %5 == 0:
        print("foo bar")

foo_bar(int_n = 12)