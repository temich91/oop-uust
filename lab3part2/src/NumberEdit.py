from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QSlider, QSpinBox, QLabel
from PyQt5.QtCore import Qt, pyqtSignal

class NumberEdit(QWidget):
    changed = pyqtSignal(int) # сигнал изменения значения в форме

    def __init__(self, parent, text):
        super().__init__(parent=parent)
        self.isUpdating = False # флаг, обновляются ли значения в формах после пользовательского ввода
        widgetLayout = QVBoxLayout()
        self.lastValidValue = 0
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

            if not value.isdigit():
                self.isUpdating = True
                self.lineEdit.setText(str(self.lastValidValue))
                self.isUpdating = False
                return

            value = int(value)

        self.changed.emit(value)
        if value != self.lastValidValue:
            self.isUpdating = True
            self.lineEdit.setText(str(self.lastValidValue))
            self.spinBox.setValue(self.lastValidValue)
            self.slider.setValue(self.lastValidValue)
            self.isUpdating = False

    def onSliderChanged(self, newValue):
        if self.isUpdating:
            return

        self.changed.emit(newValue)
        if newValue != self.lastValidValue:
            self.isUpdating = True
            self.slider.setValue(self.lastValidValue)
            self.isUpdating = False

    def updateValue(self, newValue):
        self.isUpdating = True
        self.lastValidValue = newValue
        self.lineEdit.setText(str(newValue))
        self.slider.setValue(newValue)
        self.spinBox.setValue(newValue)
        self.update()
        self.isUpdating = False
