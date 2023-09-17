def f(x):
    return x**3 - 2*x + 1 #fungsi dari soal nomor 1a

def solve_equation_n_iterations(n):
    x = 0  # Nilai awal dari x
    iteration = 0  # Inisialisasi hitungan iterasi

    while iteration < n: #program perulangan
        x_new = x - f(x) / (3*x**2 - 2)  # Metode untuk mencari akar
        if abs(x_new - x) < 1e-6:  # Kondisi dimana program akan berhenti jika perbedaan sangat kecil
            break
        x = x_new
        iteration += 1

    return x

n = 5  # Ganti dengan nilai n yang Anda inginkan
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")
