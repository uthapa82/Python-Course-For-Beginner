<<<<<<< HEAD
def foo_bar(n):
    for i in range(1, n):
        if i %3 == 0 and i %5 == 0:
            print("foo bar")

        if i % 3 == 0:
            print("foo")
        
        if i %5 == 0:
            print("bar")
            
foo_bar(n=13)
=======
def foo_bar(int_n):
    for num in range(1, int_n):
        if num % 3 == 0:
            print("foo")
        if num %5 == 0:
            print("bar")
        if num %3 == 0 and num %5 == 0:
            print("foobar")
        else:
            print(num)

foo_bar(int_n = 16)
>>>>>>> 926d130a7f77bc4a71eb0539d026be395361b8b1
