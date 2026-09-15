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
        return [
            index for index, field in enumerate(self.fields)
            if field.bean_id is None or field.bean_id == bean_index
        ]

    def plant(self, bean_index: int):
        self.print_fields()
        available_fields = self.get_available_fields(bean_index)

        if len(available_fields) == 0:
            print(f"No avalailable fields to plant your {BEANS[bean_index]}. You must harvest a field first.")
            field_index = input(f"Choose a field to harvest (1-{len(self.fields)}): ")
            while not field_index.isdigit() or not (1 <= int(field_index) <= len(self.fields)):
                field_index = input(f"Invalid input. Choose a field to harvest (1-{len(self.fields)}): ")
            field_index = int(field_index) - 1
            self.coins += self.fields[field_index].harvest()
        elif len(available_fields) == 1:
            field_index = available_fields[0]
            print(f"Only one available field to plant your {BEANS[bean_index]}. Planting in field {field_index + 1}.")
        else:
            print(f"You have {len(available_fields)} available fields to plant your {BEANS[bean_index]}.")
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


    def print_beans(self, beans: list[int]) -> None:
        for index, bean in enumerate(beans):
            print(f"| {index + 1}: {BEANS[bean]} |", end=" ")
        print("\n")


    def print_fields(self) -> None:
        print("Your fields: ")
        for index, field in enumerate(self.fields):
            if field.bean_id is not None:
                print(f"| Field {index + 1}: {field.number_of_beans} x {field.get_bean_name()} |", end=" ")
            else:
                print(f"| Field {index + 1}: Empty |", end=" ")
        print("\n")
