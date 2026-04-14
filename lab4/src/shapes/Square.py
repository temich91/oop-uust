from PyQt5.QtCore import QPoint
from lab4.src.Shape import Shape
from lab4.src.constants import *

class Square(Shape):
    def __init__(self, parent, x, y, color):
        super().__init__(parent, x, y, color)
        self.size = max(self.width(), self.height())
        size = self.size + PEN_WIDTH * 2
        self.setFixedSize(size, size)

        self.setGeometry(x - self.size // 2,
                         y - self.size // 2,
                         size, size)

    def drawShape(self, painter):
        painter.drawRect(PEN_WIDTH, PEN_WIDTH,
                         self.size - 2 * PEN_WIDTH,
                         self.size - 2 * PEN_WIDTH)

    def containsPoint(self, pos):
        return self.rect().contains(pos)
