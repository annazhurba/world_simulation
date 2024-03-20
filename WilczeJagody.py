from Roslina import Roslina


class WilczeJagody(Roslina):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(99)
        self.set_inicjatywa(0)
        self.set_wiek(0)
        self.set_gatunek("WilczeJagody")
        self.set_rodzaj("Roslina")
        self.set_znaczek('j')
        self.set_swiat(swiat)

    def kolizja(self, opp_y, opp_x, napastnik):
        from Czlowiek import Czlowiek
        if isinstance(napastnik, Czlowiek):
            napastnik.get_swiat().set_koniec(True)
        if napastnik.get_rodzaj() == "Zwierze":
            self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
            self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = None
            print(f'{napastnik.get_gatunek()} zjada {self.get_gatunek()} i umiera ({napastnik.get_y()}, {napastnik.get_x()})')
            napastnik.set_zyje(False)
            self.set_zyje(False)
            self.get_swiat().get_do_usuniecia().append(self)
            self.get_swiat().get_do_usuniecia().append(napastnik)
