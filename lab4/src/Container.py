from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor
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

    def keyPressEvent(self, event):
        # Обработка нажатия клавиши Delete
        # Удаление всех выделенных кругов
        if event.key() == Qt.Key_Delete:
            for shape in self.allShapes.copy():
                if shape.isSelected:
                    self.removeShape(shape)
        event.accept()

    def mousePressEvent(self, event):
        # Обработка нажатия ЛКМ
        if event.button() == Qt.LeftButton:
            canvas_pos = event.pos() # точка клика в координатах Canvas
            clicked = None
            # Поиск нажатого круга
            for shape in self.allShapes[::-1]:
                circ_pos = shape.mapFromParent(canvas_pos) # точка в координатах круга
                if shape.containsPoint(QPoint(circ_pos.x(), circ_pos.y())):
                    clicked = shape
                    break

            if clicked:
                if clicked.isSelected:
                    clicked.unselect()
                else:
                    if event.modifiers() != Qt.ControlModifier:
                        self.clearSelection()
                    clicked.select()
            else:
                # снятие выделения объектов если нажали ни на один из кругов
                self.clearSelection()
                self.add(canvas_pos)
                if event.modifiers() == Qt.ControlModifier:
                    self.allShapes[-1].select()
        event.accept()
