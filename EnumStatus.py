from enum import Enum


class Status(Enum):
    HEALTHY = 1 # green
    SICK = 2 # red
    RECOVERED = 3 # blue
    def get_color(self):
        if self == Status.HEALTHY:
            return (0, 255, 0)
        elif self == Status.SICK:
            return (255, 0, 0)
        elif self == Status.RECOVERED:
            return (0, 0, 255)

