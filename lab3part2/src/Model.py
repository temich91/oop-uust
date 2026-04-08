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

        self.updates_count = 0

    def addObserver(self, newObserver):
        if newObserver not in self.observers:
            self.observers.append(newObserver)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def _checkValue(self, value):
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

    def setValues(self, a=None, b=None, c=None):
        isChanged = False

        if a is not None and a != self.a:
            self.a = a
            isChanged = True

        if b is not None and b != self.b:
            self.b = b
            isChanged = True

        if c is not None and c != self.c:
            self.c = c
            isChanged = True

        return isChanged

    def setA(self, value):
        if not self._checkValue(value):
            return

        newA = value
        newB = max(newA, self.b)
        newC = max(newA, self.c)

        if self.setValues(newA, newB, newC):
            self.notify()

    def setB(self, value):
        if not self._checkValue(value):
            return

        newB = value
        newB = max(newB, self.a)
        newB = min(newB, self.c)

        if self.setValues(b=newB):
            self.notify()

    def setC(self, value):
        if not self._checkValue(value):
            return

        newC = value
        newA = min(self.a, newC)
        newB = min(self.b, newC)

        if self.setValues(newA, newB, newC):
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
        self.updates_count += 1
        print(f"обновление #{self.updates_count}")
        for observer in self.observers:
            observer(self.getA(), self.getB(), self.getC())
