class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Sword(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Coins(Item):
    def __init__(self, name, description):
        super().__init__(name, description)