import random

from beans import BEANS, Bean
from deck import Deck
from player import Player

class Game:
    beans_per_player: int = 5
    players: list[Player] = []
    deck: Deck = Deck()
    discard_pile: list[Bean] = []
    trade_area: list[Bean] = []        

    def setup(self) -> None:
        print("Setting up the game...")

        print("Initializing players...")
        number_of_players = input("Enter number of players (2-7): ")
        while not number_of_players.isdigit() or not (2 <= int(number_of_players) <= 7):
            number_of_players = input("Invalid input. Please enter a number between 2 and 7: ")
        number_of_players = int(number_of_players)

        self.players = [Player() for _ in range(number_of_players)]
        print("Players initialized.")

        print("Initializing deck...")
        self.deck.beans = {index: bean.number_in_deck for index, bean in enumerate(BEANS)}
        print("Deck initialized.")

        print("Dealing hands...")
        for _ in range(self.beans_per_player):
            for player in range(number_of_players):
                self.players[player].hand.append(self.deck.draw_bean())

        print("Hands dealt.")
        print("Game setup complete.")

