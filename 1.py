# Auto ja jalgratas


class Soiduk: 
    def __init__(self, Mark, Aasta, Kiirus, Labisoit):
        self.Mark = Mark
        self.Aasta = Aasta
        self.Kiirus = Kiirus
        self.Labisoit = 0

    def soida(self, km):
        if 0 <= km:
            self.labisoit += km
        else:
            print("Kilomeetrid peavad olema >= 0")