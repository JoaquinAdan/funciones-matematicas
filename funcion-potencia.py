import matplotlib.pyplot as plt  # librería para graficar
import numpy as np  # librería para manejo de vectores y utilidades matemáticaspip install matplotlib

N = 100
x = np.linspace(-10, 10, num=N)


def f(x):
    return x**7


y = f(x)

plt.plot(x, y)
plt.grid()
plt.show()
