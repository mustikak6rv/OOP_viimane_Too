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