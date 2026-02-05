from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLCDNumber, QLabel, QPushButton, QCheckBox, \
    QRadioButton, QLineEdit, QComboBox, QGroupBox, QSlider
from PyQt5.QtCore import pyqtSignal, Qt
import utils.constants as c


class MainTab(QWidget):
    """
    Основная вкладка приложения.
    """

    # сигналы для основного окна
    titleEditRequested = pyqtSignal(str) # изменение заголовка окна
    statusBarMessageSent = pyqtSignal(str) # отправка сообщения в строку состояния
    bgColorChanged = pyqtSignal(str) # изменение цвета фона
    statusBarChanged = pyqtSignal(bool) # изменение видимости строки состояния
    fontSizeChanged = pyqtSignal(int) # изменение размера шрифта

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        tab_layout = QGridLayout()
        self.setLayout(tab_layout)

        # отображение времени работы приложения
        self.runningTime = 0
        stopwatchDesc = QLabel("Время работы приложения, сек:")
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
        for colorName, rgb in c.BG_COLOR_TO_CSS_DICT.items():
            self.bgColorDropdown.addItem(colorName, rgb)
        bgColorLabel = QLabel("Фоновый цвет:")
        self.bgColorDropdown.currentIndexChanged.connect(self.emitColorChoice)

        # показать/спрятать строку состояния
        self.statusBarCheckbox = QCheckBox("Строка состояния")
        self.statusBarCheckbox.setChecked(True)
        self.statusBarCheckbox.stateChanged.connect(self.updateStatusBar)

        # размер шрифта
        self.fontSizeDesc = QLabel("Размер шрифта:")
        self.fontSizeSlider = QSlider(Qt.Orientation.Horizontal)
        self.fontSizeSlider.setMinimum(2)
        self.fontSizeSlider.setMaximum(30)
        self.fontSizeSlider.setValue(c.DEFAULT_FONT_SIZE)
        self.fontSizeSlider.setSingleStep(2)
        self.fontSizeSlider.valueChanged.connect(self.changeFontSize)
        self.fontSizeLabel = QLabel(str(c.DEFAULT_FONT_SIZE))
        fontSizeLayout = QHBoxLayout()
        fontSizeLayout.addWidget(self.fontSizeSlider)
        fontSizeLayout.addWidget(self.fontSizeLabel)

        # layout для настроек окна
        appearanceLayout = QVBoxLayout()
        appearanceLayout.addLayout(titleEditLayout)
        appearanceLayout.addWidget(bgColorLabel)
        appearanceLayout.addWidget(self.bgColorDropdown)
        appearanceLayout.addWidget(self.statusBarCheckbox)
        appearanceLayout.addWidget(self.fontSizeDesc)
        appearanceLayout.addLayout(fontSizeLayout)
        appearanceGroupBox = QGroupBox("Внешний вид приложения")
        appearanceGroupBox.setLayout(appearanceLayout)

        # общий layout
        tab_layout.addLayout(stopwatchLayout, 0, 0)
        tab_layout.addWidget(appearanceGroupBox, 1, 0)

    def updateRunningTime(self):
        self.runningTime += 1
        self.lcd1.display(self.runningTime)

    def updateWindowTitle(self):
        new_title = self.titleEdit.text()
        self.titleEditRequested.emit(new_title)

    def emitColorChoice(self):
        chosenRGB = self.bgColorDropdown.currentData()
        self.bgColorChanged.emit(chosenRGB)

    def updateStatusBar(self, state):
        self.statusBarChanged.emit(state == Qt.CheckState.Checked)

    def changeFontSize(self, size):
        self.fontSizeLabel.setText(str(size))
        self.fontSizeChanged.emit(size)
