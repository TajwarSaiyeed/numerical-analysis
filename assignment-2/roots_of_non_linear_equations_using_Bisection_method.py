# Tajwar Saiyeed Abid
# ID: 240242080

# starting interval [0, 1]
# tolerance level 10^-8
# function f(x) = 2x3 + 3x − 1

def f(x):
    return 2*x**3 + 3*x - 1


def main():
    x1 = 0.0
    x2 = 1.0
    E = 1e-8

    f1 = f(x1)
    f2 = f(x2)

    if f1 * f2 > 0:
        print("The chosen interval does not bracket any root.")
        return

    i = 0

    print("Iteration |     x0   |     x1   |     x2   |     f0   |     f1   |     f2   ")
    print("----------------------------------------------------------------------------")

    while True:
        i += 1
        x0 = (x1 + x2) / 2
        f0 = f(x0)

        print(f"      {i:3d} | {x0: .5f} | {x1: .5f} | {x2: .5f} | {f0: .5f} | {f1: .5f} | {f2: .5f}")


        if f0 == 0:
            print(f"\nApproximate root : {x0}")
            break

        if f1 * f0 < 0:
            x2 = x0
            f2 = f0
        else:
            x1 = x0
            f1 = f0

        if abs((x2-x1) / x2) < E:
            root = (x1 + x2) / 2
            print(f"\nApproximate root : {root}")
            break

if __name__ == "__main__":
    main()


# https://ideone.com/sHn7lK
