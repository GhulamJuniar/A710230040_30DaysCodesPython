class Kendaraan:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    
    def info(self):
        print(f"Kendaraan {self.nama}, warna {self.warna}.")

mobil1 = Kendaraan("Porsche","Biru")
mobil1.info()