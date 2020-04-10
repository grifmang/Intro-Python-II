# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
    
    def show_items(self):
        [print(x.name) for x in self.items]