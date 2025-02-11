import matplotlib.pyplot as plt  # librería para graficar
import numpy as np  # librería para manejo de vectores y utilidades matemáticaspip install matplotlib

N = 100

m = 10

b = -4


def f(x):
    return m * x + b


x = np.linspace(-10, 10, num=N)
print(x)
# print(x.shape)  # (100,) es un vector de 100 elementos

y = f(x)

# print(y.shape)  # (100,) es un vector de 100 elementos

fig, ax = plt.subplots()  # ax == axis == ejes
ax.plot(x, y)
ax.grid()

# print
plt.show()
