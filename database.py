from client import Client
from worker import Worker
from fileshandler import *
import time
from datetime import datetime

class Database():
    def __init__(self):
        self.clients = loadClients()
        self.workers = loadWorkers()
        self.nextWorkerId = len(self.workers)
        self.nextClientId = len(self.clients)

    def addClient(self):
        self.clients.append(Client(self.nextClientId))
        print(f"Added client with id {self.nextClientId}.")
        self.nextClientId+=1
        saveClients(self.clients)

    def removeClient(self, clientId):
        for client in self.clients:
            if client.id == clientId and client.removed == False:
                client.setRemoved(True)
                print(f"Removed client with id {clientId}.")
                saveClients(self.clients)
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
        saveWorkers(self.workers)

    def rmWorker(self, workerId):
        worker = self.findWorker(workerId)
        if worker != None:
            worker.removed = True
            saveWorkers(self.workers)
            print(f"Removed worker {worker.name} with id {workerId}.")
        else:
            print(f"Worker with id {workerId} doesn't exist!")

    def addRFID(self, workerId, RFID):
        worker = self.findWorker(workerId)
        if worker:
            if worker.card == -1:
                worker.setCard(RFID)
                print(f"Added RFID {RFID} to worker {worker.name} with id {worker.id}.")
                saveWorkers(self.workers)
            else:
                print(f"Worker {worker.name} with id {worker.id} RFID card assigned with id {worker.card}.")
        else:
            print(f"Worker with id {workerId} not found.")

    def rmRFID(self, workerId):
        worker = self.findWorker(workerId)
        if worker:
            if worker.card == -1:
                print(f"Worker {worker.name} with id {worker.id} doesn't have any RFID cards assigned.")
            else:
                print(f"Removed RFID card {worker.card} from worker {worker.name} with id {worker.id}.")
                worker.setCard(-1)
                saveWorkers(self.workers)
        else:
            print(f"Worker with id {workerId} not found.")

    def printWorkers(self):
        print("List of workers:")
        for worker in self.workers:
            if worker.removed == False:
                print(worker)

    def printClients(self):
        print("List of clients:")
        for client in self.clients:
            if client.removed == False:
                print(client)

    def addLog(self, RFID, clientId):
        if clientId >= self.nextClientId:
            print(f"No terminal with id {clientId}!")
            return
        for worker in self.workers:
            if worker.card == RFID and worker.removed == False:
                log = f"{clientId},{worker.id},{RFID},{time.time()}\n"
                saveLogs(log)
                print(f"Logged {worker.name} at terminal {clientId} with RFID {RFID}.")
                return
        print(f"Logged unknown at terminal {clientId} with RFID {RFID}.")
        log = f"{clientId},{-1},{RFID},{time.time()}\n"
        saveLogs(log)

    def generateReport(self, workerId):
        worker = self.findWorker(workerId)
        if worker:
            print(f"Generating report for {worker.name} with id {workerId}.")
            logs = loadWorkerLogs(workerId)
            output = "RFID,startClientId,endClientId,workerId,workerName,startTime,endTime,workTime\n"
            for i in range(0, len(logs)-1, 2):
                log = logs[i]
                nextLog = logs[i+1]
                startTime = datetime.fromtimestamp(int(log[3].split(".")[0]))
                endTime = datetime.fromtimestamp(int(nextLog[3].split(".")[0]))
                workTime = endTime - startTime
                output+=f"{log[2]},{log[0]},{nextLog[0]},{log[1]},{worker.name},{startTime},{endTime},{workTime}\n"

            if len(logs)%2==1:
                log = logs[len(logs)-1]
                startTime = datetime.fromtimestamp(int(log[3].split(".")[0]))
                output+=f"{log[2]},{log[0]},,{log[1]},{worker.name},{startTime},,\n"

            filename = f"{worker.name}ID{workerId}.csv"
            saveReport(output, filename)
            print(f"Report generated.\nOutput in file '{filename}'")
        else:
            print(f"No worker with id {workerId}!")