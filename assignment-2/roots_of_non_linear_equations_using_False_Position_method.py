# Tajwar Saiyeed Abid
# ID: 240242080


# starting interval [1, 3].
# f(x) = x3 − 4


def f(x):
    return x**3 - 4

def main():
    x1 = 1.0
    x2 = 3.0
    E = 1e-8

    f1 = f(x1)
    f2 = f(x2)

    if f1 * f2 > 0:
        print("The chosen interval does not bracket any root.")
        return

    print("Iteration |     x0   |     x1   |     x2   |     f0   |     f1   |     f2   ")
    print("----------------------------------------------------------------------------")

    for i in range(1, 4):
        x0 = x1 - (f1 * (x2 - x1)) / (f2 - f1)
        f0 = f(x0)

        print(f"      {i:3d} | {x0: .5f} | {x1: .5f} | {x2: .5f} | {f0: .5f} | {f1: .5f} | {f2: .5f}")

        if f0 == 0:
            print(f"\nApproximate root : {x0}")
            break

        if f1 * f0 < 0:
            x2 = x0
        else:
            x1 = x0
            
        if abs((x2 - x1) / x2) < E:
            break

    root = (x1 + x2) / 2
    print(f"\nApproximate root : {root}")

if __name__ == "__main__":
    main()


# https://ideone.com/rgAEop
# https://github.com/TajwarSaiyeed/numerical-analysis/blob/main/assignment-2/roots_of_non_linear_equations_using_False_Position_method.py