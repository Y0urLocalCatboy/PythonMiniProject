class Blob:
    def __init__(self, name, status, position):
        self.name = name
        self.status = status
        self.position = position
    def say_status(self):
        print("My status is {}".format(self.status))
    def say_hello(self):
        print("Hello, my name is {}".format(self.name))