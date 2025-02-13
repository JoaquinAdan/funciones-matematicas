import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.linspace(-5, 5, num=N)


# Función lineal
def f(x):
    return x


plt.plot(x, f(x))
plt.grid()

# Función escalón o de Heaviside


def H(x):
    Y = np.zeros(len(x))
    for idx, x in enumerate(x):
        if x >= 0:
            Y[idx] = 1
    return Y


N = 1000


y = H(x)

plt.plot(x, y)
plt.grid()


# Función sigmoide
def f(x):
    return 1 / (1 + np.exp(-x))


N = 1000

y = f(x)

plt.plot(x, y)
plt.grid()

# Función tangente hiperbólica


def f(x):
    return np.tanh(x)


N = 1000

y = f(x)

plt.plot(x, y)
plt.grid()

# Función ReLU


def f(x):
    return np.maximum(x, 0)


N = 1000

y = f(x)

plt.plot(x, y)
plt.grid()

# graficar

plt.show()
