from enum import Enum

class Status(Enum):
    """
    Enum representing the status of an entity.

    Attributes:
        HEALTHY: Represents a healthy status (green).
        SICK: Represents a sick status (red).
        RECOVERED: Represents a recovered status (blue).
    """
    HEALTHY = 1  # green
    SICK = 2     # red
    RECOVERED = 3  # blue

    def get_color(self):
        """
        Returns the color associated with the status.

        Returns:
            tuple: A tuple representing the RGB color.
        """
        if self == Status.HEALTHY:
            return (0, 255, 0)
        elif self == Status.SICK:
            return (255, 0, 0)
        elif self == Status.RECOVERED:
            return (0, 0, 255)



