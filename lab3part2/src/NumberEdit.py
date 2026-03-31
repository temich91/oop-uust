from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QSlider, QSpinBox, QLabel
from PyQt5.QtCore import Qt, pyqtSignal

class NumberEdit(QWidget):
    changed = pyqtSignal(str) # сигнал изменения значения в форме

    def __init__(self, parent, text):
        super().__init__(parent=parent)
        self.isUpdating = False # флаг, обновляются ли значения в формах после пользовательского ввода
        widgetLayout = QVBoxLayout()
        self.label = QLabel(text)
        self.label.setStyleSheet("font-size: 28px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.lineEdit = QLineEdit()
        self.lineEdit.editingFinished.connect(self.onEditingFinished)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.onSliderChanged)

        self.spinBox = QSpinBox()
        self.spinBox.editingFinished.connect(self.onEditingFinished)

        widgetLayout.addWidget(self.label)
        widgetLayout.addWidget(self.lineEdit)
        widgetLayout.addWidget(self.slider)
        widgetLayout.addWidget(self.spinBox)
        self.setLayout(widgetLayout)

    def onEditingFinished(self):
        if self.isUpdating:
            return

        if self.sender() == self.spinBox:
            value = self.spinBox.value()
        else:
            value = self.lineEdit.text()
        self.changed.emit(str(value))

    def onSliderChanged(self, newValue):
        if self.isUpdating:
            return

        self.changed.emit(str(newValue))

    def updateValue(self, newValue):
        self.isUpdating = True
        self.lineEdit.setText(str(newValue))
        self.slider.setValue(newValue)
        self.spinBox.setValue(newValue)
        self.update()
        self.isUpdating = False
