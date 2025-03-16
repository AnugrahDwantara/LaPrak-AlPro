def perkalian(a, b):
    hasil = 0
    for _ in range(abs(a)):
        hasil += b
    hasil_str = " + ".join([str(b)] * abs(a))
    return hasil_str, hasil if a >= 0 else (" - ".join([str(b)] * abs(a)), -hasil)

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

detail, hasil = perkalian(angka1, angka2)
print(f"{angka1} x {angka2} = {detail} = {hasil}")
