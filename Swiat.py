import sys
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtGui import QPalette, QColor
from Czlowiek import Czlowiek


keyy = None


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Swiat:
    __n: int = None
    __m: int = None
    __mapa = []
    __organizmy = []
    __nowe_organizmy = []
    __do_usuniecia = []
    __events: str = None
    __key = None
    __licznik_tur: int = 0
    __koniec: bool = False

    def __init__(self, n, m):
        from Wilk import Wilk
        from Owca import Owca
        from Lis import Lis
        from Antylopa import Antylopa
        from Czlowiek import Czlowiek
        from Zolw import Zolw
        from Trawa import Trawa
        from Mlecz import Mlecz
        from Guarana import Guarana
        from WilczeJagody import WilczeJagody
        from BarszczSosnowskiego import BarszczSosnowskiego
        from CyberOwca import CyberOwca
        self.__n = n
        self.__m = m
        self.__licznik_tur = 1
        self.__mapa = [[None for wdt in range(m)] for ht in range(n)]
        self.__organizmy = [None for itr in range(n*m)]
        self.__nowe_organizmy = [None for itr in range(n*m)]
        self.__do_usuniecia = [None for itr in range(n*m)]

        #dodaj organizmy
        lis1 = Lis(3, 5, self)
        self.__mapa[3][5] = lis1
        self.__organizmy.append(lis1)
        lis2 = Lis(6, 0, self)
        self.__mapa[6][0] = lis2
        self.__organizmy.append(lis2)

        wilk1 = Wilk(1, 2, self)
        self.__mapa[1][2] = wilk1
        self.__organizmy.append(wilk1)
        wilk2 = Wilk(2, 6, self)
        self.__mapa[2][6] = wilk2
        self.__organizmy.append(wilk2)

        owca1 = Owca(4, 3, self)
        self.__mapa[4][3] = owca1
        self.__organizmy.append(owca1)
        owca2 = Owca(1, 5, self)
        self.__mapa[1][5] = owca2
        self.__organizmy.append(owca2)

        cowca1 = CyberOwca(5, 7, self)
        self.__mapa[5][7] = cowca1
        self.__organizmy.append(cowca1)

        anty1 = Antylopa(1, 7, self)
        self.__mapa[1][7] = anty1
        self.__organizmy.append(anty1)
        anty2 = Antylopa(0, 9, self)
        self.__mapa[0][9] = anty2
        self.__organizmy.append(anty2)

        czlowiek = Czlowiek(9, 4, self)
        self.__mapa[9][4] = czlowiek
        self.__organizmy.append(czlowiek)

        zolw1 = Zolw(7, 6, self)
        self.__mapa[7][6] = zolw1
        self.__organizmy.append(zolw1)
        zolw2 = Zolw(7, 7, self)
        self.__mapa[7][7] = zolw2
        self.__organizmy.append(zolw2)

        trawa = Trawa(7, 3, self)
        self.__mapa[7][3] = trawa
        self.__organizmy.append(trawa)

        mlecz = Mlecz(9, 9, self)
        self.__mapa[9][9] = mlecz
        self.__organizmy.append(mlecz)

        guarana = Guarana(5, 5, self)
        self.__mapa[5][5] = guarana
        self.__organizmy.append(guarana)

        wj = WilczeJagody(8, 8, self)
        self.__mapa[8][8] = wj
        self.__organizmy.append(wj)

        bs = BarszczSosnowskiego(3, 8, self)
        self.__mapa[3][8] = bs
        self.__organizmy.append(bs)

    def get_n(self):
        return self.__n

    def get_m(self):
        return self.__m

    def get_licznik_tur(self):
        return self.__licznik_tur

    def get_koniec(self):
        return self.__koniec

    def get_mapa(self):
        return self.__mapa

    def get_events(self):
        return self.__events

    def get_key(self):
        return self.__key

    def get_organizmy(self):
        return self.__organizmy

    def get_nowe_organizmy(self):
        return self.__nowe_organizmy

    def get_do_usuniecia(self):
        return self.__do_usuniecia

    def set_n(self, n):
        self.__n = n

    def set_m(self, m):
        self.__m = m

    def set_licznik_tur(self, liczba):
        self.__licznik_tur = liczba

    def set_events(self, events):
        self.__events = events

    def set_key(self, key):
        self.__key = key

    def set_organizmy(self, organizmy):
        self.__organizmy = organizmy

    def set_nowe_organizmy(self, nowe_org):
        self.__nowe_organizmy = nowe_org

    def set_do_usuniecia(self, do_usun):
        self.__do_usuniecia = do_usun

    def set_koniec(self, koniec):
        self.__koniec = koniec

    def set_mapa(self, mapa):
        self.__mapa = mapa

    def zapisz_gre(self):
        f = open("wirtualnyswiatpython.txt", "w")
        f.write(str(self.__n))
        f.write("\n")
        f.write(str(self.__m))
        f.write("\n")
        f.write(str(len(self.__organizmy)))
        f.write("\n")
        f.write(str(self.__licznik_tur))
        f.write("\n")
        for i in range(len(self.__organizmy)):
            if not(self.__organizmy[i] is None):
                f.write(self.__organizmy[i].get_gatunek())
                f.write("\n")
                f.write(str(self.__organizmy[i].get_y()))
                f.write("\n")
                f.write(str(self.__organizmy[i].get_x()))
                f.write("\n")
                f.write(self.__organizmy[i].get_rodzaj())
                f.write("\n")
                f.write(str(self.__organizmy[i].get_sila()))
                f.write("\n")
                f.write(str(self.__organizmy[i].get_inicjatywa()))
                f.write("\n")
                f.write(str(self.__organizmy[i].get_wiek()))
                f.write("\n")
                if isinstance(self.__organizmy[i], Czlowiek):
                    czlowiek: Czlowiek = self.__organizmy[i]
                    f.write(str(czlowiek.get_superpower_tury()))
                    f.write("\n")
        f.close()

    def wczytaj_gre(self):
        from Wilk import Wilk
        from Owca import Owca
        from Lis import Lis
        from Antylopa import Antylopa
        from Zolw import Zolw
        from Trawa import Trawa
        from Mlecz import Mlecz
        from Guarana import Guarana
        from WilczeJagody import WilczeJagody
        from BarszczSosnowskiego import BarszczSosnowskiego
        from Czlowiek import Czlowiek
        f = open("wirtualnyswiatpython.txt", "r")
        self.__n = int(f.readline())
        self.__m = int(f.readline())
        org_size = int(f.readline()) - self.__n*self.__m
        self.__licznik_tur = int(f.readline())
        for i in range(org_size):
            gatunek1 = str(f.readline())
            gatunek = gatunek1.partition("\n")[0]
            y = int(f.readline())
            x = int(f.readline())
            if gatunek == "Wilk":
                wilk = Wilk(y, x, self)
                wilk.set_rodzaj(f.readline())
                wilk.set_sila(int(f.readline()))
                wilk.set_inicjatywa(int(f.readline()))
                wilk.set_wiek(int(f.readline()))
                self.__organizmy.append(wilk)
                self.__mapa[y][x] = wilk
            elif gatunek == "Owca":
                owca = Owca(y, x, self)
                owca.set_rodzaj(f.readline())
                owca.set_sila(int(f.readline()))
                owca.set_inicjatywa(int(f.readline()))
                owca.set_wiek(int(f.readline()))
                self.__organizmy.append(owca)
                self.__mapa[y][x] = owca
            elif gatunek == "Lis":
                lis = Lis(y, x, self)
                lis.set_rodzaj(f.readline())
                lis.set_sila(int(f.readline()))
                lis.set_inicjatywa(int(f.readline()))
                lis.set_wiek(int(f.readline()))
                self.__organizmy.append(lis)
                self.__mapa[y][x] = lis
            elif gatunek == "Antylopa":
                anty = Antylopa(y, x, self)
                anty.set_rodzaj(f.readline())
                anty.set_sila(int(f.readline()))
                anty.set_inicjatywa(int(f.readline()))
                anty.set_wiek(int(f.readline()))
                self.__organizmy.append(anty)
                self.__mapa[y][x] = anty
            elif gatunek == "Zolw":
                zolw = Zolw(y, x, self)
                zolw.set_rodzaj(f.readline())
                zolw.set_sila(int(f.readline()))
                zolw.set_inicjatywa(int(f.readline()))
                zolw.set_wiek(int(f.readline()))
                self.__organizmy.append(zolw)
                self.__mapa[y][x] = zolw
            elif gatunek == "Trawa":
                trawa = Trawa(y, x, self)
                trawa.set_rodzaj(f.readline())
                trawa.set_sila(int(f.readline()))
                trawa.set_inicjatywa(int(f.readline()))
                trawa.set_wiek(int(f.readline()))
                self.__organizmy.append(trawa)
                self.__mapa[y][x] = trawa
            elif gatunek == "Mlecz":
                mlecz = Mlecz(y, x, self)
                mlecz.set_rodzaj(f.readline())
                mlecz.set_sila(int(f.readline()))
                mlecz.set_inicjatywa(int(f.readline()))
                mlecz.set_wiek(int(f.readline()))
                self.__organizmy.append(mlecz)
                self.__mapa[y][x] = mlecz
            elif gatunek == "Guarana":
                guarana = Guarana(y, x, self)
                guarana.set_rodzaj(f.readline())
                guarana.set_sila(int(f.readline()))
                guarana.set_inicjatywa(int(f.readline()))
                guarana.set_wiek(int(f.readline()))
                self.__organizmy.append(guarana)
                self.__mapa[y][x] = guarana
            elif gatunek == "WilczeJagody":
                wj = WilczeJagody(y, x, self)
                wj.set_rodzaj(f.readline())
                wj.set_sila(int(f.readline()))
                wj.set_inicjatywa(int(f.readline()))
                wj.set_wiek(int(f.readline()))
                self.__organizmy.append(wj)
                self.__mapa[y][x] = wj
            elif gatunek == "BarszczSosnowskiego":
                bs = BarszczSosnowskiego(y, x, self)
                bs.set_rodzaj(f.readline())
                bs.set_sila(int(f.readline()))
                bs.set_inicjatywa(int(f.readline()))
                bs.set_wiek(int(f.readline()))
                self.__organizmy.append(bs)
                self.__mapa[y][x] = bs
            elif gatunek == "Czlowiek":
                czlowiek = Czlowiek(y, x, self)
                czlowiek.set_rodzaj(f.readline())
                czlowiek.set_sila(int(f.readline()))
                czlowiek.set_inicjatywa(int(f.readline()))
                czlowiek.set_wiek(int(f.readline()))
                czlowiek.set_superpower_tury(int(f.readline()))
                self.__organizmy.append(czlowiek)
                self.__mapa[y][x] = czlowiek
        f.close()

    def rysuj_swiat(self, window, app):
        from Wilk import Wilk
        from Owca import Owca
        from Lis import Lis
        from Antylopa import Antylopa
        from Zolw import Zolw
        from Trawa import Trawa
        from Mlecz import Mlecz
        from Guarana import Guarana
        from WilczeJagody import WilczeJagody
        from BarszczSosnowskiego import BarszczSosnowskiego
        from CyberOwca import CyberOwca
        layout = QGridLayout()
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__mapa[i][j] is None:
                    layout.addWidget(Color('white'), i, j)
                else:
                    if isinstance(self.__mapa[i][j], Wilk):
                        layout.addWidget(Color('darkGray'), i, j)
                    elif isinstance(self.__mapa[i][j], Owca):
                        layout.addWidget(Color('lightGray'), i, j)
                    elif isinstance(self.__mapa[i][j], Lis):
                        layout.addWidget(Color('orange'), i, j)
                    elif isinstance(self.__mapa[i][j], Antylopa):
                        layout.addWidget(Color('brown'), i, j)
                    elif isinstance(self.__mapa[i][j], Zolw):
                        layout.addWidget(Color('darkGreen'), i, j)
                    elif isinstance(self.__mapa[i][j], Trawa):
                        layout.addWidget(Color('lightGreen'), i, j)
                    elif isinstance(self.__mapa[i][j], Mlecz):
                        layout.addWidget(Color('yellow'), i, j)
                    elif isinstance(self.__mapa[i][j], Guarana):
                        layout.addWidget(Color('magenta'), i, j)
                    elif isinstance(self.__mapa[i][j], WilczeJagody):
                        layout.addWidget(Color('red'), i, j)
                    elif isinstance(self.__mapa[i][j], BarszczSosnowskiego):
                        layout.addWidget(Color('darkCyan'), i, j)
                    elif isinstance(self.__mapa[i][j], CyberOwca):
                        layout.addWidget(Color('cyan'), i, j)
                    elif isinstance(self.__mapa[i][j], Czlowiek):
                        layout.addWidget(Color('black'), i, j)
        self.set_key(keyy)
        widget = QWidget()
        widget.setLayout(layout)
        window.setCentralWidget(widget)
        window.show()
        app.exec()

    def wykonaj_ture(self, window, app):
        self.get_nowe_organizmy().clear()
        self.get_do_usuniecia().clear()
        self.set_licznik_tur(self.get_licznik_tur() + 1)
        for i in range(len(self.get_organizmy())):
            if not(self.get_organizmy()[i] is None):
                if self.get_organizmy()[i].get_zyje():
                    self.get_organizmy()[i].set_wiek(self.get_organizmy()[i].get_wiek() + 1)
        self.set_events("")
        for i in range(len(self.get_organizmy())):
            if not(self.get_organizmy()[i] is None):
                if self.get_organizmy()[i].get_zyje():
                    self.get_organizmy()[i].akcja()
        if len(self.get_do_usuniecia()) != 0:
            self.usun_zwierzeta()
        if len(self.get_nowe_organizmy()) != 0:
            self.dodaj_nowe_zwierzeta()
        if self.__key == 83:
            self.zapisz_gre()
        elif self.__key == 76:
            self.wczytaj_gre()
        self.__key = None
        self.rysuj_swiat(window, app)

    def dodaj_nowe_zwierzeta(self):
        for i in range(len(self.get_nowe_organizmy())):
            j = 0
            while (j != len(self.get_organizmy())) and (self.get_organizmy()[j] is not None) and (self.get_organizmy()[j].get_inicjatywa() >= self.get_nowe_organizmy()[i].get_inicjatywa()):
                j += 1
            if j > 0:
                self.get_organizmy().insert(j - 1, self.get_nowe_organizmy()[i])
            else:
                self.get_organizmy().insert(0, self.get_nowe_organizmy()[i])

    def usun_zwierzeta(self):
        for i in range(len(self.get_do_usuniecia())):
            for j in range(len(self.get_organizmy())):
                if self.get_organizmy()[j] is not None:
                    if (self.get_organizmy()[j].get_x() == self.get_do_usuniecia()[i].get_x()) and (self.get_organizmy()[j].get_y() == self.get_do_usuniecia()[i].get_y()):
                        self.get_organizmy().pop(j)
                        break;
