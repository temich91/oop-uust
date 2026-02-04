import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QWidget, QTabWidget, QWIDGETSIZE_MAX, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QTimer
from MainTab import MainTab
from SpamTab import SpamTab

STATUSBAR_MESSAGE_TIMEOUT = 1000 # мс

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # служебные поля
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.sendSignal)

        # компоненты окна приложения
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Status Bar")
        self.statusBar().setStyleSheet("border: 3px solid black")
        self.setWindowTitle("NU PRIVET")

        self.mainWidget = QWidget(self)
        mainWidgetLayout = QHBoxLayout()
        mainWidgetLayout.setContentsMargins(0,0,0,0)
        mainWidgetLayout.setSpacing(0)
        self.mainWidget.setLayout(mainWidgetLayout)
        self.setCentralWidget(self.mainWidget)

        # размеры окна
        self.setMinimumSize(600, 400)
        self.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)
        # self.setStyleSheet("background-color: orange")

        # вкладки
        self.mainTab = MainTab(self)
        self.spamTab = SpamTab(self)
        self.spamTab.setStyleSheet("background-color: #FFBF7B")

        self.mainTabDialog = QTabWidget(self.mainWidget)
        self.mainTabDialog.addTab(self.mainTab, "knopochki")
        self.mainTabDialog.addTab(self.spamTab, "spam")

        self.mainTab.titleEditRequested.connect(self.setWindowTitle)
        self.mainTab.statusBarMessageSent.connect(self.showStatusBarMessage)

        self.mainWidget.layout().addWidget(self.mainTabDialog)

    def sendSignal(self):
        self.mainTab.updateRunningTime()

    def showStatusBarMessage(self, message):
        self.statusBar().showMessage(message, msecs=STATUSBAR_MESSAGE_TIMEOUT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
