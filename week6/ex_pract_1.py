def foo_bar(n):
    for i in range(1, n):
        if i %3 == 0 and i %5 == 0:
            print("foo bar")

        if i % 3 == 0:
            print("foo")
        
        if i %5 == 0:
            print("bar")
            
foo_bar(n=13)
