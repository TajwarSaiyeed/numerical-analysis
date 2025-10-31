def main():
    x1 = 0
    x2 = 1

    E = 10**-8
    f1 = f(x1)
    f2 = f(x2)

    if f1 * f2 > 0:
        print("No root found")
        return

    iteration = 0
    while True:
        x0 = (x1 + x2) / 2
        f0 = f(x0)

        print(f"Iteration\n{iteration}")
        iteration += 1

        print(f"x0: {x0}\nx1: {x1}\nx2: {x2}\nf0: {f0}\nf1: {f1}\nf2: {f2}")

        if f0 == 0:
            print("Root found:", x0)
            return

        if f1 * f0 < 0:
            x2 = x0
        else:
            x1 = x0

        if abs((x2 - x1) / x2) < E:
            root = (x1 + x2) / 2
            print("Root found:", root)
            return

def f(x):
    return 2 *( x **3 )+ (3 * x) -1

if __name__ == "__main__":
    main()