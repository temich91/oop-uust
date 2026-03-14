from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtWidgets import QWidget
import src.utils.constants as c

class Circle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(c.CIRCLE_RADIUS, c.CIRCLE_RADIUS)
        self.isPainted = True
        self.color = Qt.yellow
        self.fillColor = self.color
        self.blinkPeriod = 1 # секунды

    def setColor(self, newColor: Qt.GlobalColor) -> None:
        """
        Установка нового цвета, отображаемого при мигании.
        :param newColor: Новый цвет.
        :return: None
        """
        self.color = newColor

    def updateColor(self) -> None:
        """
        Меняет цвет заливки кружка.
        :return: None
        """
        if self.isPainted:
            self.fillColor = Qt.transparent
        else:
            self.fillColor = self.color
        self.isPainted = not self.isPainted
        self.update()

    def setBlinkPeriod(self, newPeriod: int):
        """
        Устанавливает период мигания кружка. Время фаз (горит/не горит) одинаково.
        :param newPeriod: новый период (секунды)
        :return: None
        """
        self.blinkPeriod = newPeriod

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(QColor(self.fillColor), Qt.BrushStyle.SolidPattern))
        painter.drawEllipse(0, 0, c.CIRCLE_RADIUS, c.CIRCLE_RADIUS)
