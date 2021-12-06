class Banker:
    def __init__(self) -> None:
        self.shelved = 0
        self.balance = 0

    def shelf(self, value) -> None:
        self.shelved += value

    def bank(self) -> int:
        added_balance = self.shelved
        self.balance += added_balance
        self.clear_shelf()
        return added_balance

    def clear_shelf(self) -> None:
        self.shelved = 0