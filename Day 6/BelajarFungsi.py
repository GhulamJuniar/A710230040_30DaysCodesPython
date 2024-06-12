# Definisi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a,b):
    return a * b

def bagi (a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak Bisa Dibagi Dengan Nol"
    
# Pemanggilan Fungsi
x = 10
y = 5

print("Tambah:", tambah(x,y))
print("Kurang:", kurang(x,y))
print("Kali:", kali(x,y))
print("Bagi:", bagi(x,y))
print("Bagi Dengan Nol:", bagi(x, 0))