import matplotlib.pyplot as plt  # librería para graficar
import numpy as np  # librería para manejo de vectores y utilidades matemáticas


def H(x):
    Y = np.zeros(len(x))
    for idx, val in enumerate(x):
        if val >= 0:
            Y[idx] = 1
    return Y


N = 1000

x = np.linspace(-10, 10, num=N)

y = H(x)

plt.plot(x, y)
plt.grid()
plt.show()
