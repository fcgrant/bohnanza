import random

from beans import BEANS, Bean

class Deck():
    beans: dict[int, int] = {}

    def draw_bean(self) -> int:
        bean: int = random.choice(list(self.beans.keys())) 
        bean_count = self.beans.get(bean)
        if bean_count == 1:
            del self.beans[bean]
        return bean
