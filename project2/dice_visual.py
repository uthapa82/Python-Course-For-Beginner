import pygal as pg
from die import Die

#Rolling two dice.
die = Die()
die_2 = Die()

result = die.roll() + die_2.roll()
results = [result for roll_num in range(1000)]

max_result = die.num_sides + die_2.num_sides 
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pg.Bar()

hist._title = "Results of rolling on two D6 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Results"
hist._y_title = "Count/Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file("dice_visual.svg")