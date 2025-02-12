import numpy as np
import matplotlib.pyplot as plt

# N = 1000


# def f(x):
#     return x**2


# c = 4
# x = np.linspace(-10, 10, num=N)

# # Definir las cuatro funciones
# y1 = f(x - c)
# y2 = f(x + c)
# y3 = f(x) - c
# y4 = f(x) + c

# # Crear la figura con subgráficos
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# # Lista de datos y títulos
# functions = [
#     (y1, "y = f(x - c)"),
#     (y2, "y = f(x + c)"),
#     (y3, "y = f(x) - c"),
#     (y4, "y = f(x) + c"),
# ]

# # Dibujar cada gráfico en su respectivo subplot
# for ax, (y, title) in zip(axes.flat, functions):
#     ax.plot(x, y)
#     ax.grid()
#     ax.axhline(y=0, color="r", linestyle="--")
#     ax.axvline(x=0, color="r", linestyle="--")
#     ax.set_title(title)

# # Ajustar el layout
# plt.tight_layout()
# plt.show()

N = 1000


def f(x):
    return x**2


c = 4

x = np.linspace(-10, 10, num=N)

y = f(x + c)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color="r")
ax.axvline(x=0, color="r")

plt.show()
