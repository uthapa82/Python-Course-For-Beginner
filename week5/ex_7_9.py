#No pastrami.
sandwich_orders = ["veg sandwich", "tuna sandwich", "pastrami sandwich", "pastrami sandwich"]
finished_sandwich = []

print("The deli has run out of pastrami.")
while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("verifying orders: " + current_order)
    finished_sandwich.append(current_order)
    
print("\n")
print("The following sandwich have been moved to finished sandwich list:")
for j in finished_sandwich:
    print(j.title() + " was made!")   