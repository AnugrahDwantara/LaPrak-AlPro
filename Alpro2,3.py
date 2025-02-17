gaji_per_jam = float(input("Masukkan gaji per jam yang diinginkan (dalam Rp): "))
jam_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

total_minggu = 5

pendapatan_kotor = gaji_per_jam * jam_per_minggu * total_minggu
pendapatan_bersih = pendapatan_kotor * 0.86
uang_baju_aksesoris = pendapatan_bersih * 0.10
uang_alat_tulis = pendapatan_bersih * 0.01
sisa_uang = pendapatan_bersih - (uang_baju_aksesoris + uang_alat_tulis)
uang_sedekah = sisa_uang * 0.25
uang_anak_yatim = uang_sedekah * 0.30
uang_dhuafa = uang_sedekah * 0.70

print("\nHasil perhitungan:")
print("1. Pendapatan kotor selama libur musim panas: Rp {:.2f}".format(pendapatan_kotor))
print("2. Pendapatan bersih setelah pajak 14%: Rp {:.2f}".format(pendapatan_bersih))
print("3. Uang yang dihabiskan untuk baju dan aksesoris: Rp {:.2f}".format(uang_baju_aksesoris))
print("4. Uang yang dihabiskan untuk alat tulis: Rp {:.2f}".format(uang_alat_tulis))
print("5. Uang yang disedekahkan: Rp {:.2f}".format(uang_sedekah))
print("6. Uang yang diterima anak yatim (30% dari sedekah): Rp {:.2f}".format(uang_anak_yatim))
print("7. Uang yang diterima kaum dhuafa (70% dari sedekah): Rp {:.2f}".format(uang_dhuafa))