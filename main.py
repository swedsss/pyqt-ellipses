import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from UI import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.paint = False
        self.ellipse_params = []

        self.btn_paint.clicked.connect(self.do_paint)

    def do_paint(self):
        size = randint(10, min([self.width(), self.height()]))
        left = randint(0, self.width() - size)
        top = randint(0, self.height() - size)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.ellipse_params = [left, top, size, color]
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def draw_ellipse(self, qp):
        left, top, size, color = self.ellipse_params
        qp.setPen(QPen(color, 5))
        qp.drawEllipse(left, top, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec())
