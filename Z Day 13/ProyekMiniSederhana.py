def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
   return a * b

def bagi(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian Dengan 0"
    
print("Kalkulator Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukan Pilihan Anda (1/2/3/4): ")

angka1 = float(input("Masukan Angka Pertama: "))
angka2 = float(input("Masukan Angka Ke dua: "))

if pilihan == '1':
    print("Hasil :", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil :", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil :", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil :", bagi(angka1, angka2))
else:
    print("Pilihan Tidak Valid")