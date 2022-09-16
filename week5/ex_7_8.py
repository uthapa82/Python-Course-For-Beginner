#using while loop with list.
sandwich_orders = ["veg sandwich", "butter sadwich", "tuna sandwich"]
finished_sandwich = []

for i in sandwich_orders:
    print("i madde you " + i)
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("verifying orders: " + current_order)
    finished_sandwich.append(current_order)
print("\n")
print("The following sandwich have been moved to finished sandwich list:")
for j in finished_sandwich:
    print("\n" + j.title())
    print(j.title() + " was made!")