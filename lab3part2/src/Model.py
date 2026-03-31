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

    def _checkValue(self, value: str):
        """
        Проверка общих ограничений на вводимые значения переменных.
        """
        if not value.isdigit():
            return False

        return 0 <= int(value) <= 100

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def setA(self, value):
        if (not isinstance(value, int)) and (not self._checkValue(value)):
            self.notify()
            return

        newValue = int(value)
        self.a = newValue
        if newValue > self.b:
            self.setB(newValue)
        if newValue > self.c:
            self.setC(newValue)

        self.notify()

    def setB(self, value):
        if (not isinstance(value, int)) and (not self._checkValue(value)):
            self.notify()
            return

        newValue = int(value)
        self.b = newValue
        if newValue < self.a:
            self.b = self.a
        if newValue > self.c:
            self.b = self.c

        self.notify()

    def setC(self, value):
        if (not isinstance(value, int)) and (not self._checkValue(value)):
            self.notify()
            return

        newValue = int(value)
        self.c = newValue
        if newValue < self.a:
            self.setA(newValue)
        if newValue < self.b:
            self.setB(newValue)

        self.notify()

    def saveValues(self):
        """
        Запись текущих значений переменных в json.
        """

        data = {"a": self.a,
                "b": self.b,
                "c": self.c}
        with open(CONFIG_PATH, "w") as file:
            json.dump(data, file, indent=2)

    def notify(self):
        """
        Вызов у наблюдателей обновления значений A, B, C.
        """

        for observer in self.observers:
            observer(self.getA(), self.getB(), self.getC())
