from beans import BEANS
from field import Field

class Player():
    name: str
    order: int
    hand: list[int]
    coins: int
    fields: list[Field]

    def __init__(self) -> None:
        self.name = ""
        self.order = 0
        self.hand = []
        self.coins = 0
        self.fields = []


    def plant(self, field_index: int, bean_index: int) -> None:
        if field_index >= len(self.fields):
            raise IndexError("Invalid field index.")

        field = self.fields[field_index]
        bean = BEANS[bean_index]

        if field.bean_id is not None and field.bean_id != bean_index:
            raise ValueError("Cannot plant different types of beans in the same field.")

        field.plant(1)
        print(f"Planted {bean.name} in field {field_index + 1}. Now has {field.number_of_beans} beans.")
        

    def print_hand(self) -> None:
        print("Your hand: ")
        for index, bean in enumerate(self.hand):
            print(f"| {index + 1}: {BEANS[bean].name} |", end=" ")
        print("\n")
