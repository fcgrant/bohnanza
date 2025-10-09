from setup import setup_game, game


if __name__ == "__main__":
    setup_game()
    print("Starting game...")

    for index, player in enumerate(game.players):
        player.order = index + 1
        player.name = input(f"Enter name for player {player.order}: ")

    for player in game.players:
        print(f"{player.name}, your turn!")
        player.print_hand()

        print("Planting phase...")
        player.plant(player.hand[0])

        print("Plant your next bean? (y/n)")
        player.print_hand()
        choice = input().lower()
        player.plant(player.hand[0]) if choice == 'y' else None

        print("Flipping cards...")
        input("Press Enter to end your turn...")
