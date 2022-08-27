guests = ["Abhishek", "Anu", "Abhijeet", "Upendra", "Anup", "Abhi"]
print("sorry i can invite only two people for dinner")
guests.pop(1)
guests.pop(2)
guests.pop(3)

print(guests)
print("I'm sorry guys i can't invite all of you to dinner")
print(guests[0] + " " + guests[1] + " Only you two are invited for dinner")
del guests
