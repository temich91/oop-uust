from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtCore import QSize
from lab3part2.src.Model import Model
from lab3part2.src.NumberEdit import NumberEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(700, 400))
        mainWidget = QWidget(self)
        mainLayout = QHBoxLayout()

        # Логическая модель для обработки значений A, B, C
        self.model = Model()
        self.model.addObserver(self.updateValues) # метод updateValues наблюдает за изменениями в модели

        # Формы для ввода/отображения переменных
        self.widgetA = NumberEdit(self, "A")
        self.widgetA.changed.connect(self.model.setA)
        mainLayout.addWidget(self.widgetA)

        self.widgetB = NumberEdit(self, "B")
        self.widgetB.changed.connect(self.model.setB)
        mainLayout.addWidget(self.widgetB)

        self.widgetC = NumberEdit(self, "C")
        self.widgetC.changed.connect(self.model.setC)
        mainLayout.addWidget(self.widgetC)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def updateValues(self, a, b, c):
        """
        Вызов обновления значений переменных в формах A, B, C из модели.
        """
        self.widgetA.updateValue(a)
        self.widgetB.updateValue(b)
        self.widgetC.updateValue(c)
