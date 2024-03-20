from Swiat import Swiat
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import sys


keyy = None

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Wirtualny Swiat - Anna Zhurba, 192038")
        self.setFixedSize(800, 800)

    def keyPressEvent(self, e):
        global keyy
        if e.key() == Qt.Key_Up:
            keyy = 38
        elif e.key() == Qt.Key_Down:
            keyy = 40
        elif e.key() == Qt.Key_Right:
            keyy = 39
        elif e.key() == Qt.Key_Left:
            #global keyy
            keyy = 37
        elif e.key() == Qt.Key_N:
            keyy = 78
        elif e.key() == Qt.Key_A:
            keyy = 65
        elif e.key() == Qt.Key_S:
            keyy = 83
        elif e.key() == Qt.Key_L:
            keyy = 76


n = int(input("Podaj wysokosc swiata\n"))
m = int(input("Podaj szerokosc swiata\n"))

swiat = Swiat(n, m)
app = QApplication(sys.argv)
window = MainWindow()

swiat.rysuj_swiat(window, app)
swiat.set_key(keyy)
while not swiat.get_koniec():
    swiat.set_key(keyy)
    if (swiat.get_key() is not None) or (swiat.get_licznik_tur() == 0):
        swiat.wykonaj_ture(window, app)
exit(0)
