def f(x):
    return e**x - 1 # Dari soal 1B

def solve_equation_n_iterations(n):
    x = 0  # Nilai x pada awalnya
    iteration = 0  # Inisialisasi iterasi

    while iteration < n: #perulangan iterasi kurang dari n
        x_new = x - f(x) / (3*x**2 - 2)  # Metod untuk mencari akar
        if abs(x_new - x) < 1e-6:  # Kondisi berhenti jika perbedaan sangat kecil
            break
        x = x_new
        iteration += 1

    return x

n = 5  # Ganti dengan nilai n yang diinginkan user
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")