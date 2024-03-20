from abc import ABC, abstractmethod


class Organizm(ABC):
    import Swiat
    __gatunek: str = None
    __rodzaj: str = None
    __sila: int = None
    __inicjatywa: int = None
    __wiek: int = None
    __x: int = None
    __y: int = None
    __znaczek: chr = None
    __swiat: Swiat = None
    __zyje: bool = True

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def get_gatunek(self):
        return self.__gatunek

    def get_rodzaj(self):
        return self.__rodzaj

    def get_sila(self):
        return self.__sila

    def get_inicjatywa(self):
        return self.__inicjatywa

    def get_wiek(self):
        return self.__wiek

    def get_znaczek(self):
        return self.__znaczek

    def get_swiat(self):
        return self.__swiat

    def get_zyje(self):
        return self.__zyje

    def set_y(self, y):
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_gatunek(self, gatunek):
        self.__gatunek = gatunek

    def set_rodzaj(self, rodzaj):
        self.__rodzaj = rodzaj

    def set_sila(self, sila):
        self.__sila = sila

    def set_inicjatywa(self, inic):
        self.__inicjatywa = inic

    def set_wiek(self, wiek):
        self.__wiek = wiek

    def set_znaczek(self, znaczek):
        self.__znaczek = znaczek

    def set_swiat(self, swiat):
        self.__swiat = swiat

    def set_zyje(self, zyje):
        self.__zyje = zyje

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, opp_y, opp_x, napastnik):
        pass
    #destructor??