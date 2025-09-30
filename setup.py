import random

from game import Game
from player import Player
from beans import (
    CoffeeBean,
    WaxBean,
    BlueBean,
    ChiliBean,
    StinkBean,
    GreenBean,
    SoyBean,
    BlackEyedBean,
    RedBean,
    GardenBean,
    CocoaBean,
    FieldBean
)

game = Game()

def setup_game() -> None:
    print("Setting up the game...")

    print("Initializing deck...")
    game.deck.extend([CoffeeBean() for bean in range(0, CoffeeBean.number_in_deck)])
    game.deck.extend([WaxBean() for bean in range(0, WaxBean.number_in_deck)])
    game.deck.extend([BlueBean() for bean in range(0, BlueBean.number_in_deck)])
    game.deck.extend([ChiliBean() for bean in range(0, ChiliBean.number_in_deck)])
    game.deck.extend([StinkBean() for bean in range(0, StinkBean.number_in_deck)])
    game.deck.extend([GreenBean() for bean in range(0, GreenBean.number_in_deck)])
    game.deck.extend([SoyBean() for bean in range(0, SoyBean.number_in_deck)])
    game.deck.extend([BlackEyedBean() for bean in range(0, BlackEyedBean.number_in_deck)])
    game.deck.extend([RedBean() for bean in range(0, RedBean.number_in_deck)])
    game.deck.extend([GardenBean() for bean in range(0, GardenBean.number_in_deck)])
    game.deck.extend([CocoaBean() for bean in range(0, CocoaBean.number_in_deck)])
    game.deck.extend([FieldBean() for bean in range(0, FieldBean.number_in_deck)])
    print("Deck initialized.")

    print("Shuffling deck...")
    # TODO: Implement shuffling for deck
    print("Deck shuffled.")

    print("Initializing players...")
    number_of_players = input("Enter number of players (2-7): ")
    while not number_of_players.isdigit() or not (2 <= int(number_of_players) <= 7):
        number_of_players = input("Invalid input. Please enter a number between 2 and 7: ")
    number_of_players = int(number_of_players)

    game.players = [Player() for _ in range(number_of_players)]
    print("Players initialized.")

    print("Dealing hands...")
    player_hands = {index: [] for index in range(len(game.players))}
    for _ in range(game.beans_per_player):
        for player in range(number_of_players):
            game.players[player].hand.append(game.deck.pop(0))

    print("Hands dealt.")
    print("Game setup complete.")


setup_game()