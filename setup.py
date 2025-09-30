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