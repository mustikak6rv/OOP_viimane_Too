# 
class Karakter: 
    def __init__(self, Nimi, Elud, Tugevus, x, y):
        self.Nimi = Nimi
        self.Elud = Elud
        self.Tugevus = Tugevus
        self.x = x
        self.y = y
        
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
            self.Elud += lisatudelud
            print(f"[{self.Nimi}] Lisati {lisatudelud} elu.")

    def LiiguYles(self):
        self.y += 1
        print(f"[{self.Nimi}] Liikusid ülesse")

    def LiiguAlla(self):
        self.y -= 1
        print(f"[{self.Nimi}] Liikusid alla")

    def LiiguVasakule(self):
        self.x -= 1
        print(f"[{self.Nimi}] Liikusid vasakule")

    def LiiguParemale(self):
        self.x += 1
        print(f"[{self.Nimi}] Liikusid paremale")   



class Vaenlane: 
    def __init__(self, Elud, Tugevus, x, y):
        self.Elud = Elud
        self.Tugevus = Tugevus

    def KaotaElusi(self, kaotatudelud):
        if kaotatudelud <= 0:
            print("Ei sa kaotada vähem kui 1 elu")
        else:
            self.Elud -= kaotatudelud
            print(f"[Vaenlane] Kaotas {kaotatudelud} elu.")