import json
import pathlib

HOME_DIR = pathlib.Path(".").resolve() # абсолютный путь к папке lab3part2/
CONFIG_PATH = HOME_DIR / "src" / "modelConfig.json"

class Model:
    def __init__(self):
        with open(CONFIG_PATH, "r") as file:
            config = json.load(file)
        self.a = config["a"]
        self.b = config["b"]
        self.c = config["c"]

        self.observers = []

    def addObserver(self, newObserver):
        if newObserver not in self.observers:
            self.observers.append(newObserver)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def _checkValue(self, value: int):
        """
        Проверка общих ограничений на вводимые значения переменных.
        """
        return 0 <= value <= 100

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def setA(self, newValue):
        if not self._checkValue(newValue):
            return

        self.a = newValue
        if newValue > self.b:
            self.setB(newValue)

    def setB(self, newValue):
        if not self._checkValue(newValue):
            return

        self.b = newValue
        if newValue < self.a:
            self.setA(newValue)
        if newValue > self.c:
            self.setC(newValue)

    def setC(self, newValue):
        if not self._checkValue(newValue):
            return

        self.c = newValue
        if newValue < self.b:
            self.setB(newValue)

    def saveValues(self):
        """
        Запись текущих значений переменных в json.
        """

        data = {"a": self.a,
                "b": self.b,
                "c": self.c}
        with open(CONFIG_PATH, "w") as file:
            json.dump(data, file, indent=2)
