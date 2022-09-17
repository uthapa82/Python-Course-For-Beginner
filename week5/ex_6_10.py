fav_no = {
    'Abhishek': [5, 6], 
    'Abhi': [3, 4], 
    'anu': [5, 6], 
    'anusha': [6, 7],
    'anup': [7, 8],
    }
for name, no in fav_no.items():
    print(name + " favorite no is:")
    for numbers in no:
        print("\t - " + str(numbers)) 
    