import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QWidget, QTabWidget, QWIDGETSIZE_MAX, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QTimer
from MainTab import MainTab
from SpamTab import SpamTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # служебные поля
        self.timer = QTimer(self)

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
        self.setStyleSheet("background-color: orange")

        # вкладки
        self.mainTab = MainTab()
        self.spamTab = SpamTab()
        self.spamTab.setStyleSheet("background-color: green")

        self.mainTabDialog = QTabWidget(self.mainWidget)
        self.mainTabDialog.addTab(self.mainTab, "knopochki")
        self.mainTabDialog.addTab(self.spamTab, "spam")

        self.mainWidget.layout().addWidget(self.mainTabDialog)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
