import pygal as pg
from die import Die


#Rolling three six slided dice.
die = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(100000):
    result = die.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# results = [die.roll() + die_2.roll() for roll_num in range(100000)]

frequencies = []
max_result = die.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#frequencies =[results.count(value) for value in range(3, max_result+1)]

hist = pg.Bar()

hist._title = "Results of rolling on two d8 100000 times."
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.x_title = "Results"
hist._y_title = "Count/Frequency of Results"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file("three_dice_visual.svg")