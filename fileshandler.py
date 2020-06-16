from worker import Worker
import time

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