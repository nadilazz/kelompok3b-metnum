from sympy import symbols, diff

def hitung_turunan():
    # Memasukkan variabel simbolik
    x = symbols('x')

    # Memasukkan fungsi yang ingin dihitung turunannya
    fungsi = input("Masukkan fungsi (gunakan x sebagai variabel): ")

    try:
        # Mengevaluasi dan menghitung turunan
        turunan = diff(fungsi, x)
        print("Turunan dari", fungsi, "adalah:", turunan)

    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    hitung_turunan()
