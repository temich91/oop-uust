from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QAction
from PyQt5.QtCore import Qt
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

        # Меню
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


        colorMenu = menubar.addMenu("Изменить цвет")
        # save_action.setShortcut("Ctrl+S")

        shapeMenu.addAction(circleAction)
        shapeMenu.addAction(squareAction)
        shapeMenu.addAction(triangleAction)
        shapeMenu.addAction(rectangleAction)
