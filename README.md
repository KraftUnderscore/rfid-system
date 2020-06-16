# RFID System - IoT project

This is a project to-be implemented on an Raspberry Pi system on Internet of Things course. The idea is having a server (on Raspberry itself
or on a PC) and a Raspberry client equipped with RFID scanner. The system is supposed to be keeping track of workers that check in and out
with their unique RFID tags.

### Requirements for the system
- multiple clients,
- adding and removing clients,
- asigning and removing RFID cards from workers,
- keeping track of when and on which terminal was a tag scanned along with its ID (whether a worker checked in, out or the ID was unknown)
- generating reports of worker's worktime,
- using MQTT Mosquitto as broker between server and clients,
- using OpenSSL for SSL/TLS.

### How it works
Each Client can simulate an RFID input which is then sent over to broker via specific channel which the Server is subscribed to. If every terminal was successfully logged in then Server receives a message with RFID number and corresponding Client ID. Data gets saved to a simple database (custom made to minimize overhead and space usage). It can be accessed via Server.
