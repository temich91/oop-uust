from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor

from lab4.src.constants import COORDS_MOVEMENT
from lab4.src.shapes import *
from lab4.src.Shape import Shape

class Container(QWidget):
    """
    Виджет для отображения кругов.

    Представляет собой компоновщик кругов, который умеет создавать, удалять,
    выделять и отрисовывать виджеты-круги на окне приложения.
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.currentShape = Circle
        self.currentColor = QColor("red")

        self.allShapes = []
        self.selectedCircles = []
        self.setFocusPolicy(Qt.StrongFocus) # виджет принимает события клавитуры

    def add(self, pos):
        newShape = self.currentShape(self, pos.x(), pos.y(), self.currentColor)
        if not self.checkBorder(newShape, 0, 0):
            newShape.show()
            self.allShapes.append(newShape)
            self.update()

    def changeShape(self, newShape):
        self.currentShape = newShape

    def removeShape(self, shape):
        """
        Полностью удаляет виджет фигуры.
        """
        if shape in self.allShapes:
            self.allShapes.remove(shape)

        shape.setParent(None)
        shape.deleteLater()
        self.update()

    def draw(self):
        for shape in self.allShapes:
            shape.update()

    def clearSelection(self):
        for shape in self.allShapes[:]:
            shape.unselect()

    def moveShapes(self, dx, dy):
        if any(self.checkBorder(shape, dx, dy) for shape in self.allShapes):
            return
        for shape in self.allShapes:
            if shape.isSelected:
                shape.move(shape.x() + dx, shape.y() + dy)

    def updateColor(self, newColor):
        self.currentColor = newColor
        for shape in self.allShapes:
            if shape.isSelected:
                shape.changeColor(newColor)
        self.update()

    def checkBorder(self, shape, dx, dy):
        containerRect = self.rect()
        shapeRect = shape.geometry().translated(dx, dy)

        return not containerRect.contains(shapeRect)

    def keyPressEvent(self, event):
        # Обработка нажатия клавиши Delete
        # Удаление всех выделенных фигур
        if event.key() == Qt.Key_Delete:
            for shape in self.allShapes.copy():
                if shape.isSelected:
                    self.removeShape(shape)

        # Перемещение фигур по нажатию стрелок
        dx, dy = 0, 0 # изменение координат в пикселях
        if event.key() == Qt.Key_Left:
            dx -= COORDS_MOVEMENT
        if event.key() == Qt.Key_Right:
            dx += COORDS_MOVEMENT
        if event.key() == Qt.Key_Up:
            dy -= COORDS_MOVEMENT
        if event.key() == Qt.Key_Down:
            dy += COORDS_MOVEMENT

        if dx or dy:
            self.moveShapes(dx, dy)
        event.accept()

    def mousePressEvent(self, event):
        # Обработка нажатия ЛКМ
        if event.button() == Qt.LeftButton:
            canvas_pos = event.pos() # точка клика в координатах контейнера
            clicked = None
            # Поиск нажатой фигуры
            for shape in self.allShapes[::-1]:
                circ_pos = shape.mapFromParent(canvas_pos) # точка в координатах фигуры
                if shape.containsPoint(circ_pos):
                    clicked = shape
                    break

            if clicked:
                if clicked.isSelected:
                    if event.modifiers() != Qt.ControlModifier:
                        self.clearSelection()
                    clicked.unselect()
                else:
                    if event.modifiers() != Qt.ControlModifier:
                        self.clearSelection()
                    clicked.select()
            else:
                # снятие выделения объектов если нажали ни на один из кругов
                self.clearSelection()
                self.add(canvas_pos)
                if event.modifiers() & Qt.ControlModifier:
                    self.allShapes[-1].select()
        event.accept()
