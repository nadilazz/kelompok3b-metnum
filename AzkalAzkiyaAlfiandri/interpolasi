import numpy as np

def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (xi - x[j]) / (x[i] - x[j])
        result += term

    return result

# Contoh data input
x = [1.0, 2.0, 3.0, 4.0]
y = [1.0, 8.0, 27.0, 64.0]

# Nilai yang akan diinterpolasi
xi = 2.5

# Melakukan interpolasi
interpolated_value = lagrange_interpolation(x, y, xi)

print(f"Hasil interpolasi pada x = {xi} adalah y = {interpolated_value}")
