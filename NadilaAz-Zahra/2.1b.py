def f(x):
    return e**x - x

def solve_equation_n_iterations(n):
    x = 0  # Nilai awal x
    iteration = 0  # Inisialisasi hitungan iterasi

    while iteration < n:
        x_new = x - f(x) / (3*x**2 - 2)  # Metode Newton-Raphson untuk mencari akar
        if abs(x_new - x) < 1e-6:  # Kondisi berhenti jika perbedaan sangat kecil
            break
        x = x_new
        iteration += 1

    return x

n = 5  # Ganti dengan nilai n yang Anda inginkan
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")
