from Roslina import Roslina
import random
from Czlowiek import Czlowiek


class BarszczSosnowskiego(Roslina):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(0)
        self.set_inicjatywa(0)
        self.set_wiek(0)
        self.set_gatunek("BarszczSosnowskiego")
        self.set_rodzaj("Roslina")
        self.set_znaczek('b')
        self.set_swiat(swiat)

    def akcja(self):
        from CyberOwca import CyberOwca
        curr_x = self.get_x()
        curr_y = self.get_y()
        if (curr_y >= 0) and (curr_x - 1 >= 0) and (curr_y < self.get_swiat().get_n()) and (curr_x - 1 < self.get_swiat().get_m()):
            if not(self.get_swiat().get_mapa()[curr_y][curr_x - 1] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x - 1) and (self.get_swiat().get_organizmy()[i].get_y() == curr_y) and (self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze") and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y][curr_x - 1] = None
                            break
        if (curr_y >= 0) and (curr_x + 1 >= 0) and (curr_y < self.get_swiat().get_n()) and (curr_x + 1 < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y][curr_x + 1] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x + 1) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze") and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y][curr_x + 1] = None
                            break
        if (curr_y - 1 >= 0) and (curr_x >= 0) and (curr_y - 1 < self.get_swiat().get_n()) and (curr_x < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y - 1][curr_x] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y - 1) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze")  and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y - 1][curr_x] = None
                            break
        if (curr_y + 1 >= 0) and (curr_x >= 0) and (curr_y + 1 < self.get_swiat().get_n()) and (
                curr_x < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y + 1][curr_x] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y + 1) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze") and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y + 1][curr_x] = None
                            break
        if (curr_y - 1 >= 0) and (curr_x - 1 >= 0) and (curr_y < self.get_swiat().get_n()) and (
                curr_x - 1 < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y - 1][curr_x - 1] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x - 1) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y - 1) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze")  and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y - 1][curr_x - 1] = None
                            break
        if (curr_y + 1 >= 0) and (curr_x - 1 >= 0) and (curr_y + 1< self.get_swiat().get_n()) and (
                curr_x - 1 < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y + 1][curr_x - 1] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x - 1) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y + 1) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze") and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y + 1][curr_x - 1] = None
                            break
        if (curr_y - 1 >= 0) and (curr_x + 1 >= 0) and (curr_y - 1 < self.get_swiat().get_n()) and (
                curr_x + 1 < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y - 1][curr_x + 1] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x + 1) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y - 1) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze") and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y - 1][curr_x + 1] = None
                            break
        if (curr_y + 1 >= 0) and (curr_x + 1 >= 0) and (curr_y + 1 < self.get_swiat().get_n()) and (
                curr_x + 1 < self.get_swiat().get_m()):
            if not (self.get_swiat().get_mapa()[curr_y + 1][curr_x + 1] is None):
                for i in range(len(self.get_swiat().get_organizmy())):
                    if self.get_swiat().get_organizmy()[i] is not None:
                        if (self.get_swiat().get_organizmy()[i].get_x() == curr_x + 1) and (
                                self.get_swiat().get_organizmy()[i].get_y() == curr_y + 1) and (
                                self.get_swiat().get_organizmy()[i].get_rodzaj() == "Zwierze") and not(isinstance(self.get_swiat().get_organizmy()[i], CyberOwca)):
                            if isinstance(self.get_swiat().get_organizmy()[i], Czlowiek):
                                self.get_swiat().set_koniec(True)
                            self.get_swiat().get_organizmy()[i].set_zyje(False)
                            #self.get_swiat().set_events(f'{self.get_swiat().get_events()}{self.get_gatunek()} zabija {self.get_swiat().get_organizmy[i].get_gatunek()}')
                            self.get_swiat().get_do_usuniecia().append(self.get_swiat().get_organizmy()[i])
                            self.get_swiat().get_mapa()[curr_y + 1][curr_x + 1] = None
                            break
        szansa = random.randrange(4)
        if szansa == 0:
            kier = random.randrange(8)
            cur_x = self.get_x()
            cur_y = self.get_y()
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

            if (cur_y + i >= 0) and (cur_y + i < self.get_swiat().get_n()) and (cur_x + j >= 0) and (
                    cur_x + j < self.get_swiat().get_m()):
                if self.get_swiat().get_mapa()[cur_y + i][cur_x + j] is None:
                    nowy_barszcz = BarszczSosnowskiego(cur_y + i, cur_x + j, self.get_swiat())
                    self.get_swiat().get_nowe_organizmy().append(nowy_barszcz)
                    self.get_swiat().get_mapa()[cur_y + i][cur_x + j] = nowy_barszcz
                    self.get_swiat().set_events(
                        self.get_swiat().get_events() + "Wyrosla nowa roslina: " + self.get_gatunek() + "(" + str(
                            cur_y + i) + ", " + str(cur_x + j) + ")\n")

    def kolizja(self, opp_y, opp_x, napastnik):
        from CyberOwca import CyberOwca
        if isinstance(napastnik, CyberOwca):
            lp = -1
            for i in range(len(self.get_swiat().get_organizmy())):
                if self.get_swiat().get_organizmy()[i] is not None:
                    if (self.get_swiat().get_organizmy()[i].get_x() == napastnik.get_x()) and (
                            self.get_swiat().get_organizmy()[i].get_y() == napastnik.get_y()):
                        lp = i
                        break
            self.set_zyje(False)
            self.get_swiat().get_do_usuniecia().append(self)
            self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
            self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = napastnik
            self.get_swiat().get_organizmy()[lp].set_x(self.get_x())
            self.get_swiat().get_organizmy()[lp].set_y(self.get_y())
            print(f'{napastnik.get_gatunek()} zjada {self.get_gatunek()} ({self.get_y()}, {self.get_x()})')
            return
        if isinstance(napastnik, Czlowiek):
            napastnik.get_swiat().set_koniec(True)
        self.get_swiat().get_mapa()[napastnik.get_y()][napastnik.get_x()] = None
        self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = None
        print(f'{napastnik.get_gatunek()} zjada {self.get_gatunek()} i umiera ({self.get_y()}, {self.get_x()})')
        napastnik.set_zyje(False)
        self.set_zyje(False)
        self.get_swiat().get_do_usuniecia().append(self)
        self.get_swiat().get_do_usuniecia().append(napastnik)
