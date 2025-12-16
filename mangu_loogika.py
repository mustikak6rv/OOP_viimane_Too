
from Klassid import Karakter
from Klassid import Vaenlane
import random

# Vaenlaste genereerimine
vaenlased = [] 
for i in range(2):  
    randx = random.randint(1, 6)
    randy = random.randint(1, 6)
    vaenlane = Vaenlane(100, 15, randx, randy)
    vaenlased.append(vaenlane)  

Trevori = Karakter("Trevori", 250, 50, 0, 0)

def statid():
    """EASYGUI mänguseis"""
    status = f"⚔️ TREVORI SUUR LAHINGU MÄNG ⚔️\n"
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
    
    # Liikumine
    if command == 'w':
        Trevori.LiiguYles()
    elif command == 's':
        Trevori.LiiguAlla()
    elif command == 'a':
        Trevori.LiiguVasakule()
    elif command == 'd':
        Trevori.LiiguParemale()
    
    # Kokkupõrke kontroll
    for vaenlane in vaenlased[:]:
        if Trevori.x == vaenlane.x and Trevori.y == vaenlane.y:
            msgbox(f"⚔️ LAHING!\nTrevori: {Trevori.Elud} ❤️\nVaenlane: {vaenlane.Elud} ❤️", "LAHING!")
            
            Trevori.KaotaElusi(vaenlane.Tugevus)
            vaenlane.KaotaElusi(Trevori.Tugevus)
            
            if vaenlane.Elud <= 0:
                vaenlased.remove(vaenlane)
                msgbox("VAENLANE HÄVITATUD!", "VÕIT!")
            
            if Trevori.Elud <= 0:
                msgbox("TREVORI SURI!", "KAOTUS!")
                exit()
            break

    # VÕIT!
    if not vaenlased:
        msgbox("KÕIK VAENLASED HÄVITATUD! ", "SIGMA VÕIT!")
        break
