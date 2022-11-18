import pygal as pg
from die import Die

#Roll one  dice.
die = Die()

#using list comprehensive.
results = [die.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range (1, die.num_sides+1)]

# visualize the results 
hist = pg.Bar()

hist._title = "Results of rolling on D6 1000 times."
hist.x_labels = [str(x) for x in range(1, die.num_sides+1) ]
hist.x_title = "Results"
hist._y_title = "Count/Frequency of Results"

hist.add('D6', frequencies)
hist.render_to_file("diee_visual.svg")