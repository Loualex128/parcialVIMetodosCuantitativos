import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 4*x + 5

# Generamos un rango de valores para x dentro de las restricciones
x = np.linspace(2, 5, 100)

# Evaluamos la función en cada valor de x
y = f(x)

# Encontramos el índice del valor mínimo
min_index = np.argmin(y)
min_x = x[min_index]
min_y = y[min_index]

# Graficamos la función
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Minimización de f(x) con restricciones')

# Agregamos líneas verticales para las restricciones
plt.axvline(x=2, color='r', linestyle='--')
plt.axvline(x=5, color='r', linestyle='--')

# Marcamos el punto mínimo
plt.scatter(min_x, min_y, color='red', marker='o')

plt.show()

print("El valor mínimo de la función es", min_y, "y se alcanza en x =", min_x)