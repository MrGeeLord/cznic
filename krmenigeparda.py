class Gepard:
    def __init__(self):
        self.pocet_zivotu = 9

    def uber_zivot(self):
        if self.pocet_zivotu > 0:
            self.pocet_zivotu -= 1
        else:
            print("Nemuzes zabit uz mrtve zvire!")
    def snez(self, jidlo):
        if jidlo == "ryba" and self.pocet_zivotu < 9:
            if self.pocet_zivotu >= 0:
                print("Je zbytecne krmit mrtve zvire!")
            else:
                self.pocet_zivotu += 1
                print("Gepard spapal rybu a obnovil se mu jeden zivot.")
        else:
            print("Gepard se krmi.")
    def behej(self):
        if self.pocet_zivotu > 0:
            print("Gepard bezi.")
        else:
            print("Mrtve zvire uz nikam nedobehne!")

    def napapej_se(self):
        while self.pocet_zivotu < 9:
            if self.pocet_zivotu > 0:
                self.pocet_zivotu += 1
                print(f"Gepard se dal na pránickou stravu a obnovil se mu jeden zivot. Gepard teď má {self.pocet_zivotu} životů")
            else:
                print("Je zbytecne krmit mrtve zvire!")
                break
        else:
            print("Gepard je už zcela nasycen.")

gepard = Gepard()

gepard.behej()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.uber_zivot()
gepard.behej()
# gepard.snez("ryba")
print(gepard.pocet_zivotu)
gepard.napapej_se()
gepard.snez("ryba")
gepard.behej()
