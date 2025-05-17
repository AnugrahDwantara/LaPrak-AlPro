def hitung_domain_pengirim():
    nama_file = 'tugas_12,4.txt'
    try:
        with open(nama_file, 'r') as file:
            domain_count = dict()
            for baris in file:
                baris = baris.rstrip()
                if baris.startswith('From '):
                    bagian = baris.split()
                    if len(bagian) > 1:
                        email = bagian[1]
                        if '@' in email:
                            domain = email.split('@')[1]
                            domain_count[domain] = domain_count.get(domain, 0) + 1
            return domain_count
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return {}

hasil = hitung_domain_pengirim()
print(hasil)
