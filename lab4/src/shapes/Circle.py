from lab4.src.Shape import Shape
from lab4.src.constants import *

class Circle(Shape):
    def drawShape(self, painter):
        painter.drawEllipse(PEN_WIDTH, PEN_WIDTH,
                            self.width() - 2 * PEN_WIDTH,
                            self.height() - 2 * PEN_WIDTH)

    def containsPoint(self, pos):
        radius = self.width() // 2
        center = self.rect().center()
        dist = ((pos.x() - center.x()) ** 2 + (pos.y() - center.y()) ** 2) ** 0.5
        return dist <= radius
