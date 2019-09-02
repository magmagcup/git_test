import sys
def quadratic():
    import math
    a = float(input("Enter 1st coefficient: "))
    if a != 0:
        b = float(input("Enter 2nd coefficient: "))
        c = float(input("Enter 3rd coefficient: "))
        d = ((b ** 2) - (4 * a * c))
        if d > 0:
            root1 = (((-b)+(math.sqrt(d)))/(2*a))
            root2 = (((-b)-(math.sqrt(d)))/(2*a))
            print(f"Two real roots: {root1:.3f} and {root2:.3f}")
        elif d == 0:
            root1 = -b/(2*a)
            print(f"Only one real root: {root1:.3f}")
        else:
            root1 = -b/(2*a)
            root1p = abs((math.sqrt(-d))/(2*a))
            print(f"Two complex roots: {root1:.3f}+{root1p:.3f}i and {root1:.3f}-{root1p:.3f}i")
    else:
        sys.exit(f"1st coefficient can't be zero. Program exits.")

quadratic()
