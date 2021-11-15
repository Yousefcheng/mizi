class turn_str:
    def __init__(self) -> None:
        pass
    def getString(self):
        self.string=input()
    def printSting(self):
        print(self.string.upper())

A=turn_str()

A.getString()
A.printSting()