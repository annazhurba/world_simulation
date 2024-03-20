from Zwierze import Zwierze


class CyberOwca(Zwierze):

    __target_x = 999
    __target_y = 999
    __odleglosc = 999

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(11)
        self.set_inicjatywa(4)
        self.set_wiek(0)
        self.set_gatunek("CyberOwca")
        self.set_rodzaj("Zwierze")
        self.set_znaczek('c')
        self.set_swiat(swiat)

    def akcja(self):
        from BarszczSosnowskiego import BarszczSosnowskiego
        from Owca import Owca
        barszcze = []
        for i in range (self.get_swiat().get_n()):
            for j in range (self.get_swiat().get_m()):
                if isinstance(self.get_swiat().get_mapa()[i][j], BarszczSosnowskiego):
                    barszcze.append(self.get_swiat().get_mapa()[i][j])
                    x = abs(self.get_swiat().get_mapa()[i][j].get_x() - self.get_x())
                    y = abs(self.get_swiat().get_mapa()[i][j].get_y() - self.get_y())
                    curr_odleglosc = (x*x + y*y)**0.5
                    if curr_odleglosc < self.__odleglosc:
                        self.__odleglosc = curr_odleglosc
                        self.__target_y = self.get_swiat().get_mapa()[i][j].get_y()
                        self.__target_x = self.get_swiat().get_mapa()[i][j].get_x()
        if len(barszcze) == 0:
            self.set_zyje(False)
            self.get_swiat().get_do_usuniecia().append(self)
            self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = None
            owca = Owca(self.get_y(), self.get_x(), self.get_swiat())
            owca.set_wiek(self.set_wiek())
            self.get_swiat().get_nowe_organizmy().append(owca)
            self.get_swiat().get_mapa()[self.get_y()][self.get_x()] = owca
            return
        else:
            curr_x = self.get_x()
            curr_y = self.get_y()
            k = 0
            d = 0
            if self.__target_y > curr_y:
                k += 1
            elif self.__target_y < curr_y:
                k -= 1
            if self.__target_x > curr_x:
                d += 1
            elif self.__target_x < curr_x:
                d -= 1
            if (curr_y + k < self.get_swiat().get_n()) and (curr_y + k >= 0) and (curr_x + d >= 0) and (curr_x + d < self.get_swiat().get_m()):
                if self.get_swiat().get_mapa()[curr_y + k][curr_x + d] is None:
                    self.set_y(curr_y + k)
                    self.set_x(curr_x + d)
                    self.get_swiat().get_mapa()[curr_y][curr_x] = None
                    self.get_swiat().get_mapa()[curr_y + k][curr_x + d] = self
                else:
                    if isinstance(self.get_swiat().get_mapa()[curr_y + k][curr_x + d], BarszczSosnowskiego):
                        print(self.__odleglosc)
                        print(self.__target_y)
                        print(self.__target_x)
                        self.__odleglosc = 999
                        self.__target_x = 999
                        self.__target_y = 999
                    self.get_swiat().get_mapa()[curr_y + k][curr_x + d].kolizja(curr_y + k, curr_x + d, self)
