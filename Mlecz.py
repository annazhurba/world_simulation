import random
from Roslina import Roslina


class Mlecz(Roslina):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(0)
        self.set_inicjatywa(0)
        self.set_wiek(0)
        self.set_gatunek("Mlecz")
        self.set_rodzaj("Roslina")
        self.set_znaczek('m')
        self.set_swiat(swiat)

    def akcja(self):
        for it in range(3):
            szansa = random.randrange(15)
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

                if (curr_y + i >= 0) and (curr_y + i < self.get_swiat().get_n()) and (curr_x + j >= 0) and (
                        curr_x + j < self.get_swiat().get_m()):
                    if self.get_swiat().get_mapa()[curr_y + i][curr_x + j] is None:
                        nowy_mlecz = Mlecz(curr_y + i, curr_x + j, self.get_swiat())
                        self.get_swiat().get_nowe_organizmy().append(nowy_mlecz)
                        self.get_swiat().get_mapa()[curr_y + i][curr_x + j] = nowy_mlecz
                        print(f'Wyrosla nowa roslina: {self.get_gatunek()} ({str(curr_y + i)}, {str(curr_x + j)}')
                    else:
                        for itr in range(len(self.get_swiat().get_organizmy())):
                            if self.get_swiat().get_organizmy()[itr] is not None:
                                if (self.get_swiat().get_organizmy()[itr].get_x() == curr_x + j) and (
                                        self.get_swiat().get_organizmy()[itr].get_y() == curr_y + i):
                                    self.get_swiat().get_organizmy()[itr].kolizja(curr_y + i, curr_x + j, self)
                                    return

