def f(x):
    return x**3 - 2*x + 1 # Fungsi yang diketahui 

def solve_equation_n_iterations(n):
    x = 0  # Nilai x sebelum dioperasikan 
    iteration = 0  # Index awal iterasi 

    while iteration < n:
        x_new = x - f(x) / (3*x**2 - 2)  # Mencari akar
        if abs(x_new - x) < 1e-6:  # Percabangan mencari perbedaan sangat kecil 
            break
        x = x_new
        iteration += 1 # 

    return x

n = 5  # Nilai n bebas, tergantung soal
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")

