from random import randint

class Dice():
    """Display information about Rolling dice!"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

# six sided dice
dice_6 = Dice()

print("\nResult of 6 sided Dice")
result_6 = []
#rolls dice 10 times..
for i in range(1, 11):
    result = dice_6.roll_dice()
    result_6.append(result)

print(result_6)

# 10 sided dice
dice_10 = Dice(sides=10)

print("\nResult of 10 sided Dice")

result_10 = []
#rolls dice 10 times..
for i in range(1, 11):
    result = dice_10.roll_dice()
    result_10.append(result)

print(result_10)
# 20 sided dice 
dice_20 = Dice(sides=20)

print("\nResult of 20 sided Dice")

result_20 = []
#rolls dice 10 times..
for i in range(1, 11):
    result = dice_20.roll_dice()
    result_20.append(result)

print(result_20)