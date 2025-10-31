# OBJECTIVES: To find the roots of non linear equations using Newton-Raphson method.
# ALGORITHM:
# 1. Assign an initial value for x, say x0 and stopping criterion E.
# 2. Compute f (x0) and f ‘(x0).
# 3. Find the improved estimate of x0
# x1 = x0 – f (x0) / f ’(x0)
# 4. Check for accuracy of the latest estimate.
# If | (x1-x0)/x1| < E then stop; otherwise continue.
# 5. Replace x0 by x1 and repeat steps 3 and 4.
# Sample Input/output:
# ENTER THE TOTAL NO. OF POWER:::: 3
# x^0::-3
# x^1::-1
# x^2::0
# x^3::1
# THE POLYNOMIAL IS ::: 1x^3 0x^2 -1x^1 -3x^0
# INTIAL X1 ------ >3
# **************************************
# ITERATION
# X1
# FX1
# F'X1
# **************************************
# 1
# 2.192 21.000 26.000
# 2
# 1.794 5.344 13.419
# 3
# 1.681 0.980 8.656
# 4
# 1.672 0.068 7.475
# 5
# 1.672 0.000 7.384
# **************************************
# THE ROOT OF EQUATION IS 1.671700
# Tasks:
# Write a program to perform all iterations of the Newton-Raphson method using Horner’s
# rule for any function. Show the table with iterations, values, errors and percentage errors
# of all variables.


def main():
    def f(x, coeffs):
        result = 0
        for power, coeff in enumerate(coeffs):
            result += coeff * (x ** power)
        return result

    def f_prime(x, coeffs):
        result = 0
        for power, coeff in enumerate(coeffs[1:], start=1):
            result += power * coeff * (x ** (power - 1))
        return result

    n = int(input("ENTER THE TOTAL NO. OF POWER:::: "))
    coeffs = []
    for i in range(n + 1):
        coeff = float(input(f"x^{i}::"))
        coeffs.append(coeff)

    print("THE POLYNOMIAL IS ::: ", end="")
    for power, coeff in enumerate(coeffs):
        print(f"{coeff}x^{power} ", end="")
    print()

    x0 = float(input("INTIAL X1 ------ >"))
    E = 0.0001
    iteration = 0

    print("**************************************")
    print("ITERATION\tX1\tFX1\tF'X1")
    print("**************************************")

    while True:
        iteration += 1
        fx0 = f(x0, coeffs)
        fpx0 = f_prime(x0, coeffs)
        x1 = x0 - fx0 / fpx0

        print(f"{iteration}\t{x1:.3f}\t{fx0:.3f}\t{fpx0:.3f}")

        if abs((x1 - x0) / x1) < E:
            break
        x0 = x1

    print("**************************************")
    print(f"THE ROOT OF EQUATION IS {x1:.6f}")



if __name__ == "__main__":
    main()