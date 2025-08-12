import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# differential Equation 
def predator_prey(population, time):
    prey, predator = population
    prey_growth = 0.6 * prey - 0.05 * prey * predator
    predator_growth = 0.02 * prey * predator - 0.4 * predator
    return [prey_growth, predator_growth]

# declaring data
time = np.linspace(0, 50, 500)
initial_population = [40, 9] 


result = odeint(predator_prey, initial_population, time)
prey_values, predator_values = result.T

# plotting
plt.plot(time, prey_values, label="Prey")
plt.plot(time, predator_values, label="Predator")
plt.legend()
plt.title("Predator and Prey Population Over Time")
plt.xlabel("Time")
plt.ylabel("Population")
plt.grid(True)
plt.show()

# linear Algebra - Jacobian Matrix
prey_eq, predator_eq = 40, 9

# constants
a = 0.6
b = 0.05
c = 0.02
d = 0.4

# Jacobian Matrix
J = np.array([
    [a - b * predator_eq, -b * prey_eq],
    [c * predator_eq, c * prey_eq - d]
])

print("\nJacobian Matrix at equilibrium (40, 9):\n", J)

# Eigenvalues - tells the system stability
eigenvalues = np.linalg.eigvals(J)
print("\nEigenvalues of the Jacobian matrix:\n", eigenvalues)

# Eigenvalues meaning:
    # both negative → stable
    # any positive → unstable
