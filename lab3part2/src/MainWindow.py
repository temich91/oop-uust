from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSlider, QSpinBox
from PyQt5.QtCore import QSize
from lab3part2.src.Model import Model

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(700, 400))
        mainWidget = QWidget(self)

        self.model = Model()

        mainLayout = QHBoxLayout()

        self.aLayout = QVBoxLayout()
        

        mainLayout.addLayout(self.aLayout)
        mainLayout.addLayout(self.bLayout)
        mainLayout.addLayout(self.cLayout)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
