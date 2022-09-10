user = ['admin', 'akabhi']
if user:
    for i in user:
        if i == 'admin':
            print("hello " + i + " would you like to see a status report?")
    
        else:
            print("hello " + i + " thank you for logging in again")
else:
    print("we need to find some users")