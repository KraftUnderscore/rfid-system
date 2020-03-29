from database import Database

def read():
    #will be done using client
    return int(input("Input RFID number (1-9)")*5)

def main():
    db = Database()
    isRunning = True
    while(isRunning):
        token = input(">")
        if token == "end":
            isRunning = False
        elif token == "addClient":
            db.addClient()
        elif token == "rmClient":
            clientId = int(input("Input client id (integer): "))
            db.removeClient(clientId)
        elif token == "addRFID":
            pass
        elif token == "rmRFID":
            pass
        elif token == "read":
            rfid = read()
            clientId = int(input("Input clientId: "))
            

if __name__ == "__main__":
    main()