from game import Game


if __name__ == "__main__":
    game = Game()
    print("Starting game...")
    game.setup()

    for index, player in enumerate(game.players):
        player.order = index + 1
        player.name = input(f"Enter name for player {player.order}: ")

    for player in game.players:
        print(f"{player.name}, your turn!")
        player.print_hand()

        game.planting_before_trade_phase(player)

        game.trading_phase(player)
        
        game.planting_after_trade_phase(player)

        game.draw_phase(player)

        input("Press Enter to end your turn...")
