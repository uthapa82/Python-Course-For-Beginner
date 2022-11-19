import pygal as pg
from die import Die

#Rolling two eight slided dice.
die = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(10000):
    result = die.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pg.Bar()

hist._title = "Results of rolling on two d8 10000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Results"
hist._y_title = "Count/Frequency of Results"

hist.add('D8 + D8', frequencies)
hist.render_to_file("two_dice_visual.svg")