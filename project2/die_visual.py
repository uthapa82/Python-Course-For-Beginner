import pygal as pg
from die import Die
from lxml import etree

die = Die()
die_2 = Die()

# roll the die
results = []

for roll in range(1, 1000):
    result = die.roll() + die_2.roll()
    results.append(result)

# analyze the results 
frequencies = []
for value in range(1, die.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results 
hist = pg.Bar()

hist._title = "Results of rolling on D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Results"
hist._y_title = "Count/Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file("die_visual.svg")