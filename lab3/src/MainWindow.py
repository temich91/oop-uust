from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from .Canvas import Canvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Параметры окна
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Контейнер кружочков")

        # Контейнер кругов
        self.circleContainer = Canvas(self)
        self.circleContainer.show()

        # Основной виджет и layout
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.circleContainer)
        self.mainWidget.setLayout(mainLayout)
