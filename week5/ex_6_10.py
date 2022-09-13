fav_no = {
    'Abhishek': 1, 
    'Abhi': 2, 
    'anu': 3, 
    'anusha': 4, 
    'anup': 5,
    }

fav_no["Abhishek"] = [5, 6]
fav_no["Abhi"] = [3, 4]
fav_no["anu"] = [5, 6]
fav_no["anusha"] = [6, 7]
fav_no["anup"] = [7, 8]
print(fav_no)

for name, no in fav_no.items():
    print(name + " favorite no is:" + str(no))
    