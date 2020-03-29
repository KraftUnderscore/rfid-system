class Worker:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def addId(self, id):
        self.cards.append(id)
        print(f"Added RFID {id} to worker {self.name}")

    def rmId(self, id):
        self.cards.remove(id)
        print(f"Removed RFID {id} from worker {self.name}")