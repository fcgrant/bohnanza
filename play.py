from constants import MAX_RESHUFFLES
from game import Game, EmptyDeck


if __name__ == "__main__":
    game = Game()
    print("Starting game...")
    game.setup()

    for index, player in enumerate(game.players):
        player.order = index + 1
        player.name = input(f"Enter name for player {player.order}: ")

    for player in game.players:
        try:
            print(f"{player.name}, your turn!")
            player.print_hand()
            game.planting_before_trade_phase(player)
            game.trade_phase(player)
            game.planting_after_trade_phase(player)
            game.draw_phase(player)
        except EmptyDeck:    
            if game.reshuffle_count == MAX_RESHUFFLES:
                print("Maximum reshuffles reached. Ending game.")
                break
            print("Deck empty.")
            
        input("Press Enter to end your turn...")

    print("Game over! Final scores: ")
