from database import Database
import time

rfids = {
    "1" : [176, 111, 225, 37, 27], #116599648176
    "2" : [217, 125, 80, 211, 39], #171048992217
    "3" : [92, 43, 129, 240, 18], #81344408412
    "4" : [60, 218, 39, 194, 147], #634617584188
    "5" : [79, 26, 128, 195, 205], #883748248143
    "6" : [123, 175, 29, 54, 109], #469059350395
    "7" : [92, 49, 137, 251, 123], #532501049692
    "8" : [19, 39, 149, 209, 29], #128070264595
    "9" : [18, 56, 172, 213, 119] #514685941778
}

#will be done using client
def read():
    print("-----READING RFID-----")
    UID = rfids[input("Input RFID number (1-9): ")]
    num = 0
    for i in range(0, len(UID)):
        num += UID[i] << (i*8)
    return num

def populateDatabase(db):
    db.addClient()
    db.addClient()
    db.addClient()

    db.addWorker("Sebastian")
    db.addWorker("Michal")
    db.addWorker("Agnieszka")

    db.addRFID(0, 116599648176)
    time.sleep(0.05)
    db.addRFID(0, 171048992217)
    time.sleep(0.05)
    db.addRFID(1, 81344408412)
    time.sleep(0.05)
    db.addRFID(2, 634617584188)
    time.sleep(0.05)
    db.addRFID(2, 883748248143)
    time.sleep(0.05)

    db.addLog(116599648176, 0)
    time.sleep(0.05)
    db.addLog(81344408412, 1)
    time.sleep(0.05)
    db.addLog(634617584188, 2)
    time.sleep(0.05)
    db.addLog(116599648176, 0)
    time.sleep(0.05)
    db.addLog(81344408412, 1)
    time.sleep(0.05)
    db.addLog(634617584188, 2)
    time.sleep(0.05)
    db.addLog(171048992217, 0)
    time.sleep(0.05)
    db.addLog(883748248143, 1)
    time.sleep(0.05)
    db.addLog(81344408412, 2)
    time.sleep(0.05)
    db.addLog(171048992217, 0)
    time.sleep(0.05)
    db.addLog(883748248143, 1)
    time.sleep(0.05)
    db.addLog(81344408412, 2)   

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
            > read - simulate an RFID card input
            > addClient - add a new terminal to the system
            > rmClient - remove an existing terminal from the system
            > addWorker - add a new worker to the system
            > rmWorker - remove an existing worker from the system
            > addRFID - add an RFID card to an existing worker
            > rmRFID - remove an RFID card from an existing worker
            > lsWorkers - list all workers in the system
            > lsClients - list all terminals in the system
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