from client import Client
from worker import Worker
import worker

class Database():
    def __init__(self):
        self.logs = []
        self.clients = []
        self.nextClientId = 0

    def addClient(self):
        self.clients.append(Client(self.nextClientId))
        print(f"Added client with id {self.nextClientId}.")
        self.nextClientId+=1

    def removeClient(self, clientId):
        for client in self.clients:
            if client.id == clientId:
                self.clients.remove(client)
                print(f"Removed client with id {clientId}.")
                return
        print(f"No client with id {clientId}.")

    def addLog(self, timestamp, clientId, workerId):
        self.logs.append((timestamp, clientId, workerId))

    def generateReport(self, workerId):
        output = []
        for log in self.logs:
            if log[2] == workerId:
                output.append((log[0], log[1]))
        return output