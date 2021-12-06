class Banker:
    def __init__(self) -> None:
        self. shelved = 0
        self.balance = 0

    def shelf(self, value):
        self.shelved += value