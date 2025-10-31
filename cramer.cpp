#include <iostream>
using namespace std;

const int MAX = 10;

double determinant(double mat[][MAX], int n) {
    if (n == 1) {
        return mat[0][0];
    }
    
    if (n == 2) {
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0];
    }
    
    double det = 0;
    double temp[MAX][MAX];
    int sign = 1;
    
    for (int f = 0; f < n; f++) {
        int sub_i = 0;
        for (int i = 1; i < n; i++) {
            int sub_j = 0;
            for (int j = 0; j < n; j++) {
                if (j == f) continue;
                temp[sub_i][sub_j] = mat[i][j];
                sub_j++;
            }
            sub_i++;
        }
        det += sign * mat[0][f] * determinant(temp, n - 1);
        sign = -sign;
    }
    
    return det;
}

void cramersRule(double coeff[][MAX], double constants[], int n) {
    double D = determinant(coeff, n);
    
    if (D == 0) {
        return;
    }
    
    
    for (int i = 0; i < n; i++) {
        double temp[MAX][MAX];
        
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (col == i) {
                    temp[row][col] = constants[row];
                } else {
                    temp[row][col] = coeff[row][col];
                }
            }
        }
        
        double Di = determinant(temp, n);
        cout << "x" << i + 1 << " = " << Di / D << endl;
    }
}

int main() {
    int n;
    double coeff[MAX][MAX];
    double constants[MAX];
    
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> coeff[i][j];
        }
    }
    
    for (int i = 0; i < n; i++) {
        cin >> constants[i];
    }
    
    cramersRule(coeff, constants, n);
    
    return 0;
}