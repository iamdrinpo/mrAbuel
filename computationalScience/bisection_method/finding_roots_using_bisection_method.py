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
