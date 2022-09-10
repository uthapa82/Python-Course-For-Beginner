current_users = ["Ram", "shyam", "om", "Hari", "Gita"]
new_users = ["Abhi", "Abhijeet", "Shyam", "Anu", "RAM"]

current_users_lower = [users.lower() for users in current_users]

for i in new_users:
    if i.lower() in current_users_lower:
        print(f"{i} is not available, you need to enter a new user name")

    else:
        print(f"{i}, user name is available ")

