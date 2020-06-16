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

broker = "DESKTOP-LD3U7DI"
port = 8883
server = mqtt.Client()
db = Database()

def receive_message(client, data, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(":")
    token = message_decoded[0]
    value = int(message_decoded[1])
    if token == "rfid":
        db.addLog(value, int(message_decoded[2]))
    elif token == "connected":
        print(f"Terminal with id {value} {message_decoded[0]}.")
        db.addClient(value)
    elif token == "disconnected":
        print(f"Terminal with id {value} {message_decoded[0]}.")
        db.rmClient(value)

def connect():
    server.tls_set("ca.crt")
    server.username_pw_set(username='server', password=input("PASSWORD:"))#password123
    server.connect(broker, port)
    server.on_message = receive_message
    server.subscribe("worker")
    server.loop_start()

def disconnect():
    server.loop_stop()
    server.disconnect()

def main():
    connect()
    isRunning = True
    while(isRunning):
        token = input(">")
        if token == "exit":
            isRunning = False
        elif token == "help":
            print("""Command list:
            > help - list of all commands
            > exit - end server
            > addWorker - add a new worker to the system
            > rmWorker - remove an existing worker from the system
            > addRFID - add an RFID card to an existing worker
            > rmRFID - remove an RFID card from an existing worker
            > lsWorkers - list all workers in the system
            > lsClients - list all terminals in the system
            > generateReport - generate a .csv file with worktime of selected worker.""")
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