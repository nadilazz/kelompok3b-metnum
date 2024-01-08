from sympy import symbols, integrate

def hitung_integral():
    # Memasukkan variabel simbolik
    x = symbols('x')

    # Memasukkan fungsi yang ingin dihitung integralnya
    fungsi = input("Masukkan fungsi (gunakan x sebagai variabel): ")

    try:
        # Mengevaluasi dan menghitung integral
        integral = integrate(fungsi, x)
        print("Integral dari", fungsi, "adalah:", integral)

    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    hitung_integral()
