import matplotlib.pyplot as plt

import pygal as pg

from die import Die

die = Die()
die_2 = Die()

results = []
for i in range(10000):
    result = die.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pg.Bar()

hist._title = "Results of rolling on two D6 10000 times using matplotlib."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Results"
hist._y_title = "Count/Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file("exercise_15_10.svg")