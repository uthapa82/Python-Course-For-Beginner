def pizza(*topping):
    print(topping)
    for top in topping:
        print("-" + top)

pizza('cheesi')
pizza('mushroom', 'cheese')