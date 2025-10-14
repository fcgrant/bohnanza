from beans import BEANS

class Field():
    bean_id: int | None
    number_of_beans: int

    def __init__(self, bean_id: int, number_of_beans: int) -> None:
        self.bean_id = bean_id
        self.number_of_beans = number_of_beans
    
    def get_bean_name(self) -> str:
        if self.bean_id is None:
            return "Empty"
        return BEANS[self.bean_id].name

    def plant(self, bean_index: int) -> None:
        if self.bean_id is None:
            self.bean_id = bean_index

        if self.bean_id != bean_index:
            print("Cannot plant different types of beans in the same field.")
            return

        self.number_of_beans += 1

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

        print(f"Harvested {self.number_of_beans} {bean.name}(s). Got {coins} coins.")
        self.number_of_beans = 0
        self.bean_id = None
        return coins
