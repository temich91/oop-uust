from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(700, 400))