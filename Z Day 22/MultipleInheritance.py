class A:
    def metode_A(self):
        print("Metode dari kelas A")

class B:
    def metode_B(self):
        print("Metode dari kelas B")

class C(A, B):
    def metode_C(self):
        print("Metode dari kelas C")


objek_c = C()
objek_c.metode_A()
objek_c.metode_B()
objek_c.metode_C()
