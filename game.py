from beans import BEANS, Bean
from deck import Deck
from player import Player

class Game:
    reshuffle_count: int = 0
    beans_per_player: int = 5
    players: list[Player] = []
    deck: Deck = Deck()
    discard_pile: list[Bean] = []
    table: list[int] = []

    def setup(self) -> None:
        number_of_players = input("Enter number of players (2-7): ")
        while not number_of_players.isdigit() or not (2 <= int(number_of_players) <= 7):
            number_of_players = input("Invalid input. Please enter a number between 2 and 7: ")
        number_of_players = int(number_of_players)

        self.players = [Player() for _ in range(number_of_players)]
        self.deck.beans = {index: bean.number_in_deck for index, bean in enumerate(BEANS)}
        for _ in range(self.beans_per_player):
            for player in range(number_of_players):
                self.players[player].hand.append(self.deck.draw_bean())


    def planting_before_trade_phase(self, player: Player) -> None:
        print("Pre-trade planting phase...")
        if len(player.hand) == 0:
            print("No beans in hand to plant. Skipping to trading phase.")
            return

        player.plant(player.hand.pop(0))

        if len(player.hand) == 0:
            print("No beans in hand to plant. Skipping to trading phase.")
            return

        player.print_beans(player.hand)
        choice = input("Plant your next bean? (y/n)").lower()
        player.plant(player.hand.pop(0)) if choice == 'y' else None
        print("Moving to trading phase...")
    
    def trade_phase(self, player: Player) -> None:
        print("Trading phase...")
        if self.table:
            raise ValueError("Table must be empty at the start of the trading phase")
        self.table = [self.deck.draw_bean(), self.deck.draw_bean()]

        print("Table shows:\n")
        player.print_beans(self.table)
        for bean_index in self.table:
            if not player.get_available_fields(bean_index):
                continue
            print(f"There are available fields for your {BEANS[bean_index]}.")
            choice = input(f"Would you like to plant your {BEANS[bean_index]}?").lower()
            player.plant(bean_index) if choice == "y" else None

        print("Trading is now open...")
        return

    def planting_after_trade_phase(self, player: Player) -> None:
        print("Post-trade planting phase...")
        if not self.table:
            print("Table is empty, no beans need planting.")
            return

        for bean_index in self.table:
            if not player.get_available_fields(bean_index):
                continue
            print(f"There are available fields for your {BEANS[bean_index]}.")
            choice = input(f"Would you like to plant your {BEANS[bean_index]}?").lower()
            player.plant(bean_index) if choice == "y" else None

        for bean_index in self.table:
            player.plant(bean_index)

        self.table = []
        print("Table is empty, moving to draw phase...")
        return
    
    def draw_phase(self, player: Player) -> None:
        print("Draw phase...")
        for _ in range(3):
            bean_index = self.deck.draw_bean()
            player.hand.append(bean_index)
            print(f"Drew a {BEANS[bean_index]}.")
            if len(self.deck.beans) == 0:
                print("Deck is empty. Reshuffling discard pile into deck...")
                raise EmptyDeck()
    
    def reshuffle_deck(self) -> None:
        if not self.discard_pile:
            print("No cards in discard pile to reshuffle.")
            return
        print("Reshuffling discard pile into deck...")
        for bean in self.discard_pile:
            bean_id = BEANS.index(bean)
            if bean_id in self.deck.beans:
                self.deck.beans[bean_id] += 1
            else:
                self.deck.beans[bean_id] = 1
        self.discard_pile.clear()
        self.reshuffle_count += 1
        print("Reshuffle complete.")


class EmptyDeck(Exception):
    pass