class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class Toko:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def tampilkan_produk(self):
        print(f"Daftar produk di toko {self.nama}:")
        for produk in self.daftar_produk:
            print(f"Kode: {produk.kode}, Nama: {produk.nama}, Harga: {produk.harga}")

toko1 = Toko("Toko Serba Ada")

produk1 = Produk("P001", "Buku Tulis", 85000)
produk2 = Produk("P002", "Mouse Wireless", 200000)

toko1.tambah_produk(produk1)
toko1.tambah_produk(produk2)

toko1.tampilkan_produk()
