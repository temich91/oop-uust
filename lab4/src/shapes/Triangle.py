from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import QPoint
from lab4.src.Shape import Shape
from lab4.src.constants import *

class Triangle(Shape):
    def __init__(self, parent, x, y, color):
        super().__init__(parent, x, y, color)

    def drawShape(self, painter):
        polygon = QPolygon([QPoint(self.width() // 2, PEN_WIDTH),
                                 QPoint(PEN_WIDTH, self.height() - PEN_WIDTH),
                                 QPoint(self.width() - PEN_WIDTH, self.height() - PEN_WIDTH)])

        painter.drawPolygon(polygon)

    def containsPoint(self, pos):
        return self.polygon.containsPoint(pos, 0)
