n = int(input("Masukkan tinggi: "))
m = int(input("Masukkan lebar: "))

counter = 1
for i in range(n):
    for j in range(m):
        print(counter, end=" ")
        counter += 1
    print()

