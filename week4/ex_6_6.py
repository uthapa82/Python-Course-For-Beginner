peoples = {
    "Anu": "poll",
    "Abhishek": "English",
    "Anusha": "poll"}

for key, value in peoples.items():
    if key == "Anu":
        print("\nkey:" + key + " Thank you for responding")
    elif key == "Anusha":
        print("key:" + key + " thank you for responding")
    else:
        print("you are invited to take a poll")