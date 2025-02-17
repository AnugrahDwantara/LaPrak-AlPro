x = int(input("Masukkan bilangan bulat x: "))
if x == 0:
    print("Error")
else:
    fx = 2 * (x ** 3) + 2 * x + 15 / x
    print("Hasil dari f(x) adalah:", fx)