class Client:
    def __init__(self, id):
        self.id = id
        self.removed = False
    
    def setRemoved(self, removed):
        self.removed = removed

    def __str__(self):
        return f"Terminal with id {self.id}."