class Client:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Terminal with id {self.id}."