from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QAction, QColorDialog
from lab4.src.shapes import *
from .Container import Container


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Параметры окна
        self.setMinimumSize(800, 500)
        self.setWindowTitle("Четвертая лаба")

        # Контейнер фигур
        self.container = Container(self)
        self.container.show()

        # Основной виджет и layout
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.container)
        self.mainWidget.setLayout(mainLayout)

        # Меню с выбором фигур и параметрами фигуры
        menubar = self.menuBar()

        shapeMenu = menubar.addMenu("Фигуры")
        circleAction = QAction("Круг", self)
        circleAction.triggered.connect(lambda: self.container.changeShape(Circle))
        squareAction = QAction("Квадрат", self)
        squareAction.triggered.connect(lambda: self.container.changeShape(Square))
        triangleAction = QAction("Треугольник", self)
        triangleAction.triggered.connect(lambda: self.container.changeShape(Triangle))
        rectangleAction = QAction("Прямоугольник", self)
        rectangleAction.triggered.connect(lambda: self.container.changeShape(Rectangle))

        shapeMenu.addAction(circleAction)
        shapeMenu.addAction(squareAction)
        shapeMenu.addAction(triangleAction)
        shapeMenu.addAction(rectangleAction)

        optionsMenu = menubar.addMenu("Параметры фигур")
        changeColorAction = QAction("Изменить цвет", self)
        changeColorAction.triggered.connect(self.chooseColor)
        optionsMenu.addAction(changeColorAction)

    def chooseColor(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.container.updateColor(color)
