import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x[0]**2 + x[1]**2 + x[2]**2 - 2*x[0]*x[1] + 3*x[2]

def grad_f(x):
  return np.array([2*x[0] - 2*x[1], 2*x[1] - 2*x[0], 2*x[2] + 3])

# Parámetros iniciales
x0 = np.array([1, 1, 1])
alpha = 0.1
num_iter = 15

# Lista para almacenar los valores de la función en cada iteración
f_values = []

# Algoritmo de descenso del gradiente
x = x0.copy()
for i in range(num_iter):
  f_values.append(f(x))
  x = x - alpha * grad_f(x)

print("Valor mínimo aproximado:", f(x))
print("Punto mínimo aproximado:", x)

plt.plot(range(num_iter), f_values)
plt.xlabel("Iteración")
plt.ylabel("Valor de f(x)")
plt.title("Evolución del valor de la función")
plt.show()