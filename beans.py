class Bean():
    name: str
    number_in_deck: int
    number_needed_to_harvest: dict[int, int | None]


class CoffeeBean(Bean):
    name = "Coffee Bean"
    number_in_deck = 24
    number_needed_to_harvest = {1: 4, 2: 7, 3: 10, 4: 12}


class WaxBean(Bean):
    name = "Wax Bean"
    number_in_deck = 22
    number_needed_to_harvest = {1: 4, 2: 7, 3: 9, 4: 11}


class BlueBean(Bean):
    name = "Blue Bean"
    number_in_deck = 20
    number_needed_to_harvest = {1: 4, 2: 6, 3: 8, 4: 10}


class ChiliBean(Bean):
    name = "Chili Bean"
    number_in_deck = 18
    number_needed_to_harvest = {1: 3, 2: 6, 3: 8, 4: 9}


class StinkBean(Bean):
    name = "Stink Bean"
    number_in_deck = 16
    number_needed_to_harvest = {1: 3, 2: 5, 3: 7, 4: 8}


class GreenBean(Bean):
    name = "Green Bean"
    number_in_deck = 14
    number_needed_to_harvest = {1: 3, 2: 5, 3: 6, 4: 7}


class SoyBean(Bean):
    name = "Soy Bean"
    number_in_deck = 12
    number_needed_to_harvest = {1: 2, 2: 4, 3: 6, 4: 7}


class BlackEyedBean(Bean):
    name = "Black-Eyed Bean"
    number_in_deck = 10
    number_needed_to_harvest = {1: 2, 2: 4, 3: 5, 4: 6}


class RedBean(Bean):
    name = "Red Bean"
    number_in_deck = 8
    number_needed_to_harvest = {1: 2, 2: 3, 3: 4, 4: 5}


class GardenBean(Bean):
    name = "Garden Bean"
    number_in_deck = 6
    number_needed_to_harvest = {1: None, 2: 2, 3: 3, 4: None}


class CocoaBean(Bean):
    name = "Cocoa Bean"
    number_in_deck = 4
    number_needed_to_harvest = {1: None, 2: 2, 3: 3, 4: 4}


class FieldBean(Bean):
    name = "Field Bean"
    number_in_deck = 3
    number_needed_to_harvest = {1: None, 2: 2, 3: 3, 4: None}