#ex_9_12.py
from adminn import Admin

user_0 = Admin('Elon', 'Musk', 36, 'CEO')
user_0.describe_user()

print("\n" + "privileges:")
user_0_privileges = [
    "can add post", 
    "can delete post", 
    "can ban user"
] 

user_0.privileges.privileges = user_0_privileges
user_0.privileges.show_priviliges()
