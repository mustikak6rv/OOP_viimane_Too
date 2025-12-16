from easygui import msgbox, buttonbox
import random

# VÄIKE LABÜRINT 5x5
# 1 = sein, 0 = vaba
laburint = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

def kas_sein(x, y):
    """True = sein või väljas, False = vaba"""
    if y < 0 or y >= len(laburint):
        return True
    if x < 0 or x >= len(laburint[0]):
        return True
    return laburint[y][x] == 1


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

    # ÜLES = y-1, ALLA = y+1, vasak/parem x-1/x+1
    def LiiguYles(self):
        uus_y = self.y - 1
        if kas_sein(self.x, uus_y):
            msgbox("Ees on SEIN, siia ei saa liikuda!", "SEIN!")
        else:
            self.y = uus_y
            print(f"[{self.Nimi}] Liikusid ülesse")

    def LiiguAlla(self):
        uus_y = self.y + 1
        if kas_sein(self.x, uus_y):
            msgbox("Ees on SEIN, siia ei saa liikuda!", "SEIN!")
        else:
            self.y = uus_y
            print(f"[{self.Nimi}] Liikusid alla")

    def LiiguVasakule(self):
        uus_x = self.x - 1
        if kas_sein(uus_x, self.y):
            msgbox("Ees on SEIN, siia ei saa liikuda!", "SEIN!")
        else:
            self.x = uus_x
            print(f"[{self.Nimi}] Liikusid vasakule")

    def LiiguParemale(self):
        uus_x = self.x + 1
        if kas_sein(uus_x, self.y):
            msgbox("Ees on SEIN, siia ei saa liikuda!", "SEIN!")
        else:
            self.x = uus_x
            print(f"[{self.Nimi}] Liikusid paremale")  


class Vaenlane: 
    def __init__(self, Elud, Tugevus, x, y):
        self.Elud = Elud
        self.Tugevus = Tugevus
        self.x = x
        self.y = y

    def KaotaElusi(self, kaotatudelud):
        if kaotatudelud <= 0:
            print("Ei sa kaotada vähem kui 1 elu")
        else:
            self.Elud -= kaotatudelud
            print(f"[Vaenlane] Kaotas {kaotatudelud} elu.")


# Vaenlased ainult vabadesse ruutudesse
vaenlased = [] 
vabad_kohad = [(1,1),(2,1),(3,1),(1,2),(3,2),(1,3),(2,3),(3,3)]
for i in range(2):
    x, y = random.choice(vabad_kohad)
    vabad_kohad.remove((x,y))
    vaenlane = Vaenlane(100, 15, x, y)
    vaenlased.append(vaenlane)


# Algus (1,1) – vaba ruut
Trevori = Karakter("Trevori", 250, 50, 1, 1)


def statid():
    status = "⚔️ TREVORI MÄNG ⚔️\n\n"
    status += f"Trevori: ({Trevori.x}, {Trevori.y}) | ❤️ {Trevori.Elud}\n\n"
    status += "VAENLASED:\n"
    for i, vaenlane in enumerate(vaenlased, 1):
        status += f"Vaenlane{i}: ({vaenlane.x}, {vaenlane.y}) ❤️ {vaenlane.Elud}\n"
    
    buttons = ["W (üles)", "S (alla)", "A (vasak)", "D (parem)", "Lõpeta"]
    valik = buttonbox(status, "TREVORI MÄNG", buttons)
    
    if valik is None:
        return 'q'
    elif "W" in valik:
        return 'w'
    elif "S" in valik:
        return 's'
    elif "A" in valik:
        return 'a'
    elif "D" in valik:
        return 'd'
    else:
        return 'q'


# Mängutsükkel
while True:
    command = statid()
    
    if command == 'q':
        msgbox("Mäng lõppes!", "BAKA!")
        break
    
    if command == 'w':
        Trevori.LiiguYles()
    elif command == 's':
        Trevori.LiiguAlla()
    elif command == 'a':
        Trevori.LiiguVasakule()
    elif command == 'd':
        Trevori.LiiguParemale()
    
    # Kokkupõrge
    for vaenlane in vaenlased[:]:
        if Trevori.x == vaenlane.x and Trevori.y == vaenlane.y:
            msgbox(
                f"⚔️ LAHING!\nTrevori: {Trevori.Elud} ❤️\nVaenlane: {vaenlane.Elud} ❤️",
                "LAHING!"
            )
            Trevori.KaotaElusi(vaenlane.Tugevus)
            vaenlane.KaotaElusi(Trevori.Tugevus)
            
            if vaenlane.Elud <= 0:
                vaenlased.remove(vaenlane)
                msgbox("VAENLANE HÄVITATUD!", "VÕIT!")
            
            if Trevori.Elud <= 0:
                msgbox("TREVORI SURI!", "KAOTUS!")
                exit()
            break

    if not vaenlased:
        msgbox("KÕIK VAENLASED HÄVITATUD!", "SIGMA VÕIT!")
        break
