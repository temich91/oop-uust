from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from abc import abstractmethod
from lab4.src.constants import *
import random

class Shape(QWidget):
    def __init__(self, parent, x, y, color):
        super().__init__(parent=parent)
        self.isSelected = False

        # координаты центра
        self.x = x
        self.y = y

        self.color = color
        self.penColor = self.color

        # размеры виджета, на котором рисуется фигура

        self.setFixedSize(random.randint(MIN_SHAPE_WIDTH, MAX_SHAPE_WIDTH),
                          random.randint(MIN_SHAPE_WIDTH, MAX_SHAPE_WIDTH))
        self.setGeometry(x - self.width(), y - self.height(),
                        self.width(), self.height())

    @abstractmethod
    def drawShape(self, painter):
        """
        Абстрактный метод отрисовки фигуры с помощью QPainter.
        """
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
        self.update()

    def select(self):
        self.isSelected = True
        self.penColor = QColor("blue")
        self.update()

    def unselect(self):
        self.isSelected = False
        self.penColor = self.color
        self.update()

    def checkBorders(self):
        pass

    @abstractmethod
    def containsPoint(self, pos):
        """
        Проверка принадлежности точки с координатами pos фигуре.
        """
        pass
