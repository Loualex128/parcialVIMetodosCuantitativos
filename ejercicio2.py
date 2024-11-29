from scipy.optimize import minimize
import numpy as np

# Definimos la función de costos
def objective(x):
    return 5*x[0]**2 + 3*x[1]**2 + x[2]**2

# Definimos la restricción de igualdad
def constraint(x):
    return x[0] + x[1] + x[2] - 100

# Establecemos los límites de las variables (opcional, si se conocen)
bounds = ((0, None), (0, None), (0, None))  # x, y, z deben ser no negativos

# Creamos la restricción
con = {'type': 'eq', 'fun': constraint}

# Establecemos un punto inicial (opcional)
x0 = np.array([33.33, 33.33, 33.33])  # Un punto inicial razonable

# Resolvemos el problema
sol = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=con)

# Imprimimos la solución
print("Valores óptimos: x =", sol.x[0], ", y =", sol.x[1], ", z =", sol.x[2])
print("Costo mínimo:", sol.fun)