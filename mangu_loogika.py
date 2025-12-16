from Klassid import Karakter
from Klassid import Vaenlane
import random

# Vaenlaste genereerimine
vaenlased = [] 

for i in range(2):  
    randx = random.randint(1, 6)
    randy = random.randint(1, 6)
    print(f"Vaenlane: {i+1} at ({randx}, {randy})")
    vaenlane = Vaenlane(100, 15, randx, randy)
    vaenlased.append(vaenlane)  

print(f"Generated {len(vaenlased)} enemies.") 

Trevori = Karakter("Trevori", 250, 50, 0, 0)

# Movemint
print("\n=== Trevori Movement System ===")
print("Commands: 'w' (up), 's' (down), 'a' (left), 'd' (right), 'q' (quit)")
print(f"Trevori position: ({Trevori.x}, {Trevori.y})")

while True:
    command = input("Enter movement command: ").lower().strip()
    if command == 'q':
        print("Mäng lõppes!")
        break
    elif command == 'w':
        Trevori.LiiguYles()
    elif command == 's':
        Trevori.LiiguAlla()
    elif command == 'a':
        Trevori.LiiguVasakule()
    elif command == 'd':
        Trevori.LiiguParemale()
    else:
        print("Teadmatu käsk! Kasuta w/a/s/d või q et lõpetada mäng.")
    
    # For loop mis kontrollib kas trevori on vastaste peal.
    for vaenlane in vaenlased:
        if Trevori.x == vaenlane.x and Trevori.y == vaenlane.y:
            print("Kokku põrkusid vaenlaga!")
            Trevori.KaotaElusi(vaenlane.Tugevus)
            vaenlane.KaotaElusi(Trevori.Tugevus)
            # Eemalda surnud vaenlased
            if vaenlane.Elud <= 0:
                vaenlased.remove(vaenlane)
            break

    print(f"Trevori positoon: ({Trevori.x}, {Trevori.y})")
    print(f"Elud: {Trevori.Elud}")

    
    print("Vaenlaste positsioonid:")
    for i, vaenlane in enumerate(vaenlased, 1):
        print(f"  Vaenlane {i}: Elud: {vaenlane.Elud} | ({vaenlane.x}, {vaenlane.y})")

    if not vaenlased:
        print("Kõik vaenlased on hävitatud!")
