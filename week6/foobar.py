def foo_bar(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FooBar')
        elif i % 3 == 0:
            print('Foo')
        elif i % 5 == 0:
            print('Bar')
        else:
            print(i)

def main():
    user_input = int(input("Please enter the number(n): "))
    foo_bar(user_input)
    
if __name__ == '__main__':
    main()