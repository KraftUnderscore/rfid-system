import paho.mqtt.client as mqtt

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
    readId = input("Input RFID number [1-9]: ")
    if readId < '1' or readId > '9':
        print("Number out of range of [1-9]!")
        return -1
    UID = rfids[readId]
    num = 0
    for i in range(0, len(UID)):
        num += UID[i] << (i*8)
    return num

client = mqtt.Client()
broker = "DESKTOP-LD3U7DI"
port = 8883

def connect(clientId):
    client.tls_set("ca.crt")
    client.username_pw_set(username='client', password=input("PASSWORD:"))#password
    client.connect(broker, port)
    client.publish("client", f"connected:{clientId}",)

def disconnect(clientId):
    client.publish("client", f"disconnected:{clientId}",)
    client.disconnect()

def main():
    clientId =-1
    clientId = int(input("Input terminal ID(positive integer): "))
    if(clientId<0):
        print("Invalid id. Terminating...")
        return
    connect(clientId)
    isRunning = True
    while(isRunning):
        token = input(">")
        if token == "exit":
            isRunning = False
        elif token == "help":
            print("""Command list:
            > help - list of all commands
            > exit - end client
            > read - simulate an RFID card input""")
        elif token == "read":
            RFID = read()
            if RFID != -1:
                client.publish("worker", f"rfid:{RFID}:{clientId}",)
        else:
            print(f"Unrecognised command '{token}'.")
    disconnect(clientId)

if __name__ == "__main__":
    main()