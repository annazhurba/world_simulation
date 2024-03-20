from Roslina import Roslina


class Trawa(Roslina):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(0)
        self.set_inicjatywa(0)
        self.set_wiek(0)
        self.set_gatunek("Trawa")
        self.set_rodzaj("Roslina")
        self.set_znaczek('t')
        self.set_swiat(swiat)
