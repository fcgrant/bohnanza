from beans import Bean

class Player():
    hand: list[Bean]
    coins: int
    fields: list[list[Bean]]

    def __init__(self) -> None:
        self.hand = []
        self.coins = 0
        self.fields = [[], []]