from beans import BEANS

class Field():
    bean_id: int | None
    number_of_beans: int

    def __init__(self, bean_id: int, number_of_beans: int) -> None:
        self.bean_id = bean_id
        self.number_of_beans = number_of_beans

    def plant(self, number_of_beans: int) -> None:
        self.number_of_beans += number_of_beans

    def harvest(self) -> int:
        if self.bean_id is None:
            print("No beans to harvest.")
            return 0

        bean = BEANS[self.bean_id]
        coin_limits = list(bean.number_needed_to_harvest.keys())
        if self.number_of_beans > max(coin_limits):
            coins = bean.number_needed_to_harvest[max(coin_limits)]
        elif self.number_of_beans < min(coin_limits):
            coins = 0
        else:
            coins = bean.number_needed_to_harvest.get(self.number_of_beans)

        print(f"Harvested {self.number_of_beans}. Got {coins} coins.")
        self.number_of_beans = 0
        return coins
