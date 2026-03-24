from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from .CCircle import CCircle

class Canvas(QWidget):
    """
    Виджет для отображения кругов.

    Представляет собой компоновщик кругов, который умеет создавать, удалять,
    выделять и отрисовывать виджеты-круги на окне приложения.
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.allCircles = []
        self.selectedCircles = []
        self.setFocusPolicy(Qt.StrongFocus) # виджет принимает события клавитуры

    def add(self, pos):
        newCircle = CCircle(self, pos.x(), pos.y())
        newCircle.show()
        self.allCircles.append(newCircle)
        self.update()

    def removeCircle(self, circle):
        """
        Полностью удаляет виджет круга.
        """
        if circle in self.allCircles:
            self.allCircles.remove(circle)
        if circle in self.selectedCircles:
            self.selectedCircles.remove(circle)
        circle.setParent(None)
        circle.deleteLater()
        self.update()

    def draw(self):
        for circle in self.allCircles:
            circle.update()

    def select(self, circle):
        self.selectedCircles.append(circle)
        circle.select()

    def unselectCircle(self, circle):
        if circle in self.selectedCircles:
            self.selectedCircles.remove(circle)
        circle.unselect()

    def clearSelection(self):
        for circle in self.selectedCircles[:]:
            circle.unselect()
        self.selectedCircles.clear()

    def keyPressEvent(self, event):
        # Обработка нажатия клавиши Delete
        # Удаление всех выделенных кругов
        if event.key() == Qt.Key_Delete:
            c = 0
            for circle in self.selectedCircles.copy():
                self.removeCircle(circle)
        event.accept()

    def mousePressEvent(self, event):
        # Обработка нажатия ЛКМ
        if event.button() == Qt.LeftButton:
            canvas_pos = event.pos() # точка клика в координатах Canvas
            clickedCircle = None
            # Поиск нажатого круга
            for circle in self.allCircles:
                circ_pos = circle.mapFromParent(canvas_pos) # точка в координатах круга
                if circle.containsPoint(QPoint(circ_pos.x(), circ_pos.y())):
                    clickedCircle = circle
                    break

            if clickedCircle:
                if clickedCircle in self.selectedCircles:
                    self.unselectCircle(clickedCircle)
                else:
                    if event.modifiers() != Qt.ControlModifier:
                        self.clearSelection()
                    self.select(clickedCircle)
            else:
                # снятие выделения объектов если нажали ни на один из кругов
                self.clearSelection()
                self.add(canvas_pos)
                if event.modifiers() == Qt.ControlModifier:
                    self.select(self.allCircles[-1])
        event.accept()
