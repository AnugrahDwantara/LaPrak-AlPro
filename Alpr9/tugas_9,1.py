def perbandingan(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            baris1 = f1.readlines()
            baris2 = f2.readlines()

            max_baris = max(len(baris1), len(baris2))
            ada_perbedaan = False

            for i in range(max_baris):
                teks1 = baris1[i].strip() if i < len(baris1) else ""
                teks2 = baris2[i].strip() if i < len(baris2) else ""
                
                if teks1 != teks2:
                    print(f"Baris {i+1} berbeda:")
                    print(f"  File1: {teks1}")
                    print(f"  File2: {teks2}")
                    ada_perbedaan = True

            if not ada_perbedaan:
                print("Kedua file sama persis.")
    except FileNotFoundError:
        print("Salah satu file tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

perbandingan ("9,1,1.txt","9,1,2.txt")

