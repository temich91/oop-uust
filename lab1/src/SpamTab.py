from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QGridLayout,
                             QLabel, QPushButton, QLineEdit)
from PyQt5.QtWidgets import QWidget
import src.utils.constants as c

class SpamTab(QWidget):
    """
    Вкладка для спама виджетами.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        tabLayout = QVBoxLayout(self)
        self.gridWidth = c.BTNS_GRID_WIDTH
        self.gridHeight = c.BTNS_GRID_HEIGHT
        self.curBtnX = 0
        self.curBtnY = 0
        self.btnsCnt = 0

        # место для появления кнопок
        self.spamLayout = QGridLayout()

        # настройки кнопок
        addBtnsBtn = QPushButton("Добавить кнопку")
        addBtnsBtn.clicked.connect(self.addBtn)

        widthLabel = QLabel("Макс. столбцов:")
        self.widthEdit = QLineEdit()
        gridWidthLayout = QHBoxLayout()
        gridWidthLayout.addWidget(widthLabel)
        gridWidthLayout.addWidget(self.widthEdit)

        heightLabel = QLabel("Макс. строк:")
        self.heightEdit = QLineEdit()
        gridHeightLayout = QHBoxLayout()
        gridHeightLayout.addWidget(heightLabel)
        gridHeightLayout.addWidget(self.heightEdit)

        gridUpdateBtn = QPushButton("Обновить сетку")
        gridUpdateBtn.clicked.connect(self.updateGrid)

        self.btnNumberLabel = QLabel()  # номер нажатой кнопки

        paramsLayout = QHBoxLayout()
        paramsLayout.addWidget(addBtnsBtn)
        paramsLayout.addLayout(gridHeightLayout)
        paramsLayout.addLayout(gridWidthLayout)
        paramsLayout.addWidget(gridUpdateBtn)

        tabLayout.addLayout(self.spamLayout)
        tabLayout.addLayout(paramsLayout)
        tabLayout.addWidget(self.btnNumberLabel)

    def addBtn(self):
        if self.btnsCnt > self.gridWidth * self.gridHeight - 1:
            # вызвать окно ошибки
            return
        if self.btnsCnt % self.gridWidth == 0:
            self.curBtnX = 0
            self.curBtnY += 1
        newBtn = QPushButton(str(self.btnsCnt + 1))
        newBtn.clicked.connect(lambda _, btn=newBtn: self.sendNumber(newBtn))
        self.curBtnX += 1
        self.btnsCnt += 1
        self.spamLayout.addWidget(newBtn, self.curBtnY, self.curBtnX)

    def sendNumber(self, btn):
        self.btnNumberLabel.setText(f"Последняя нажатая кнопка: {btn.text()}")

    def updateGrid(self):
        newWidth = self.widthEdit.text()
        newHeight = self.heightEdit.text()
        try:
            self.gridWidth = int(newWidth)
            self.gridHeight = int(newHeight)

            # очистка сетки кнопок
            for i in range(self.spamLayout.count() - 1, -1, -1):
                item = self.spamLayout.takeAt(i)
                if item:
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            cntToAdd = min(self.btnsCnt, self.gridWidth * self.gridHeight)
            self.curBtnX = 0
            self.curBtnY = 0
            self.btnsCnt = 0
            for i in range(cntToAdd):
                self.addBtn()

        except ValueError:
            return
