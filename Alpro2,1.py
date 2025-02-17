bmi_diharapkan = float(input("Masukkan BMI yang diharapkan: "))
tinggi = float(input("Masukkan tinggi badan (dalam meter): "))
berat = bmi_diharapkan * (tinggi ** 2)
print("Berat badan yang diperlukan adalah:", berat, "kg")