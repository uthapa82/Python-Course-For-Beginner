#TODO
rivers = {
    "Bishnumati": "Machhapokhari",
    "Hang Ho": "China",
    "Nile": "Egypt"
}

for k, v in rivers.items():
    print(k + " river " + "runs through " + v + ".")
    
print("\nThe following rivers are included in the data: ")
for key, value in rivers.items():
    print("- " +key + " river.")
    
print("\nThe following countries are included in the data: ")
for key, value in rivers.items():
    print("- " + value)
    
     