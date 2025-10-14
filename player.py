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
        self.fields = [Field(None, 0), Field(None, 0)]

    def get_available_fields(self, bean_index: int) -> list[int]:
        """Gets the index/indices of available fields you can plant the bean in."""
        available_fields: list[int] = []
        for field in self.fields:
            if field.bean_id == bean_index or field.bean_id is None:
                available_fields.append(self.fields.index(field))
        return available_fields
    
    def plant(self):
        if not self.hand:
            print("No beans in hand to plant.")
            return

        bean_index = self.hand.pop(0)
        available_fields = self.get_available_fields(bean_index)
        number_of_available_fields = len(available_fields)
        number_of_fields = len(self.fields)

        if len(available_fields) == 0:
            print("No avalailable fields to plant the bean. You must harvest a field first.")
            field_index = input(f"Choose a field to harvest (1-{number_of_fields}): ")
            while not field_index.isdigit() or not (1 <= int(field_index) <= len(self.fields)):
                field_index = input(f"Invalid input. Choose a field to harvest (1-{len(self.fields)}): ")
            field_index = int(field_index) - 1
            self.coins += self.fields[field_index].harvest()
        elif number_of_available_fields == 1:
            field_index = available_fields[0]
            print(f"Only one available field to plant the bean. Planting in field {field_index + 1}.")
        else:
            print(f"You have {len(available_fields)} available field(s) to plant the bean.")
            field_index = input(f"Choose a field to plant the bean (1-{len(self.fields)}): ")
            while not field_index.isdigit() or not (1 <= int(field_index) <= len(self.fields)) or (int(field_index) - 1) not in available_fields:
                field_index = input(f"Invalid input. Choose a field to plant the bean (1-{len(self.fields)}): ")
            field_index = int(field_index) - 1

        field = self.fields[field_index]

        if field.bean_id is not None and field.bean_id != bean_index:
            print("Cannot plant different types of beans in the same field.")
            return

        field.plant(bean_index)
        self.fields[field_index] = field

        print(f"{field.get_bean_name()} planted in field {field_index + 1}.")
        self.print_fields()


    def print_hand(self) -> None:
        print("Your hand: ")
        for index, bean in enumerate(self.hand):
            print(f"| {index + 1}: {BEANS[bean].name} |", end=" ")
        print("\n")


    def print_fields(self) -> None:
        print("Your fields: ")
        for index, field in enumerate(self.fields):
            if field.bean_id is not None:
                print(f"| Field {index + 1}: {field.number_of_beans} x {field.get_bean_name()} |", end=" ")
            else:
                print(f"| Field {index + 1}: Empty |", end=" ")
        print("\n")
