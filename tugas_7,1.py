def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prima_terdekat(n):
    for i in range(n-1, 1, -1):
        if is_prima(i):
            return i
    return None

n = int(input("Masukkan bilangan n: "))
hasil = prima_terdekat(n)

if hasil:
    print(f"Bilangan prima terdekat yang lebih kecil dari {n} adalah {hasil}")
else:
    print("Tidak ada bilangan prima yang lebih kecil dari n")
