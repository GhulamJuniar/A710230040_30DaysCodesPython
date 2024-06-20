
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f"Halo, nama saya {self.nama}.")


orang1 = Manusia("Ghulam", 18)
orang1.sapa()
