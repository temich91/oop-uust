from lab4.src.Shape import Shape
from lab4.src.constants import *

class Circle(Shape):
    def __init__(self, parent, x, y, color):
        super().__init__(parent, x, y, color)
        self.radius = max(self.width(), self.height()) // 2
        size = self.radius * 2 + PEN_WIDTH * 2
        self.setFixedSize(size, size)

        self.setGeometry(x - self.radius - PEN_WIDTH,
                         y - self.radius - PEN_WIDTH,
                        size, size)

    def drawShape(self, painter):
        painter.drawEllipse(PEN_WIDTH, PEN_WIDTH, self.radius * 2, self.radius * 2)

    def containsPoint(self, pos):
        centerX = self.width() // 2
        centerY = self.height() // 2
        dx = pos.x() - centerX
        dy = pos.y() - centerY
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= self.radius + PEN_WIDTH
