import numpy as np
import matplotlib.pyplot as plt

N = 1000


def f(x):
    return np.sin(x)


c = 0.1

x = np.linspace(-15, 15, num=N)

# y = f((1 / c) * x)
# y = 15 * f(x)
y = f(x * 15)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color="r")
ax.axvline(x=0, color="r")

plt.show()
