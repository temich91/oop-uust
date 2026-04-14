from PyQt5.QtCore import QPoint
from lab4.src.Shape import Shape
from lab4.src.constants import *

class Rectangle(Shape):
    def __init__(self, parent, x, y, color):
        super().__init__(parent, x, y, color)

        self.setGeometry(x - self.width() // 2,
                         y - self.height() // 2,
                        self.width(), self.height())

    def drawShape(self, painter):
        painter.drawRect(PEN_WIDTH, PEN_WIDTH,
                         self.width() - 2 * PEN_WIDTH,
                         self.height() - 2 * PEN_WIDTH)

    def containsPoint(self, pos):
        return self.rect().contains(pos)
