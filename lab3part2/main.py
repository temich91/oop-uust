import sys
from PyQt5.QtWidgets import QApplication
from lab3part2.src.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()