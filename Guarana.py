from Roslina import Roslina


class Guarana(Roslina):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(0)
        self.set_inicjatywa(0)
        self.set_wiek(0)
        self.set_gatunek("Guarana")
        self.set_rodzaj("Roslina")
        self.set_znaczek('g')
        self.set_swiat(swiat)

    def kolizja(self, opp_y, opp_x, napastnik):
        if napastnik.get_rodzaj() == "Zwierze":
            napastnik.set_sila(napastnik.get_sila() + 3)
            lp = -1
            for i in range(len(self.get_swiat().get_organizmy())):
                if self.get_swiat().get_organizmy()[i] is not None:
                    if (self.get_swiat().get_organizmy()[i].get_x() == napastnik.get_x()) and (self.get_swiat().get_organizmy()[i].get_y() == napastnik.get_y()):
                        lp = i
                        break
            self.get_swiat().get_do_usuniecia().append(self)
            self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
            self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = napastnik
            napastnik.set_x(self.get_x())
            napastnik.set_y(self.get_y())
            #self.get_swiat().get_organizmy()[lp].set_x(self.get_x())
            #self.get_swiat().get_organizmy()[lp].set_y(self.get_y())
            print(f'{napastnik.get_gatunek()} zjada {self.get_gatunek()} ({self.get_y()}, {self.get_x()})')
            self.set_zyje(False)
