# Tajwar Saiyeed Abid
# 240242080

# Horner rule = a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0 

# Total No. of Power = 3

# x^3 = 3
# x^2 = -1
# x^1 = 0
# x^0 = 1

# Initial X1 = 3


def horner(coefficients, x):
    result = coefficients[0]
    for coeff in coefficients[1:]:
        result = result * x + coeff
    return result


def main():
    degree = 3
    x_0 = -3
    x_1 = -1
    x_2 = 0
    x_3 = 1

    coefficients = [x_3, x_2, x_1, x_0]

    print("THE POLYNOMIAL IS ::: ", end="")
    for i in range(degree, -1, -1):
        print(f"{coefficients[-(i + 1)]}x^{i} ", end="")
    print()

    x0 = 3
    E = 0.0001
    max_iterations = 1000

    print("**************************************")
    print("ITERATION    X1    FX1     F'X1")
    print("**************************************")
    iteration = 1
    while iteration <= max_iterations:
        fx0 = horner(coefficients, x0)

        derivative_coeffs = [coefficients[i] * (degree - i) for i in range(degree)]


        f_x0 = horner(derivative_coeffs, x0)

        if abs(f_x0) < 1e-10:
            return

        x1 = x0 - fx0 / f_x0

        print(f"        {iteration}   {x1:.3f}  {fx0:.3f}   {f_x0:.3f}")

        if abs((x1 - x0) / x1) < E: 
            break

        x0 = x1
        iteration += 1
    
    if iteration > max_iterations:
        return
        
    print("**************************************")
    print(f"THE ROOT OF EQUATION IS {x1:.6f}")
    

if __name__ == "__main__":
    main()


# https://ideone.com/otZXs2