import random
from Zwierze import Zwierze


class Lis(Zwierze):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(3)
        self.set_inicjatywa(7)
        self.set_wiek(0)
        self.set_gatunek("Lis")
        self.set_rodzaj("Zwierze")
        self.set_znaczek('L')
        self.set_swiat(swiat)

    def action(self):
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
                    if (self.get_swiat().get_organizmy()[itr].get_x() == curr_x) and (self.get_swiat().getOrganizmy()[itr].get_y() == curr_y + i):
                        if self.get_swiat().get_organizmy()[itr].get_sila() > self.get_sila():
                            print(f'{self.get_gatunek()} nie rusza sie na pole {self.get_swiat().get_organizmy()[itr].get_gatunek()} ({self.get_swiat().get_organizmy()[itr].get_y()},{self.get_swiat().get_organizmy()[itr].get_x()})')
                            self.akcja()
                        else:
                            self.get_swiat().get_organizmy()[itr].kolizja(curr_y + i, curr_x + j, self)
                            return
        else:
            self.akcja()