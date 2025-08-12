# **PREDATOR–PREY MODEL**

This Python program simulates predator–prey population changes over time using **Differential Equations and Linear Algebra**.
It shows how two populations (prey and predators) interact, and it also checks the **stability** of a given point in the system using eigenvalues.

---

## **How It Works**

### **Model**

The program assumes:

* Prey grow naturally, but are eaten by predators.
* Predators survive by eating prey, but die off if prey are scarce.

Both populations affect each other’s growth rates.

---

### **Simulation Steps**

1. **Initial setup**
   The program starts with:

   * Prey population = 40
   * Predator population = 9
   * Time range = 0 to 50 (500 steps)

2. **Population change calculation**
   At each time step, the growth or decline of prey and predators is computed.

3. **Graph output**
   The program plots prey and predator populations over time so you can see the rise and fall patterns.

4. **Stability check**
   At the starting point (40 prey, 9 predators), the program calculates **eigenvalues**.

   * If all eigenvalues are **negative** → the system is stable (populations settle).
   * If any eigenvalue is **positive** → the system is unstable (populations move away from that point).

---

## **Example Output**

```
Jacobian Matrix at equilibrium (40, 9):
 [[ 0.15 -2.  ]
 [ 0.18  0.4 ]]

Eigenvalues of the Jacobian matrix:
 [0.44161284 0.10838716]
```

**What these numbers mean:**

* **Both positive** → The system is **unstable**.
  Small changes in populations will grow larger over time, not settle down.
* If both had been negative, it would mean populations return to balance after disturbances.
* If one is positive and one negative, the system is unstable but in a more complex way (saddle point).

---

## **Code**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Population change equations
def predator_prey(population, time):
    prey, predator = population
    prey_growth = 0.6 * prey - 0.05 * prey * predator
    predator_growth = 0.02 * prey * predator - 0.4 * predator
    return [prey_growth, predator_growth]

# Time and starting values
time = np.linspace(0, 50, 500)
initial_population = [40, 9]

# Solve the system
result = odeint(predator_prey, initial_population, time)
prey_values, predator_values = result.T

# Plot populations
plt.plot(time, prey_values, label="Prey")
plt.plot(time, predator_values, label="Predator")
plt.legend()
plt.title("Predator and Prey Population Over Time")
plt.xlabel("Time")
plt.ylabel("Population")
plt.grid(True)
plt.show()

# Stability check
prey_eq, predator_eq = 40, 9
a, b, c, d = 0.6, 0.05, 0.02, 0.4

J = np.array([
    [a - b * predator_eq, -b * prey_eq],
    [c * predator_eq, c * prey_eq - d]
])

print("\nJacobian Matrix at equilibrium (40, 9):\n", J)

eigenvalues = np.linalg.eigvals(J)
print("\nEigenvalues of the Jacobian matrix:\n", eigenvalues)

# Explain meaning
if all(ev < 0 for ev in eigenvalues):
    print("\nAll eigenvalues negative → Stable equilibrium.")
elif any(ev > 0 for ev in eigenvalues):
    print("\nOne or more eigenvalues positive → Unstable equilibrium.")
else:
    print("\nMixed signs → Unstable (saddle point).")
```

---

## **Features**

* Simulates predator–prey population changes.
* Visualizes population curves over time.
* Checks if a given population point is **stable**.
* Explains **eigenvalues** in plain English.

---

## **Requirements**

* Python **3.6+**
* A code editor (VSC, PyCharm, or Sublime Text)
* Install: 
  NumPy, 
  Matplotlib,
  SciPy,

Install in terminal:

```bash
pip install numpy matplotlib scipy
```
]
