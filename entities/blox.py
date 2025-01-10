from entities.status import Status

class Blox:

    def __init__(self, name, status, position):
        self.name = name
        self.status = status
        self.position = position

    def move(self, new_position):
        self.position = new_position

    def change_status(self):
        if self.status == Status.HEALTHY:
            self.status = Status.SICK
        elif self.status == Status.SICK:
            self.status = Status.RECOVERED
        elif self.status == Status.RECOVERED:
            self.status = Status.HEALTHY
