#No pastrami.
print("The deli has run out of pastrami.")
sandwich_orders = ["veg sandwich", "tuna sandwich", "pastrami sandwich"]

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
print(sandwich_orders)
    