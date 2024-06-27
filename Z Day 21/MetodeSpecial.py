class Kendaraan:
    def __init__(self, nama, Warna):
        self.nama = nama
        self.warna = Warna

    def __str__(self):
        return f"Kendaraan {self.nama}, Warna {self.warna}."

mobil1 = Kendaraan("Porsche", "Biru")
print(mobil1)
