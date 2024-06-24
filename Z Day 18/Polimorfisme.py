class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        print("Miaw miaw miaw miaw miaw miaw!")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk guk guk guk!")

def dengarkan_suara(hewan):
    hewan.suara()

kucing1 = Kucing()
anjing1 = Anjing()

dengarkan_suara(kucing1)
dengarkan_suara(anjing1)
