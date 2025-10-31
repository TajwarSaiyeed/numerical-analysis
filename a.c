#include <stdio.h>
#include <math.h>

double f(double x) {
    return 2 * (x * x * x) + (3 * x) - 1;
}

int main() {
    double x1 = 0;
    double x2 = 1;
    double E = 1e-8;
    double f1 = f(x1);
    double f2 = f(x2);

    if (f1 * f2 > 0) {
        printf("No root found\n");
        return 0;
    }

    while (1) {
        double x0 = (x1 + x2) / 2;
        double f0 = f(x0);

        if (f0 == 0) {
            printf("Root found: %lf\n", x0);
            return 0;
        }

        if (f1 * f0 < 0) {
            x2 = x0;
        } else {
            x1 = x0;
            f1 = f0;
        }

        if (fabs((x2 - x1) / x2) < E) {
            double root = (x1 + x2) / 2;
            printf("Root found: %lf\n", root);
            return 0;
        }
    }

    return 0;
}