from worker import Worker
from client import Client
import time

class Log():
    def __init__(self, clientId, workerId, RFID):
        self.timestamp = time.time()
        self.clientId = clientId
        self.workerId = workerId
        self.RFID = RFID

def saveWorkers(allWorkers):
    f = open("workers.txt", "w")
    for worker in allWorkers:
        f.write(f"{worker.id},{worker.name},{worker.removed},{worker.card}\n")
    f.close()

def loadWorkers():
    f = open("workers.txt", "r")
    workers = []
    for worker in f:
        tmp = worker.split(",")
        toAdd = Worker(tmp[1], int(tmp[0]))
        toAdd.setCard(int(tmp[3]))
        if tmp[2] == "False":
            toAdd.setRemoved(False)
        else:
            toAdd.setRemoved(True)
        workers.append(toAdd)
    f.close()
    return workers

def saveClients(allClients):
    f = open("clients.txt", "w")
    for client in allClients:
        f.write(f"{client.id},{client.removed}\n")
    f.close()

def loadClients():
    f = open("clients.txt", "r")
    clients = []
    for client in f:
        infoStr = client.split(",")
        toAdd = Client(int(infoStr[0]))
        if infoStr[1] == "False\n":
            toAdd.setRemoved(False)
        else:
            toAdd.setRemoved(True)
        clients.append(toAdd)
    f.close()
    return clients

def saveLogs(log):
    f = open("logs.txt", "a")
    f.write(log)
    f.close()

def loadWorkerLogs(workerId):
    f = open("logs.txt", "r")
    workerLogs = []
    for log in f:
        log = log.split(",")
        if log[1] == str(workerId):
            workerLogs.append(log)
    f.close()
    return workerLogs

def saveReport(report, filename):
    f = open(filename, "w")
    f.write(report)
    f.close()