class Matematika:
    @staticmethod
    def tambah(a, b):
        return a + b

    @classmethod
    def kali(cls, a, b):
        return a * b

# Penggunaan static method
print("Hasil penjumlahan:", Matematika.tambah(3, 4))

# Penggunaan class method
print("Hasil perkalian:", Matematika.kali(3, 4))
