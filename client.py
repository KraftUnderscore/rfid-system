import paho.mqtt.client as mqtt

class Client:
    def __init__(self, id):
        self.id = -1
        self.removed = False
    
    def setRemoved(self, removed):
        self.removed = removed

    def __str__(self):
        return f"Terminal with id {self.id}."

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

def read():
    print("-----READING RFID-----")
    UID = rfids[input("Input RFID number (1-9): ")]
    num = 0
    for i in range(0, len(UID)):
        num += UID[i] << (i*8)
    return num

client = mqtt.Client()
broker = "localhost"
clientId = -1

def connect():
    client.connect(broker)
    client.publish("client", "connected:ID",)

def disconnect():
    client.publish("client", "disconnected:ID",)
    client.disconnect()

def main():
    clientId = int(input("Input terminal ID(positive integer): "))
    if(clientId<0):
        print("Invalid id. Terminating...")
        return
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
            > read - simulate an RFID card input""")
        elif token == "read":
            RFID = read()
            client.publish("client", f"rfid:{RFID}",)
        else:
            print(f"Unrecognised command '{token}'.")
    disconnect()

if __name__ == "__main__":
    main()