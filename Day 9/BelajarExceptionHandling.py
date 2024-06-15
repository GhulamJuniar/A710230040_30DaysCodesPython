try :
    angka = int(input("Masukan Angka: "))
    print("Pangkat Dua Dari Angka Tersebut Adalah", angka**2)
except ValueError:
    print("Input Harus Berapa Angka!")