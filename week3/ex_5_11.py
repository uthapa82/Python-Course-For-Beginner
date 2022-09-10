ordinal_no = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
for i in ordinal_no:
    print(i)
    if i == '1':
        print("1st")
    elif i == '2':
        print("2nd")
    elif i == '3':
        print("3rd")
    else:
        print(i + "th")