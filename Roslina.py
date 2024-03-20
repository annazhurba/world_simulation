import random
from Organizm import Organizm


class Roslina(Organizm):
    def akcja(self):
        from Trawa import Trawa
        from Mlecz import Mlecz
        from Guarana import Guarana
        from WilczeJagody import WilczeJagody
        szansa = random.randrange(4)
        if szansa == 0:
            kier = random.randrange(8)
            curr_x = self.get_x()
            curr_y = self.get_y()
            i, j = 0, 0
            if kier == 0:
                j -= 1
            elif kier == 1:
                j += 1
            elif kier == 2:
                i -= 1
            elif kier == 3:
                i += 1
            elif kier == 4:
                i -= 1
                j -= 1
            elif kier == 5:
                i += 1
                j -= 1
            elif kier == 6:
                i -= 1
                j -= 1
            elif kier == 7:
                i += 1
                j += 1

            if (curr_y + i >= 0) and (curr_y + i < self.get_swiat().get_n()) and (curr_x + j >= 0) and (curr_x + j < self.get_swiat().get_m()):
                if self.get_swiat().get_mapa()[curr_y + i][curr_x + j] is None:
                    if isinstance(self, Guarana):
                        nowa_trawa = Trawa(curr_y + i, curr_x + j, self.get_swiat())
                        self.get_swiat().get_nowe_organizmy().append(nowa_trawa)
                        self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = nowa_trawa
                    elif self.get_gatunek() == "Mlecz":
                        nowy_mlecz = Mlecz(curr_y + i, curr_x + j, self.get_swiat())
                        self.get_swiat().get_nowe_organizmy().append(nowy_mlecz)
                        self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = nowy_mlecz
                    elif self.get_gatunek() == "Guarana":
                        nowa_guarana = Guarana(curr_y + i, curr_x + j, self.get_swiat())
                        self.get_swiat().get_nowe_organizmy().append(nowa_guarana)
                        self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = nowa_guarana
                    elif self.get_gatunek() == "WilczeJagody":
                        nowe_wj = WilczeJagody(curr_y + i, curr_x + j, self.get_swiat())
                        self.get_swiat().get_nowe_organizmy().append(nowe_wj)
                        self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = nowe_wj
                    print(f'Wyrosla nowa roslina: {self.get_gatunek()} ({curr_y + i}, {curr_x + j})')

    def kolizja(self, opp_y, opp_x, napastnik):
        if napastnik.get_rodzaj() == "Zwierze":
            lp = -1
            for i in range(len(self.get_swiat().get_organizmy())):
                if self.get_swiat().get_organizmy()[i] is not None:
                    if (self.get_swiat().get_organizmy()[i].get_x() == napastnik.get_x()) and (self.get_swiat().get_organizmy()[i].get_y() == napastnik.get_y()):
                        lp = i
                        break
            self.get_swiat().get_do_usuniecia().append(self)
            self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
            self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = self.get_swiat().get_organizmy()[lp]
            self.get_swiat().get_organizmy()[lp].set_x(self.get_x())
            self.get_swiat().get_organizmy()[lp].set_y(self.get_y())
            print(f'{napastnik.get_gatunek()} zjada {self.get_gatunek()} ({self.get_y()}, {self.get_x()})')
            self.set_zyje(False)
