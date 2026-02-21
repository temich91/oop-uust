from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLCDNumber, QLabel, QPushButton, QCheckBox, \
    QLineEdit, QComboBox, QGroupBox, QSlider, QSpinBox
from PyQt5.QtCore import pyqtSignal, Qt
import utils.constants as c
from CircleWidget import Circle

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
    blinkPeriodChanged = pyqtSignal(int) # изменение периода мигания кружка

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        tabLayout = QGridLayout()
        self.setLayout(tabLayout)

        self.circle = Circle(self)
        self.circle.show()

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

        # размеры шрифта
        fontSizeDesc = QLabel("Размер шрифта: Мин.:")
        maxFontLabel = QLabel("Макс.:")
        self.minFontSpinBox = QSpinBox()
        self.minFontSpinBox.setRange(c.MIN_FONT_SIZE, c.MAX_FONT_SIZE)
        self.minFontSpinBox.setValue(c.DEFAULT_MIN_FONT_SIZE)
        self.minFontSpinBox.valueChanged.connect(self.updateMinFontSize)
        # self.minFontSpinBox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.maxFontSpinBox = QSpinBox()
        self.maxFontSpinBox.setRange(c.MIN_FONT_SIZE, c.MAX_FONT_SIZE)
        self.maxFontSpinBox.setValue(c.DEFAULT_MAX_FONT_SIZE)
        self.maxFontSpinBox.valueChanged.connect(self.updateMaxFontSize)

        fontSizeDescLayout = QHBoxLayout()
        fontSizeDescLayout.addWidget(fontSizeDesc)
        fontSizeDescLayout.addWidget(self.minFontSpinBox)
        fontSizeDescLayout.addWidget(maxFontLabel)
        fontSizeDescLayout.addWidget(self.maxFontSpinBox)
        # fontSizeDescLayout.setSpacing(0)
        fontSizeDescLayout.setContentsMargins(0, 0, 0, 0)

        # ползунок размера шрифта
        self.fontSizeSlider = QSlider(Qt.Orientation.Horizontal)
        self.fontSizeSlider.setMinimum(c.DEFAULT_MIN_FONT_SIZE)
        self.fontSizeSlider.setMaximum(c.DEFAULT_MAX_FONT_SIZE)
        self.fontSizeSlider.setValue(c.DEFAULT_FONT_SIZE)
        self.fontSizeSlider.setSingleStep(c.FONT_SLIDER_STEP)
        self.fontSizeSlider.valueChanged.connect(self.updateFontSize)
        self.fontSizeLabel = QLabel(str(c.DEFAULT_FONT_SIZE))
        fontSizeLayout = QHBoxLayout()
        fontSizeLayout.addWidget(self.fontSizeSlider)
        fontSizeLayout.addWidget(self.fontSizeLabel)

        # мигающий кружок
        circlePeriodLabel = QLabel("Период мигания, с.:")
        self.circlePeriodEdit = QLineEdit()
        self.circlePeriodEdit.setPlaceholderText("Новый период")
        blinkingCircleLayout = QHBoxLayout()
        circleBtn = QPushButton("Обновить")
        circleBtn.clicked.connect(self.updateBlinkPeriod)
        blinkingCircleLayout.addWidget(self.circle)
        blinkingCircleLayout.addWidget(circlePeriodLabel)
        blinkingCircleLayout.addWidget(self.circlePeriodEdit)
        blinkingCircleLayout.addWidget(circleBtn)

        # layout для настроек окна
        appearanceLayout = QVBoxLayout()
        appearanceLayout.addLayout(titleEditLayout)
        appearanceLayout.addWidget(bgColorLabel)
        appearanceLayout.addWidget(self.bgColorDropdown)
        appearanceLayout.addWidget(self.statusBarCheckbox)
        appearanceLayout.addLayout(fontSizeDescLayout)
        appearanceLayout.addLayout(fontSizeLayout)
        appearanceGroupBox = QGroupBox("Внешний вид приложения")
        appearanceGroupBox.setLayout(appearanceLayout)

        # общий layout
        tabLayout.addLayout(stopwatchLayout, 0, 0)
        tabLayout.addWidget(appearanceGroupBox, 1, 0)
        tabLayout.addLayout(blinkingCircleLayout, 2, 0)

    def updateRunningTime(self):
        self.runningTime += 1
        # обновление секундомера
        self.lcd1.display(self.runningTime)
        # обновление мигающего круга
        self.updateCircle()

    def updateWindowTitle(self):
        new_title = self.titleEdit.text()
        self.titleEditRequested.emit(new_title)

    def emitColorChoice(self):
        chosenRGB = self.bgColorDropdown.currentData()
        self.bgColorChanged.emit(chosenRGB)

    def updateStatusBar(self, state):
        self.statusBarChanged.emit(state == Qt.CheckState.Checked)

    def updateFontSize(self, newSize):
        self.fontSizeLabel.setText(str(newSize))
        self.fontSizeChanged.emit(newSize)

    def updateMinFontSize(self, newSize):
        maxFontValue = self.maxFontSpinBox.value()
        if self.minFontSpinBox.value() > maxFontValue:
            self.minFontSpinBox.setValue(maxFontValue)
            return
        self.fontSizeSlider.setMinimum(newSize)

    def updateMaxFontSize(self, newSize):
        minFontValue = self.minFontSpinBox.value()
        if self.maxFontSpinBox.value() < minFontValue:
            self.maxFontSpinBox.setValue(minFontValue)
            return
        self.fontSizeSlider.setMaximum(newSize)

    def updateCircle(self):
        if self.runningTime % self.circle.blinkPeriod == 0:
            if self.circle.isPainted:
                self.circle.setColor(self.bgColorDropdown.currentData())
            else:
                self.circle.setColor(Qt.yellow)
            self.circle.isPainted = not self.circle.isPainted

    def updateBlinkPeriod(self):
        try:
            newPeriod = int(self.circlePeriodEdit.text())
            self.circle.setBlinkPeriod(newPeriod)
            self.blinkPeriodChanged.emit(newPeriod)
        except ValueError:
            return
