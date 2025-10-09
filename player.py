from beans import Bean

class Player():
    name: str
    order: int
    hand: list[Bean]
    coins: int
    field_limit: int
    fields: dict[str, list[Bean]]

    def __init__(self) -> None:
        self.name = ""
        self.order = 0
        self.hand = []
        self.coins = 0
        self.field_limit = 2
        self.fields = {}


    def plant(self, bean: Bean):
        if len(self.fields) >= self.field_limit and bean.name not in self.fields:
            print(f"Can't plant {bean.name}. No available fields.")

        field: list[Bean] = self.fields.get(bean.name, [])
        field.append(bean)
        self.fields[bean.name] = field
        self.hand.remove(bean)
        self.print_fields()


    def print_fields(self) -> None:
        for bean_name, field in self.fields.items():
            print(f"{bean_name} field: {len(field)} beans")


    def print_hand(self) -> None:
        print("Your hand: ", end="")
        for index, bean in enumerate(self.hand):
            print(f"| {index + 1}: {bean.name} |", end=" ")
        print("\n")
