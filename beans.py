class Bean():
    name: str
    number_in_deck: int
    # Maps a number of beans to the coins received when harvested
    number_needed_to_harvest: dict[int, int]

    def __init__(self, name: str, number_in_deck: int, number_needed_to_harvest: dict[int, int]) -> None:
        self.name = name
        self.number_in_deck = number_in_deck
        self.number_needed_to_harvest = number_needed_to_harvest

BEANS = [
    Bean("Coffee Bean", 24, {4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2, 10: 3, 11: 3, 12: 4}),
    Bean("Wax Bean", 22, {4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 3, 10: 3, 11: 4}),
    Bean("Blue Bean", 20, {4: 1, 5: 1, 6: 2, 7: 2, 8: 3, 9: 3, 10: 4}),
    Bean("Chili Bean", 18, {3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 3, 9: 4}),
    Bean("Stink Bean", 16, {3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4}),
    Bean("Green Bean", 14, {3: 1, 4: 1, 5: 2, 6: 3, 7: 4}),
    Bean("Soy Bean", 12, {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4}),
    Bean("Black-Eyed Bean", 10, {2: 1, 3:1, 4: 2, 5: 3, 6: 4}),
    Bean("Red Bean", 8, {2: 1, 3: 2, 4: 3, 5: 4}),
    Bean("Garden Bean", 6, {2: 2, 3: 3}),
    Bean("Cocoa Bean", 4, {2: 2, 3: 3, 4: 4}),
    Bean("Field Bean", 3, {2: 2, 3: 3})
]

COFFEE_BEAN = 0
WAX_BEAN = 1
BLUE_BEAN = 2
CHILI_BEAN = 3
STINK_BEAN = 4
GREEN_BEAN = 5
SOY_BEAN = 6
BLACK_EYED_BEAN = 7
RED_BEAN = 8
GARDEN_BEAN = 9
COCOA_BEAN = 10
FIELD_BEAN = 11
