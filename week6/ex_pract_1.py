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