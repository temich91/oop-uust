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

    def add(self, pos):
        newCircle = CCircle(self, pos.x(), pos.y())
        newCircle.show()
        self.allCircles.append(newCircle)
        self.update()

    def remove(self, circle):
        self.allCircles.remove(circle)
        circle.setParent(None)
        circle.deleteLater()

    def draw(self):
        for circle in self.allCircles:
            circle.update()

    def select(self, circle):
        self.selectedCircles.append(circle)
        circle.select()

    def unselect(self, circle):
        self.selectedCircles.remove(circle)
        circle.unselect()

    def clearSelection(self):
        for circle in self.selectedCircles:
            circle.unselect()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        # Обработка нажатия ЛКМ
        if event.button() == Qt.LeftButton:
            canvas_pos = event.pos() # точка клика в координатах Canvas
            circlePressed = False # нажат ли хотя бы один круг
            for circle in self.allCircles:
                circ_pos = circle.mapFromParent(canvas_pos) # точка в координатах круга
                if circle.containsPoint(QPoint(circ_pos.x(), circ_pos.y())):
                    print("da")
                    circlePressed = True
                    # если Ctrl нажат, выделение круга инвертируется
                    if event.modifiers() == Qt.ControlModifier:
                        if circle not in self.selectedCircles:
                            self.select(circle)
                        else:
                            self.unselect(circle)

                    # иначе отменяются выделения всех кругов, кроме нажатого сейчас
                    else:
                        self.clearSelection()
                        if circle not in self.selectedCircles:
                            self.select(circle)
                        else:
                            self.unselect(circle)

            # снятие выделения объектов если нажали ни на один из кругов
            if not circlePressed:
                if self.selectedCircles:
                    self.clearSelection()
                self.add(canvas_pos)
                if event.modifiers() == Qt.ControlModifier:
                    self.select(self.allCircles[-1])
