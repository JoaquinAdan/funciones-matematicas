import matplotlib.pyplot as plt  # librería para graficar
import numpy as np  # librería para manejo de vectores y utilidades matemáticaspip install matplotlib

N = 1000
x = np.linspace(0.001, 256, num=N)


def f(x):
    return np.log2(x)


y = f(x)

plt.plot(x, y)
plt.grid()
plt.show()
