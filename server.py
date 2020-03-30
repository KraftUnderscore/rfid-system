from database import Database
import time

#will be done using client
def read():
    print("-----READING RFID-----")
    return int(input("Input RFID number (1-9): ")*5)

def populateDatabase(db):
    db.addClient()
    db.addClient()
    db.addClient()

    db.addWorker("Sebastian")
    db.addWorker("Michal")
    db.addWorker("Agnieszka")

    db.addRFID(0, 33333)
    time.sleep(0.05)
    db.addRFID(0, 77777)
    time.sleep(0.05)
    db.addRFID(1, 55555)
    time.sleep(0.05)
    db.addRFID(2, 99999)
    time.sleep(0.05)
    db.addRFID(2, 22222)
    time.sleep(0.05)

    db.addLog(33333, 0)
    time.sleep(0.05)
    db.addLog(55555, 1)
    time.sleep(0.05)
    db.addLog(99999, 2)
    time.sleep(0.05)
    db.addLog(33333, 0)
    time.sleep(0.05)
    db.addLog(55555, 1)
    time.sleep(0.05)
    db.addLog(99999, 2)
    time.sleep(0.05)
    db.addLog(77777, 0)
    time.sleep(0.05)
    db.addLog(22222, 1)
    time.sleep(0.05)
    db.addLog(55555, 2)
    time.sleep(0.05)
    db.addLog(77777, 0)
    time.sleep(0.05)
    db.addLog(22222, 1)
    time.sleep(0.05)
    db.addLog(55555, 2)   

def main():
    db = Database()
    if input("Load sample database? (Y/N): ") == "Y":
        populateDatabase(db)

    isRunning = True
    while(isRunning):
        token = input(">")
        if token == "end":
            isRunning = False
        elif token == "help":
            print("""Command list:
            > help - list of all commands
            > end - end server
            > addClient - add a new terminal to the system
            > rmClient - remove an existing terminal from the system
            > addWorker - add a new worker to the system
            > rmWorker - remove an existing worker from the system
            > addRFID - add an RFID card to an existing worker
            > rmRFID - remove an RFID card from an existing worker
            > lsWorkers - list all workers in the system
            > lsClients - list all terminals in the system
            > read - simulate an RFID card input
            > logWorker - print logs of a single worker in CSV format
            > logAllWorkers - print logs of all workers in CSV format\n""")
        elif token == "addClient":
            db.addClient()
        elif token == "rmClient":
            clientId = int(input("Input client id (integer): "))
            db.removeClient(clientId)
        elif token == "addWorker":
            db.addWorker(input("Input worker's name: "))
        elif token == "rmWorker":
            db.rmWorker(int(input("Input worker's id (integer): ")))
        elif token == "addRFID":
            workerId = int(input("Input worker's id (integer): "))
            RFID = read()
            db.addRFID(workerId, RFID)
        elif token == "rmRFID":
            workerId = int(input("Input worker's id (integer): "))
            RFID = read()
            db.rmRFID(workerId, RFID)
        elif token == "read":
            clientId = int(input("Input client id (integer): "))
            RFID = read()
            db.addLog(RFID, clientId)
        elif token == "lsWorkers":
            db.printWorkers()
        elif token == "lsClients":
            db.printClients()
        elif token == "logWorker":
            print(db.getWorkerCSV(int(input("Input worker's id (integer): "))))
        elif token == "logAllWorkers":
            print(db.getAllWorkerCSV())
        elif token == "test":
            print(db.getWorkerLogs(int(input("Input worker's id (integer): "))))
        else:
            print(f"Unrecognised command '{token}'.")
            
if __name__ == "__main__":
    main()