# PEP 8
# Styling the code 
# dictionary 
sample_dict = {'c': 'color', 'A': 80}

#access 
print(sample_dict['c'])
print(sample_dict['A'])

sample_dict1 = {
    'Anup' : 'banepa',
    'Abhishek' : 'gorkha',
    'Abhi' : 'taplejung',
    'Upen' : 'NJ',
    
}

for key, value in sample_dict1.items():
    print('\n key: ' + key)
    print('\n value: ' + value)
    
for key, value in sample_dict1.items():
    print(key + " is from " + value)
    
for key in sample_dict1.values():
    print(key)