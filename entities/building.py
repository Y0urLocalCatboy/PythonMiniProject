from entities.entity import Entity


class Building(Entity):
    def __init__(self, name, position, size, bloxes):
        super().__init__(name, position)
        self.size = size
        self.bloxes = bloxes

