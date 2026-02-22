import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStatusBar, QWidget, QTabWidget,
                             QWIDGETSIZE_MAX, QHBoxLayout, QMenuBar)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QCursor, QFont
from MainTab import MainTab
from SpamTab import SpamTab
import utils.constants as c

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # служебные поля
        self.timer = QTimer(self)
        self.timer.start(c.TIMER_PERIOD)
        self.timer.timeout.connect(self.sendSignal)
        self.setCursor(QCursor(Qt.UpArrowCursor))

        # компоненты окна приложения
        self.setStatusBar(QStatusBar())

        menuBar = QMenuBar()
        menuBar.addAction("Свернуть окно", self.showMinimized)
        menuBar.addAction("Закрыть окно", self.close)
        self.setMenuBar(menuBar)
        self.setWindowTitle("NU PRIVET")

        self.mainWidget = QWidget(self)
        mainWidgetLayout = QHBoxLayout()
        mainWidgetLayout.setContentsMargins(0, 0, 0, 0)
        mainWidgetLayout.setSpacing(0)
        self.mainWidget.setLayout(mainWidgetLayout)
        self.setCentralWidget(self.mainWidget)

        # размеры окна
        self.setMinimumSize(600, 400)
        self.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)
        self.setStyleSheet(f"background-color: {c.DEFAULT_BG_COLOR}; font-size: {c.DEFAULT_FONT_SIZE}px;")

        # вкладки
        self.mainTab = MainTab(self)
        self.spamTab = SpamTab(self)

        self.mainTabDialog = QTabWidget(self.mainWidget)
        self.mainTabDialog.addTab(self.mainTab, "knopochki")
        self.mainTabDialog.addTab(self.spamTab, "spam")

        self.mainTab.titleEditRequested.connect(self.changeWindowTitle)
        self.mainTab.statusBarMessageSent.connect(self.showStatusBarMessage)
        self.mainTab.bgColorChanged.connect(self.changeBgColor)
        self.mainTab.statusBarChanged.connect(self.updateStatusBar)
        self.mainTab.fontSizeChanged.connect(self.updateFontSize)
        self.mainTab.blinkPeriodChanged.connect(self.updateBlinkPeriod)

        self.mainWidget.layout().addWidget(self.mainTabDialog)

    def sendSignal(self):
        self.mainTab.updateRunningTime()

    def changeWindowTitle(self, newTitle):
        if newTitle == self.windowTitle():
            return
        self.setWindowTitle(newTitle)
        self.showStatusBarMessage("Изменен заголовок окна")

    def showStatusBarMessage(self, message):
        self.statusBar().showMessage(message, msecs=c.STATUSBAR_MESSAGE_TIMEOUT)

    def changeBgColor(self, newRGB):
        styleSheet = self.styleSheet()
        newBg = f"background-color: {newRGB}"
        if "background-color" in styleSheet:
            bgColorIdx = styleSheet.index("background-color: ")
            currentBg = styleSheet[bgColorIdx: bgColorIdx + 25]
            newStyleSheet = styleSheet.replace(currentBg, newBg)
            self.setStyleSheet(newStyleSheet)
            self.showStatusBarMessage("Изменен цвет фона")
        else:
            self.setStyleSheet(styleSheet + newBg)

    def updateStatusBar(self, isVisible):
        self.statusBar().setVisible(isVisible)

    def updateFontSize(self, newSize):
        styleSheet = self.styleSheet()
        newFontSize = f"font-size: {newSize}px"
        if "font-size" in styleSheet:
            fontSizeIdx = styleSheet.index("font-size: ")
            pxIdx = styleSheet.index("px")
            currentSize = styleSheet[fontSizeIdx: pxIdx + 2]
            newStyleSheet = styleSheet.replace(currentSize, newFontSize)
            self.setStyleSheet(newStyleSheet)
        else:
            self.setStyleSheet(styleSheet + newFontSize)
        self.showStatusBarMessage("Изменен размер шрифта")

    def updateBlinkPeriod(self, newPeriod):
        self.showStatusBarMessage(f"Период мигания кружка изменен на {newPeriod}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
