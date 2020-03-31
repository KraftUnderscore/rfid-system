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

def main():
    db = Database()
    isRunning = True
    while(isRunning):
        token = input(">")
        if token == "exit":
            isRunning = False
        elif token == "help":
            print("""Command list:
            > help - list of all commands
            > exit - end server
            > read - simulate an RFID card input
            > addClient - add a new terminal to the system
            > rmClient - remove an existing terminal from the system
            > addWorker - add a new worker to the system
            > rmWorker - remove an existing worker from the system
            > addRFID - add an RFID card to an existing worker
            > rmRFID - remove an RFID card from an existing worker
            > lsWorkers - list all workers in the system
            > lsClients - list all terminals in the system
            > generateReport - generate a .csv file with worktime of selected worker.""")
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
            db.rmRFID(workerId)
        elif token == "read":
            clientId = int(input("Input client id (integer): "))
            RFID = read()
            db.addLog(RFID, clientId)
        elif token == "lsWorkers":
            db.printWorkers()
        elif token == "lsClients":
            db.printClients()
        elif token == "generateReport":
            print(db.generateReport(int(input("Input worker's id (integer): "))))
        elif token == "test":
            print(db.test())
        else:
            print(f"Unrecognised command '{token}'.")
            
if __name__ == "__main__":
    main()