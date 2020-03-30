class Worker:
    def __init__(self, name, id):
        self.name = name
        self.cards = []
        self.id = id
        self.removed = False

    def addCard(self, id):
        if self.cards.count(id) >0:
            print(f"Worker {self.name} with id {self.id} already has RFID {id}.")
        else:
            self.cards.append(id)
            print(f"Added RFID {id} to worker {self.name} with id {self.id}.")

    def rmCard(self, id):
        if self.cards.count(id) > 0:
            self.cards.remove(id)
            print(f"Removed RFID {id} from worker {self.name} with id {self.id}.")
        else:
            print(f"Worker {self.name} with id {self.id} doesn't have RFID {id}")

    def __str__(self):
        return f"Worker {self.name} with id {self.id}. \n > Assigned cards: {self.cards}"