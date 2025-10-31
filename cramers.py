def determinant(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        submatrix = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            submatrix.append(row)
        
        det += ((-1) ** j) * matrix[0][j] * determinant(submatrix)
    
    return det

def cramers_rule(matrix):
    # Validate input: expect an augmented matrix with n rows and n+1 columns
    if not matrix:
        print("Input matrix is empty")
        return

    n = len(matrix)

    # Every row must have n+1 elements (n coefficients + 1 constant)
    for idx, row in enumerate(matrix):
        if len(row) != n + 1:
            print(f"Invalid input: row {idx} has length {len(row)} but expected {n+1} (augmented matrix with n+1 columns).")
            return

    A = [row[:n] for row in matrix]
    b = [row[n] for row in matrix]
    
    det_A = determinant(A)
    
    if det_A == 0:
        print("No unique solution exists (determinant is 0)")
        return
    
    solutions = []
    for i in range(n):
        A_i = [row[:] for row in A]  # Deep copy
        for j in range(n):
            A_i[j][i] = b[j]
        
        x_i = determinant(A_i) / det_A
        solutions.append(x_i)
    
    return solutions

def main():
    row, col = map(int, input().split())

    matrix = []
    for i in range(row):
        vals = list(map(int, input().split()))
        if len(vals) != col:
            print(f"Invalid input: row {i} has length {len(vals)} but expected {col} columns.")
            return
        matrix.append(vals)

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()

    # If user provided only the coefficient matrix (n x n), prompt for constants
    if col == row:
        print(f"Detected {row}x{col} coefficient matrix without constants.")
        print(f"Enter {row} constants (space-separated) for the RHS (or press Enter to assume zeros):")
        line = input().strip()
        if line == "":
            constants = [0] * row
        else:
            constants = list(map(int, line.split()))
            if len(constants) != row:
                print(f"Invalid constants length: expected {row}, got {len(constants)}")
                return

        augmented = [matrix[i] + [constants[i]] for i in range(row)]
    elif col == row + 1:
        augmented = matrix
    else:
        print(f"Invalid input: expected {row} or {row+1} columns, got {col} columns.")
        return

    solutions = cramers_rule(augmented)

    if solutions:
        for i, sol in enumerate(solutions):
            print(f"x{i+1} = {sol}")

if __name__ == "__main__":
    main()
