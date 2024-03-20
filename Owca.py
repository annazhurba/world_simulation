from Zwierze import Zwierze


class Owca(Zwierze):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(4)
        self.set_inicjatywa(4)
        self.set_wiek(0)
        self.set_gatunek("Owca")
        self.set_rodzaj("Zwierze")
        self.set_znaczek('O')
        self.set_swiat(swiat)
