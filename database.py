from client import Client
from worker import Worker
import time

class Database():

    class Log():
        def __init__(self, clientId, workerId, RFID):
            self.timestamp = time.time()
            self.clientId = clientId
            self.workerId = workerId
            self.RFID = RFID

    def __init__(self):
        self.logs = []
        self.clients = []
        self.workers = []
        self.nextWorkerId = 0
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
        print(f"No client with id {clientId}!")

    def findWorker(self, workerId):
        for worker in self.workers:
            if worker.id == workerId:
                if worker.removed == False:
                    return worker
        return None

    def addWorker(self, name):
        self.workers.append(Worker(name, self.nextWorkerId))
        print(f"Added worker {name} with id {self.nextWorkerId}.")
        self.nextWorkerId+=1

    def rmWorker(self, workerId):
        worker = self.findWorker(workerId)
        if worker != None:
            worker.removed = True
            print(f"Removed worker {worker.name} with id {workerId}.")
        else:
            print(f"Worker with id {workerId} doesn't exist!")
    #lacks feedback when worker not found
    def addRFID(self, workerId, RFID):
        worker = self.findWorker(workerId)
        if worker != None:
            worker.addCard(RFID)
    #same here
    def rmRFID(self, workerId, RFID):
        worker = self.findWorker(workerId)
        if worker != None:
            worker.rmCard(RFID)

    def printWorkers(self):
        print("List of workers:")
        for worker in self.workers:
            if worker.removed == False:
                print(worker)

    def printClients(self):
        print("List of clients:")
        for client in self.clients:
            print(client)

    def addLog(self, RFID, clientId):
        for worker in self.workers:
            for card in worker.cards:
                if card == RFID:
                    self.logs.append(self.Log(clientId, worker.id, RFID))
                    return
        self.logs.append(self.Log(clientId, -1, RFID))

    def getWorkerLogs(self, workerId):
        pass

    def getAllWorkerLogs(self):
        pass

    def getWorkerCSV(self, workerId):
        pass
    
    def getAllWorkerCSV(self):
        pass

    def generateReport(self, workerId):
        output = []
        for log in self.logs:
            if log.workerId == workerId:
                output.append((log.clientId, workerId, log.RFID, log.timestamp))
        return output