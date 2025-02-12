import numpy as np
import matplotlib.pyplot as plt


# Definir funciones
def par(x):
    return x**2  # Ejemplo de función par (parábola)


def impar(x):
    return x**3  # Ejemplo de función impar (cúbica)


# Rango de valores
x = np.linspace(-10, 10, 400)

# Evaluar funciones
y_par = par(x)
y_impar = impar(x)

# Crear subgráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfica de función par
axes[0].plot(x, y_par, label="y = x²", color="b")
axes[0].axhline(0, color="k", linewidth=1)
axes[0].axvline(0, color="k", linewidth=1)
axes[0].set_title("Función Par (Simétrica respecto al eje Y)")
axes[0].grid()
axes[0].legend()

# Gráfica de función impar
axes[1].plot(x, y_impar, label="y = x³", color="g")
axes[1].axhline(0, color="k", linewidth=1)
axes[1].axvline(0, color="k", linewidth=1)
axes[1].set_title("Función Impar (Simétrica respecto al origen)")
axes[1].grid()
axes[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()
