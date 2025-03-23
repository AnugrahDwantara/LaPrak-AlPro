def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

n = int(input("Masukkan nilai n: "))

for i in range(n, 0, -1):
    print(faktorial(i), end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
