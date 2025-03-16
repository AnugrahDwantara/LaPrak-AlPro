def hitung_ips(jumlah_mk):
    total_nilai = 0
    sks = 3 * jumlah_mk
    bobot = {"A": 4, "B": 3, "C": 2, "D": 1}
    
    for i in range(jumlah_mk):
        while True:
            nilai = input(f"nilai matakuliah {i+1}: ").upper()
            if nilai in bobot:
                total_nilai += bobot[nilai] * 3
                break
            else:
                print("Input tidak valid. Masukkan nilai A, B, C, atau D.")
    
    return total_nilai / sks

print ("Program Penghitung IPS Mahasiswa")
jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
ips = hitung_ips(jumlah_mk)
print(f"Indeks Prestasi Semester (IPS): {ips:.2f}")
