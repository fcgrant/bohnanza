from beans import Bean
from player import Player

class Game:
    beans_per_player: int = 5
    players: list[Player] = []
    deck: list[Bean] = []
    discard_pile: list[Bean] = []
    trade_area: list[Bean] = []
