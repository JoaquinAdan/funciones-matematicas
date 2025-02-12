import numpy as np
import matplotlib.pyplot as plt

N = 1000


def f(x):
    return x**3


x = np.linspace(-10, 10, num=N)

y = f(-x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color="r")
ax.axvline(x=0, color="r")

plt.show()
