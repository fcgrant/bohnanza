import random

class Deck():
    # A dictionary of the bean ID to the number of those beans in the deck
    beans: dict[int, int] = {}

    def draw_bean(self) -> int:
        bean: int = random.choice(list(self.beans.keys())) 
        bean_count = self.beans.get(bean)
        if bean_count == 1:
            del self.beans[bean]
        return bean
