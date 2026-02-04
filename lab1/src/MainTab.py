from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLCDNumber, QLabel, QPushButton, QCheckBox, \
    QRadioButton, QLineEdit, QComboBox
from PyQt5.QtCore import pyqtSignal

class MainTab(QWidget):
    """
    Основная вкладка приложения.
    """

    # сигналы для основного окна
    titleEditRequested = pyqtSignal(str) # изменение заголовка окна
    statusBarMessageSent = pyqtSignal(str) # отправка сообщения в статус бар
    bgColorChanged = pyqtSignal(str) # изменение цвета фона

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        tab_layout = QGridLayout()
        self.setLayout(tab_layout)

        # отображение времени работы приложения
        self.runningTime = 0
        stopwatchDesc = QLabel("Время работы приложения:")
        self.lcd1 = QLCDNumber()
        stopwatchLayout = QHBoxLayout()
        stopwatchLayout.addWidget(stopwatchDesc)
        stopwatchLayout.addWidget(self.lcd1)

        # форма настроек внешнего вида окна
        # заголовок окна
        self.titleEdit = QLineEdit()
        self.titleEdit.setPlaceholderText("Новый заголовок окна")
        titleEditBtn = QPushButton("Нажми меня")
        titleEditBtn.pressed.connect(self.updateWindowTitle)
        titleEditLayout = QHBoxLayout()
        titleEditLayout.addWidget(self.titleEdit)
        titleEditLayout.addWidget(titleEditBtn)

        # цвет фона
        self.bgColorDropdown = QComboBox()
        self.bgColorDropdown.addItems(["Белый", "Синий", "Зеленый", "Желтый", "Оранжевый", "Розовый"])
        bgColorLabel = QLabel("Выберите фоновый цвет:")
        self.bgColorDropdown.currentIndexChanged.connect(self.emitColorChoice)

        appearencaLayout = QVBoxLayout()
        appearencaLayout.addLayout(titleEditLayout)
        appearencaLayout.addWidget(bgColorLabel)
        appearencaLayout.addWidget(self.bgColorDropdown)

        # общий layout
        tab_layout.addLayout(stopwatchLayout, 0, 0)
        tab_layout.addLayout(appearencaLayout, 1, 0)

    def updateRunningTime(self):
        self.runningTime += 1
        self.lcd1.display(self.runningTime)

    def updateWindowTitle(self):
        new_title = self.titleEdit.text()
        self.titleEditRequested.emit(new_title)
        self.statusBarMessageSent.emit("Изменен заголовок окна")

    def emitColorChoice(self, index):
        chosenColor = self.bgColorDropdown.currentText()
        self.bgColorChanged.emit(chosenColor)
