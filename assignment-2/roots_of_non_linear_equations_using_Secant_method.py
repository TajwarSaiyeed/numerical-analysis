# Tajwar Saiyeed Abid
# 240242080

# x1 = 4
# x2 = 2

def f(x):
    return x**2 - 7 * (x**2) + 14 * x - 6 
    
def main():
    x1 = float(input())
    x2 = float(input())
    E = 0.0001

    print("Iteration x1       x2       x3       f(x1)       f(x2)")
    iteration = 1

    while True:
        f1 = f(x1)
        f2 = f(x2)

        x3 = (f2 * x1 - f1 * x2) / (f2 - f1)
        f3 = f(x3)

        print(f"        {iteration} {x1:.6f} {x2:.6f} {x3:.6f} {f1:.6f} {f2:.6f}")

        if abs((x3 - x2) / x3) < E:
            break

        x1, x2 = x2, x3
        iteration += 1

    print(f"\nApproximate root = {x3:.6f}")

if __name__ == "__main__":
    main()

# https://ideone.com/wOOk2u
# https://github.com/TajwarSaiyeed/numerical-analysis/blob/main/assignment-2/roots_of_non_linear_equations_using_Secant_method.py