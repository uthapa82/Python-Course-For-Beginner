family = ['ram', 'anup', 'anu', 'abhi', 'ram', 'ram', 'ram']
full_family = []

# while family:
#     current_member = family.pop()
#     print("Full family :" +  current_member.title())
#     full_family.append(current_member)
#     print("\n The follwing members have been added....")
    
#     for member in full_family:
#         print(member.title())

while 'ram' in family:
    family.remove('ram')

print(family)