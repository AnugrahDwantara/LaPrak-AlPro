def cek_angka(a, b, c):
    if a != b and b != c and a != c:
        if a + b == c or a + c == b or b + c == a:
            return True
    return False


print(cek_angka(3, 5, 8))  
print(cek_angka(10, 4, 6))  
print(cek_angka(7, 2, 5))  
print(cek_angka(1, 1, 2))  
print(cek_angka(10, 15, 30))  
