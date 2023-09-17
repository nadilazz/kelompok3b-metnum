import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, exp, solve

# Fungsi yang akan dicari akarnya
def user_input_function():
    x = symbols('x')
    expression = input("Masukkan fungsi f(x) (gunakan x sebagai variabel): ")
    try:
        f = eval(expression)
        return f
    except:
        print("Fungsi yang dimasukkan tidak valid.")
        return None

# Input batas awal a dan b
def user_input_bounds():
    a = float(input("Masukkan batas bawah a: "))
    b = float(input("Masukkan batas atas b: "))
    return a, b

# Input toleransi (galat)
def user_input_tolerance():
    tolerance = float(input("Masukkan toleransi (galat): "))
    return tolerance

def plot_function(f, a, b):
    x_values = np.linspace(a, b, 1000)
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values, label="f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.title("Grafik f(x)")
    plt.show()

def bisection_method_with_user_input():
    f = user_input_function()
    if f is None:
        return

    a, b = user_input_bounds()
    tolerance = user_input_tolerance()

    if f(a) * f(b) >= 0:
        print("Nilai a dan b harus memiliki tanda yang berlawanan.")
        return

    c = (a + b) / 2
    iteration = 0

    while abs(f(c)) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print("Akar yang dihasilkan setelah", iteration, "iterasi:", c)

    # Plot fungsi dan akar yang dihasilkan
    plot_function(f, a, b)
    plt.scatter(c, f(c), color='red', label="Akar")
    plt.legend()
    plt.show()

# Panggil metode bagi dua dengan input pengguna
bisection_method_with_user_input()
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, exp, solve

# Fungsi yang akan dicari akarnya
def user_input_function():
    x = symbols('x')
    expression = input("Masukkan fungsi f(x) (gunakan x sebagai variabel): ")
    try:
        f = eval(expression)
        return f
    except:
        print("Fungsi yang dimasukkan tidak valid.")
        return None

# Input batas awal a dan b
def user_input_bounds():
    a = float(input("Masukkan batas bawah a: "))
    b = float(input("Masukkan batas atas b: "))
    return a, b

# Input toleransi (galat)
def user_input_tolerance():
    tolerance = float(input("Masukkan toleransi (galat): "))
    return tolerance

def plot_function(f, a, b):
    x_values = np.linspace(a, b, 1000)
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values, label="f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.title("Grafik f(x)")
    plt.show()

def bisection_method_with_user_input():
    f = user_input_function()
    if f is None:
        return

    a, b = user_input_bounds()
    tolerance = user_input_tolerance()

    if f(a) * f(b) >= 0:
        print("Nilai a dan b harus memiliki tanda yang berlawanan.")
        return

    c = (a + b) / 2
    iteration = 0

    while abs(f(c)) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print("Akar yang dihasilkan setelah", iteration, "iterasi:", c)

    # Plot fungsi dan akar yang dihasilkan
    plot_function(f, a, b)
    plt.scatter(c, f(c), color='red', label="Akar")
    plt.legend()
    plt.show()

# Panggil metode bagi dua dengan input pengguna
bisection_method_with_user_input()