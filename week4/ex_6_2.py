#using dictonary 
#2nd step print each person name and their favroite numbers
fav_no = {
    'Abhishek': 1, 
    'Abhi': 2, 
    'anu': 3, 
    'anusha': 4, 
    'anup': 5,
    } 
#print(fav_no["Abhishek"])
#print("Abhi favorite number is " + str(fav_no['Abhishek']))
#print(fav_no["Abhi"])
#print(fav_no["anu"])
#print(fav_no["anusha"])
#print(fav_no["anup"])

#using forloop.
for key, value in fav_no.items():
    print(key + " favroite number is " + value)