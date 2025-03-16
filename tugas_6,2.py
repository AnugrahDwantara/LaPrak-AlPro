def ganjil(bawah, atas):
    if bawah > atas:
        langkah = -2
        if bawah % 2 == 0:
            bawah -= 1
    else:
        langkah = 2
        if bawah % 2 == 0:
            bawah += 1
    
    for i in range(bawah, atas + langkah, langkah):
        print(i, end=' ')

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

ganjil(bawah, atas)
