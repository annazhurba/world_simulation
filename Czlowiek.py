import random
from Zwierze import Zwierze


class Czlowiek(Zwierze):
    __superpower_tury: int = 0

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(5)
        self.set_inicjatywa(4)
        self.set_wiek(0)
        self.set_gatunek("Czlowiek")
        self.set_rodzaj("Zwierze")
        self.set_znaczek('C')
        self.set_swiat(swiat)

    def get_superpower_tury(self):
        return self.__superpower_tury

    def set_superpower_tury(self, liczba):
        self.__superpower_tury = liczba

    def akcja(self):
        if (self.__superpower_tury > 0) and (self.__superpower_tury <= 5):
            self.__superpower_tury = self.__superpower_tury + 1
            print("Specjalna umiejetnosc Czlowieka jest aktywna")
        elif (self.__superpower_tury > 5) and (self.__superpower_tury <= 10):
            self.__superpower_tury = self.__superpower_tury + 1
        elif self.__superpower_tury > 10:
            self.__superpower_tury = 0
        kier = -1
        curr_x = self.get_x()
        curr_y = self.get_y()
        if self.get_swiat().get_key() == 37: #lewo
            kier = 0
        elif self.get_swiat().get_key() == 39: #prawo
            kier = 1
        elif self.get_swiat().get_key() == 38: #gora
            kier = 2
        elif self.get_swiat().get_key() == 40: #dol
            kier = 3
        elif self.get_swiat().get_key() == 65:
            if self.__superpower_tury == 0:
                self.__superpower_tury = 1
                print("Specjalna umiejetnosc Czlowieka zostala aktywowana!")
            elif (self.__superpower_tury > 0) and (self.__superpower_tury <= 5):
                print("Specjalna umiejetnosc Czlowieka jest aktywna")
            elif (self.__superpower_tury > 5) and (self.__superpower_tury <= 10):
                print("Specjalna umiejetnosc Czlowieka jest nieostepna. Sprobuj pozniej.")
            else:
                return
        i = 0
        j = 0
        if kier != -1:
            if kier == 0:
                j -= 1
            elif kier == 1:
                j += 1
            elif kier == 2:
                i -= 1
            elif kier == 3:
                i += 1
        if (self.get_swiat().get_key() == 38) or (self.get_swiat().get_key() == 39) or (
                self.get_swiat().get_key() == 37) or (self.get_swiat().get_key() == 40):
            if (curr_y + i >= 0) and (curr_y + i < self.get_swiat().get_n()) and (curr_x + j >= 0) and (curr_x + j < self.get_swiat().get_m()):
                if self.get_swiat().get_mapa()[curr_y + i][curr_x + j] is None:
                    self.set_x(curr_x + j)
                    self.set_y(curr_y + i)
                    self.get_swiat().get_mapa()[curr_y][curr_x] = None
                    self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = self
                else:
                    for itr in range(len(self.get_swiat().get_organizmy())):
                        if self.get_swiat().get_organizmy()[itr] is not None:
                            if (self.get_swiat().get_organizmy()[itr].get_x() == curr_x + j) and (self.get_swiat().get_organizmy()[itr].get_y() == curr_y + i):
                                self.get_swiat().get_organizmy()[itr].kolizja(curr_y + i, curr_x + j, self)
                                return

    def kolizja(self, opp_y, opp_x, napastnik):
        if self.__superpower_tury == 0:
            if self.get_sila() > napastnik.get_sila():
                print(f'{self.get_gatunek()} zabija {napastnik.get_gatunek()} ({napastnik.get_y()}, {napastnik.get_x()})')
                self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = self
                napastnik.set_zyje(False)
                self.get_swiat().get_do_usuniecia().append(napastnik)
            else:
                print(f'{napastnik.get_gatunek()} zabija {self.get_gatunek()} ({self.get_y()},{self.get_x()})')
                self.get_swiat().get_mapa()[opp_y][opp_x] = None
                self.set_zyje(False)
                self.get_swiat().get_do_usuniecia().append(self)
        elif 0 < self.__superpower_tury <= 5:
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

            if (curr_y + i >= 0) and (curr_y + i < self.get_swiat().get_n()) and (curr_x + j >= 0) and (
                    curr_x + j < self.get_swiat().get_m()):
                if self.get_swiat().get_mapa()[curr_y + i][curr_x + j] is None:
                    napastnik.set_x(curr_x + j)
                    napastnik.set_y(curr_y + i)
                    self.get_swiat().get_mapa()[curr_y][curr_x] = None
                    self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = self
                else:
                    for itr in range(len(self.get_swiat().get_organizmy())):
                        if not (self.get_swiat().get_organizmy()[itr] is None):
                            if (self.get_swiat().get_organizmy()[itr].get_x() == curr_x) and (
                                    self.get_swiat().get_organizmy()[itr].get_y() == curr_y + i):
                                self.get_swiat().get_do_usuniecia().append(napastnik)
                                return
            else:
                self.get_swiat().get_mapa()[curr_y][curr_x] = self
                self.get_swiat().get_do_usuniecia().append(napastnik)
                return
            print(f'Czlowiek odpiera atak {napastnik.get_gatunek()} korzystajac z supermocy')
        elif 5 < self.__superpower_tury <= 10:
            if self.get_sila() > napastnik.get_sila():
                print(f'{self.get_gatunek()} zabija {napastnik.get_gatunek()} ({napastnik.get_y()}, {napastnik.get_x()})')
                self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
                self.get_swiat().get_do_usuniecia().append(napastnik)
                napastnik.set_zyje(False)
            else:
                print(f'{napastnik.get_gatunek()} zabija {self.get_gatunek()} ({self.get_y()}, {self.get_x()})')
                self.get_swiat().get_mapa()[opp_y][opp_x] = None
                self.set_zyje(False)
                self.get_swiat().set_koniec(True)
                self.get_swiat().get_do_usuniecia().append(self)
        elif self.__superpower_tury > 10:
            self.__superpower_tury = 0