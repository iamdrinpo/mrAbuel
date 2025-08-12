# **BISECTION METHOD — Root Finding**

This Python program implements the **Bisection Method** to approximate the root of a given mathematical function.
In this example, the function is:

$$
f(x) = x^3 - x - 2
$$

The method works by repeatedly halving an interval that contains the root until the interval is smaller than a specified **tolerance**.

---

## **How It Works**

1. **User Input**

   * Inputs:

     * **Starting point `a`** — lower bound of the interval.
     * **Ending point `b`** — upper bound of the interval.
     * **Tolerance** — maximum allowed error for the root approximation.

2. **Validation**

   * The program first checks:

     ```python
     if f(a) * f(b) >= 0:
         print("No root found. f(a) and f(b) must have opposite signs.")
         return
     ```
   * This ensures `f(a)` and `f(b)` have **opposite signs**, meaning a root lies between them.
   * If they don’t, the method stops immediately because a root is **not guaranteed** in the given range.

3. **Bisection Iterations**

   * The midpoint of the current interval is calculated as:

$$
\text{mid} = \frac{a + b}{2}
$$

   * If `f(mid) = 0`, an exact root is found.

   * Otherwise, the interval is replaced with the half that contains the root.

   * The process repeats until the stopping condition is met.

4. **Stopping Condition**

   * The iterations stop when the interval width `(b - a)` is **less than** the given tolerance.

5. **Output**

   * The program prints the **approximate root** found.

---

## **Example Usage**

### **Example 1**

```
This program finds the root of the function: f(x) = x^3 - x - 2
Enter the starting point a: 1
Enter the ending point b: 2
Enter the tolerance (e.g., 0.01): 0.001
Root is approximately: 1.521484375
```

**Explanation:**

* The sign of `f(x)` changes between `x = 1` and `x = 2`, so a root exists there.
* The method narrows down the range until the result is accurate to within `0.001`.

---

## **Code**

```python
def f(x):
    return x**3 - x - 2  # test function

def bisection(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("No root found. f(a) and f(b) must have opposite signs.")
        return

    while (b - a) > tolerance:
        mid = (a + b) / 2

        if f(mid) == 0:
            break

        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    print("Root is approximately:", mid)

print("This program finds the root of the function: f(x) = x^3 - x - 2")

a = float(input("Enter the starting point a: "))
b = float(input("Enter the ending point b: "))
tolerance = float(input("Enter the tolerance (e.g., 0.01): "))

bisection(a, b, tolerance)
```

---

## **Features**

* Implements the **Bisection Method** for root finding.
* Works with **any continuous function** (modify `f(x)` as needed).
* Includes a **sign check** to ensure a valid interval before starting.
* Stops automatically when the root is found within the given tolerance.

---

## **Requirements**

* Python 3.6+ installed on your system.
* A code editor or IDE (e.g., VS Code, PyCharm, Sublime Text) or simply the Python IDLE.
* No external libraries required — uses only Python built-ins.
