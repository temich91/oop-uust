from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QSlider, QSpinBox, QLabel
from PyQt5.QtCore import Qt, pyqtSignal

class NumberEdit(QWidget):
    changed = pyqtSignal(int) # сигнал изменения значения в форме

    def __init__(self, parent, text):
        super().__init__(parent=parent)
        self.isUpdating = False # флаг, обновляются ли значения в формах после пользовательского ввода
        widgetLayout = QVBoxLayout()
        self.label = QLabel(text)
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.onValueChanged)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.onValueChanged)
        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.onValueChanged)

        widgetLayout.addWidget(self.label)
        widgetLayout.addWidget(self.lineEdit)
        widgetLayout.addWidget(self.slider)
        widgetLayout.addWidget(self.spinBox)
        self.setLayout(widgetLayout)

    def onValueChanged(self, newValue):
        try:
            if self.isUpdating:
                return
            self.changed.emit(int(newValue))
        except ValueError:
            return

    def updateValue(self, newValue):
        self.isUpdating = True
        self.lineEdit.setText(str(newValue))
        self.slider.setValue(newValue)
        self.spinBox.setValue(newValue)
        self.update()
        self.isUpdating = False
