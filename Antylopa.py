from Zwierze import Zwierze
import random


class Antylopa(Zwierze):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(4)
        self.set_inicjatywa(4)
        self.set_wiek(0)
        self.set_gatunek("Antylopa")
        self.set_rodzaj("Zwierze")
        self.set_znaczek('A')
        self.set_swiat(swiat)

    def akcja(self):
        kier = random.randrange(8)
        curr_x = self.get_x()
        curr_y = self.get_y()
        i, j = 0, 0
        if kier == 0:
            j -= 2
        elif kier == 1:
            j += 2
        elif kier == 2:
            i -= 2
        elif kier == 3:
            i += 2
        elif kier == 4:
            i -= 2
            j -= 2
        elif kier == 5:
            i += 2
            j -= 2
        elif kier == 6:
            i -= 2
            j -= 2
        elif kier == 7:
            i += 2
            j += 2

        if (curr_y + i >= 0) and (curr_y + i < self.get_swiat().get_n()) and (curr_x + j >= 0) and (curr_x + j < self.get_swiat().get_m()):
            if self.get_swiat().get_mapa()[curr_y + i][curr_x + j] is None:
                self.set_x(curr_x + j)
                self.set_y(curr_y + i)
                self.get_swiat().get_mapa()[curr_y][curr_x] = None
                self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = self
            else:
                for itr in range(len(self.get_swiat().get_organizmy())):
                    if not(self.get_swiat().get_organizmy()[itr] is None):
                        if (self.get_swiat().get_organizmy()[itr].get_x() == curr_x) and (self.get_swiat().get_organizmy()[itr].get_y() == curr_y + i):
                            self.get_swiat().get_organizmy()[itr].kolizja(curr_y + i, curr_x + j, self)
                            return
        else:
            self.akcja()

    def kolizja(self, opp_y, opp_x, napastnik):
        if self.get_gatunek() == napastnik.get_gatunek():
            new_y, new_x = -1, -1
            k, d = 0, 0
            if (opp_y != 0) and (self.get_swiat().get_mapa()[opp_y - 1][opp_x] is None):
                k -= 1
            elif (opp_y != self.get_swiat().get_n() - 1) and (self.get_swiat().get_mapa()[opp_y + 1][opp_x] is None):
                k += 1
            elif (opp_x != 0) and (self.get_swiat().get_mapa()[opp_y][opp_x - 1] is None):
                d -= 1
            elif (opp_x != 0) and (self.get_swiat().get_mapa()[opp_y][opp_x - 1] is None):
                d += 1

            new_y = opp_y + k
            new_x = opp_x + d
            if (new_y >= 0) and (new_y < self.get_swiat().get_n()) and (new_x >= 0) and (new_x < self.get_swiat().get_m()) and (self.get_swiat().get_mapa()[new_y][new_x] is None):
                nowa_antylopa = Antylopa(new_y, new_x, self.get_swiat())
                self.get_swiat().get_nowe_organizmy().append(nowa_antylopa)
                self.get_swiat().get_mapa()[new_y][new_x] = nowa_antylopa
                print(f'Urodzilo sie nowe zwierze: Antylopa ({str(new_y)}, {str(new_x)})')
        else:
            szansa = random.randrange(4)
            if szansa == 0 or szansa == 1:
                new_y = -1
                new_x = -1
                k = 0
                d = 0
                if (opp_y != 0) and (self.get_swiat().get_mapa()[opp_y - 1][opp_x] is None):
                    k -= 1
                elif (opp_y != self.get_swiat().get_n() - 1) and (self.get_swiat().get_mapa()[opp_y + 1][opp_x] is None):
                    k += 1
                elif (opp_x != 0) and self.get_swiat().get_mapa()[opp_y][opp_x - 1] is None:
                    d -= 1
                elif (opp_x != self.get_swiat().get_m() - 1) and (self.get_swiat().get_mapa()[opp_y][opp_x + 1] is None):
                    d += 1
                new_y = opp_y + k
                new_x = opp_x + d
                if (new_y >= 0) and (new_y < self.get_swiat().get_n()) and (new_x >= 0) and (new_x < self.get_swiat().get_m()):
                    self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = None
                    self.get_swiat().get_mapa()[new_y][new_x] = self
                    self.set_x(new_x)
                    self.set_y(new_y)
                    self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
                    self.get_swiat().get_mapa()[opp_y][opp_x] = napastnik
                    napastnik.set_x(opp_x)
                    napastnik.set_y(opp_y)
                    print(f'Antylopa ucieka przed walka z {napastnik.get_gatunek()}')
            else:
                if self.get_sila() > napastnik.get_sila():
                    if napastnik.get_gatunek() == "Czlowiek":
                        napastnik.get_swiat().set_koniec(True)
                    print(f'Antylopa zabija {napastnik.get_gatunek()} ')
                    self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
                    self.get_swiat().get_do_usuniecia().append(napastnik)
                    napastnik.set_zyje(False)
                else:
                    print(f'{napastnik.get_gatunek()} zabija Antylopa')
                    self.get_swiat().get_mapa()[opp_y][opp_x] = None
                    self.set_zyje(False)
                    self.get_swiat().get_do_usuniecia().append(self)