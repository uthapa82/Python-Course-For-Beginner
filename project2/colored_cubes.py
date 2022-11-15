import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.title("x_value", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("cube of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

plt.show()