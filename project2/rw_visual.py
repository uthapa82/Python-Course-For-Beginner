import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize =(20, 12))

    point_number = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=120)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=115)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break