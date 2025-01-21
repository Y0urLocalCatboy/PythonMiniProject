class Entity:
    """
    Represents an entity in the simulation.

    Attributes:
        name (str): The name of the entity.
        position (pygame.Vector2): The position of the entity.
    """
    def __init__(self, name, position):
        self.name = name
        self. position = position