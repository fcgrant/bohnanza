from beans import Bean
from player import Player

class Game:
    players: list[Player] = []
    deck: list[Bean] = []
    discard_pile: list[Bean] = []
    trade_area: list[Bean] = []