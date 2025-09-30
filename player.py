from beans import Bean

class Player():
    hand: list[Bean] = []
    coins: int = 0
    fields: list[list[Bean]] = [[], []]
