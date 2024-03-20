import random
from Organizm import Organizm


class Zwierze(Organizm):

    def akcja(self):
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
        from Wilk import Wilk
        from Owca import Owca
        from Lis import Lis
        from Zolw import Zolw
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
                if self.get_gatunek() == "Wilk":
                    nowy_wilk = Wilk(new_y, new_x, self.get_swiat())
                    self.get_swiat().get_nowe_organizmy().append(nowy_wilk)
                    self.get_swiat().get_mapa()[new_y][new_x] = nowy_wilk
                elif self.get_gatunek() == "Owca":
                    nowa_owca = Owca(new_y, new_x, self.get_swiat())
                    self.get_swiat().get_nowe_organizmy().append(nowa_owca)
                    self.get_swiat().get_mapa()[new_y][new_x] = nowa_owca
                elif self.get_gatunek() == "Lis":
                    nowy_lis = Lis(new_y, new_x, self.get_swiat())
                    self.get_swiat().get_nowe_organizmy().append(nowy_lis)
                    self.get_swiat().get_mapa()[new_y][new_x] = nowy_lis
                elif self.get_gatunek() == "Zolw":
                    nowy_zolw = Zolw(new_y, new_x, self.get_swiat())
                    self.get_swiat().get_nowe_organizmy().append(nowy_zolw)
                    self.get_swiat().get_mapa()[new_y][new_x] = nowy_zolw

                print(f'Urodzilo sie nowe zwierze: {self.get_gatunek()} ({str(new_y)}, {str(new_x)})')
        else:
            if self.get_sila() > napastnik.get_sila():
                if napastnik.get_gatunek() == "Czlowiek":
                    napastnik.get_swiat().set_koniec(True)
                print(f'{self.get_gatunek()} zabija {napastnik.get_gatunek()} ({napastnik.get_y()},{napastnik.get_x()})')
                self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
                self.get_swiat().get_do_usuniecia().append(napastnik)
                napastnik.set_zyje(False)
            else:
                print(f'{napastnik.get_gatunek()} zabija {self.get_gatunek()} ({self.get_y()},{self.get_x()})')
                self.get_swiat().get_mapa()[opp_y][opp_x] = None
                self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = napastnik
                self.set_zyje(False)
                self.get_swiat().get_do_usuniecia().append(self)