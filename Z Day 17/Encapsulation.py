class Karyawan:
    def __init__(self, nama, gaji):
        self.__nama = nama  
        self.__gaji = gaji  

    def get_nama(self):
        return self.__nama

    def set_gaji(self, gaji_baru):
        self.__gaji = gaji_baru

    def tampilkan_profil(self):
        print(f"Nama: {self.__nama}, Gaji: {self.__gaji}")

karyawan1 = Karyawan("Ghulam", 5000000)
print(karyawan1.get_nama())
karyawan1.set_gaji(6000000)
karyawan1.tampilkan_profil()
