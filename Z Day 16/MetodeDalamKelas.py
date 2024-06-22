class Karyawan:
    jumlah_karyawan = 0  

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print(f"Total karyawan: {Karyawan.jumlah_karyawan}")

    def tampilkan_profil(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

karyawan1 = Karyawan("Ghulam", 500000000)
karyawan2 = Karyawan("Sir V", 200000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan1.tampilkan_jumlah()
