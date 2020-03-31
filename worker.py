class Worker:
    def __init__(self, name, id):
        self.name = name
        self.card = -1
        self.id = id
        self.removed = False

    def setCard(self, RFID):
        self.card = RFID

    def setRemoved(self, removed):
        self.removed = removed

    def __str__(self):
        tmp = ""
        if self.card == -1:
            tmp = "none"
        else:
            tmp = str(self.card)
        return f"Worker {self.name} with id {self.id}. \n > Assigned card: {tmp}"