# 
class Karakter: 
    def __init__(self, Nimi, Elud, Tugevus):
        self.Nimi = Nimi
        self.Elud = Elud
        self.Tugevus = Tugevus

    def KaotaElusi(self, kaotatudelud):
        if kaotatudelud <= 0:
            print("Ei sa kaotada vähem kui 1 elu")
        else:
            self.Elud -= kaotatudelud
            print(f"[{self.Nimi}] Kaotasid {kaotatudelud} elu.")
    
    def LisaElusi(self, lisatudelud):
        if lisatudelud <= 0:
            print("Ei sa lisada vähem kui 1 elu")
        else:
            self.Elud += kaotatudelud
            print(f"[{self.Nimi}] Lisati {kaotatudelud} elu.")

class Vaenlane: 
    def __init__(self, Elud, Tugevus):
        self.Elud = Elud
        self.Tugevus = Tugevus

    def KaotaElusi(self, kaotatudelud):
        if kaotatudelud <= 0:
            print("Ei sa kaotada vähem kui 1 elu")
        else:
            self.Elud -= kaotatudelud
            print(f"[Vaenlane] Kaotas {kaotatudelud} elu.")