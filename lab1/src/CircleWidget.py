from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtWidgets import QWidget
import utils.constants as c

class Circle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(c.CIRCLE_RADIUS, c.CIRCLE_RADIUS)
        self.isPainted = True
        self.color = Qt.yellow
        self.blinkPeriod = 1 # секунды

    def setColor(self, color: str) -> None:
        """
        Меняет цвет кружка.
        :param color:
        :return: None
        """
        self.color = color
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
        painter.setBrush(QBrush(QColor(self.color), Qt.BrushStyle.SolidPattern))
        painter.drawEllipse(0, 0, c.CIRCLE_RADIUS, c.CIRCLE_RADIUS)
