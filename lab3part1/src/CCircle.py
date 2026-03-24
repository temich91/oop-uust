from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
import random

PEN_WIDTH = 3

class CCircle(QWidget):
    def __init__(self, parent, x, y):
        super().__init__(parent=parent)
        self.radius = random.randint(10, 100)
        # center coords
        self.x = x
        self.y = y
        self.color = QColor(random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))
        self.penColor = self.color
        self.setGeometry(x - self.radius, y - self.radius,
                        self.radius * 2 + PEN_WIDTH * 2, self.radius * 2 + PEN_WIDTH * 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(self.penColor, PEN_WIDTH))
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(PEN_WIDTH, PEN_WIDTH, self.radius * 2, self.radius * 2)
        painter.end()

    def select(self):
        self.penColor = QColor("blue")
        self.update()

    def unselect(self):
        self.penColor = self.color
        self.update()

    def containsPoint(self, pos):
        centerX = self.width() // 2
        centerY = self.height() // 2
        dx = pos.x() - centerX
        dy = pos.y() - centerY
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= self.radius + PEN_WIDTH
