import paho.mqtt.client as mqtt
from database import Database
import time

rfids = {
    "1" : 116599648176,
    "2" : 171048992217,
    "3" : 81344408412,
    "4" : 634617584188,
    "5" : 883748248143,
    "6" : 469059350395,
    "7" : 532501049692,
    "8" : 128070264595,
    "9" : 514685941778
}

broker = "localhost"
server = mqtt.Client()

def receive_message(client, data, message):
    message_decoded = (str(message.payload.decode("utf-8")))
    print(f"Received message: {message_decoded}")

def connect():
    server.connect(broker)
    server.on_message = receive_message
    server.loop_start()
    server.subscribe("client")

def disconnect():
    server.loop_stop()
    server.disconnect()

def main():
    connect()
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
            RFID = rfids[input("Input RFID number (1-9): ")]
            db.addRFID(workerId, RFID)
        elif token == "rmRFID":
            workerId = int(input("Input worker's id (integer): "))
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
        else:
            print(f"Unrecognised command '{token}'.")
    disconnect()

if __name__ == "__main__":
    main()