# import matplotlib.pyplot as plt

# x = range(1, 6)
# x_values = y_values = [a**3 for a in x]
# plt.style.use("seaborn-v0_8")
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# plt.show()

import matplotlib.pyplot as plt

x = range(1, 5001)
x_values = y_values = [a**3 for a in x]
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, 10)

plt.show()
