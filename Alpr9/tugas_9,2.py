def cek_jawaban(soal, jawaban_benar, jawaban_user):
    return jawaban_user.strip().lower() == jawaban_benar.strip().lower()

def proses_soal(filename):
    try:
        with open(filename, 'r') as file:
            for baris in file:
                if '||' in baris:
                    bagian = baris.strip().split('||')
                    soal = bagian[0].strip()
                    jawaban_benar = bagian[1].strip()

                    print(soal)
                    jawaban_user = input("Jawab: ")

                    if cek_jawaban(soal, jawaban_benar, jawaban_user):
                        print("Jawaban benar!\n")
                    else:
                        print("Jawaban salah!\n")
    except FileNotFoundError:
        print("File tidak ditemukan!")


proses_soal("tugas_9,2.txt")
