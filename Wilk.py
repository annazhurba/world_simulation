from Zwierze import Zwierze


class Wilk(Zwierze):

    def __init__(self, y, x, swiat):
        self.set_y(y)
        self.set_x(x)
        self.set_sila(9)
        self.set_inicjatywa(5)
        self.set_wiek(0)
        self.set_gatunek("Wilk")
        self.set_rodzaj("Zwierze")
        self.set_znaczek('W')
        self.set_swiat(swiat)
