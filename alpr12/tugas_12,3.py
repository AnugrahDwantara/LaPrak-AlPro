def hitung_pesan_email(nama_file):
    try:
        with open(nama_file, 'r') as file:
            hist = dict()
            for baris in file:
                baris = baris.rstrip()

                if baris.startswith('From '):
                    bagian = baris.split()
                    if len(bagian) > 1:
                        email = bagian[1]
                        hist[email] = hist.get(email, 0) + 1
            return hist
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return {}

nama_file = "tugas_12,3.txt"
hasil = hitung_pesan_email(nama_file)
print(hasil)
