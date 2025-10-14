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
    
    def planting_before_trade_phase(self, player: Player) -> None:
        print("Pre-trade planting phase...")
        if len(player.hand) == 0:
            print("No beans in hand to plant. Skipping to trading phase.")
            return

        player.plant()

        if len(player.hand) == 0:
            print("No beans in hand to plant. Skipping to trading phase.")
            return

        print("Plant your next bean? (y/n)")
        player.print_hand()
        choice = input().lower()
        player.plant() if choice == 'y' else None
        print("Moving to trading phase...")
    
    def trading_phase(self, player: Player) -> None:
        print("Trading phase...")
        # Trading logic to be implemented
        pass

    def planting_after_trade_phase(self, player: Player) -> None:
        print("Post-trade planting phase...")
        pass
    
    def draw_phase(self, player: Player) -> None:
        pass
