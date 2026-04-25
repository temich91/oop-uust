from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from abc import abstractmethod
from lab4.src.constants import *
import random


class Shape(QWidget):
    def __init__(self, parent, x, y, color):
        super().__init__(parent=parent)
        self.isSelected = False
        self.color = color
        self.penColor = self.color

        side = random.randint(MIN_SHAPE_WIDTH, MAX_SHAPE_WIDTH)

        self.resize(side, side)

        self.move(x - side // 2, y - side // 2)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    @abstractmethod
    def drawShape(self, painter):
        """ Абстрактный метод: реализуется в Circle, Square и т.д. """
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QPen(self.penColor, PEN_WIDTH))
        painter.setBrush(QBrush(self.color))

        self.drawShape(painter)
        painter.end()

    def changeColor(self, newColor):
        self.color = newColor

        if not self.isSelected:
            self.penColor = newColor
        self.update()

    def select(self):
        self.isSelected = True
        self.penColor = QColor("blue")  # Цвет рамки при выделении
        self.update()

    def unselect(self):
        self.isSelected = False
        self.penColor = self.color
        self.update()

    @abstractmethod
    def containsPoint(self, pos):
        """ Проверка попадания курсора в фигуру """
        pass