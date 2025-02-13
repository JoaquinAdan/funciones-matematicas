import numpy as np
import matplotlib.pyplot as plt


# Función Par (Simétrica respecto al eje Y)
def funcion_par(x):
    return x**2


# Función Impar (Simétrica respecto al origen)
def funcion_impar(x):
    return x**3


# Función Periódica (Ejemplo: Seno)
def funcion_periodica(x):
    return np.sin(x)


# Función Acotada (Ejemplo: Seno, acotado en [-1,1])
def funcion_acotada(x):
    return np.sin(x)


# Función Monótona (Ejemplo: Creciente: y = 2x)
def funcion_monotona(x):
    return 2 * x


# Función Cóncava y Convexa (Ejemplo: y = x^2 cambia de convexa a cóncava en x=0)
def funcion_concava_convexa(x):
    return x**2


# Rango de valores para x
x = np.linspace(-10, 10, 400)

# Evaluar funciones
y_par = funcion_par(x)
y_impar = funcion_impar(x)
y_periodica = funcion_periodica(x)
y_acotada = funcion_acotada(x)
y_monotona = funcion_monotona(x)
y_concava_convexa = funcion_concava_convexa(x)

# Crear subgráficos
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Gráfica de función par
axes[0, 0].plot(x, y_par, label="y = x²", color="b")
axes[0, 0].set_title("Función Par")
axes[0, 0].grid()
axes[0, 0].legend()

# Gráfica de función impar
axes[0, 1].plot(x, y_impar, label="y = x³", color="g")
axes[0, 1].set_title("Función Impar")
axes[0, 1].grid()
axes[0, 1].legend()

# Gráfica de función periódica
axes[0, 2].plot(x, y_periodica, label="y = sin(x)", color="r")
axes[0, 2].set_title("Función Periódica")
axes[0, 2].grid()
axes[0, 2].legend()

# Gráfica de función acotada
axes[1, 0].plot(x, y_acotada, label="y = sin(x)", color="m")
axes[1, 0].set_title("Función Acotada")
axes[1, 0].grid()
axes[1, 0].legend()

# Gráfica de función monótona
axes[1, 1].plot(x, y_monotona, label="y = 2x", color="c")
axes[1, 1].set_title("Función Monótona")
axes[1, 1].grid()
axes[1, 1].legend()

# Gráfica de función cóncava y convexa
axes[1, 2].plot(x, y_concava_convexa, label="y = x²", color="y")
axes[1, 2].set_title("Función Cóncava y Convexa")
axes[1, 2].grid()
axes[1, 2].legend()

# Ajustar diseño y mostrar gráfico
plt.tight_layout()
plt.show()
