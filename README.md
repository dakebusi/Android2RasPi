# Android2RasPi

Small project to connect an Android phone to a Raspberry Pi.

The aim of the project is to be able to send information from the Android phone (e.g. GPS readings, battery levels, accelerometer data...) to a Raspberry Pi.

This is achieved via websockets:

* A process in the Raspberry Pi opens and listens to a websocket
* The Android phone sends the data to the websocket opened by the Raspberry Pi

The project has 3 files:

* raspi_server.py: this is the process running on the Raspberry Pi. It creates a websocket and listens to it for incoming messages. When receiving one, it tries to decode it as a JSON message (since most of the messages coming from Android will be in JSON format) and prints out the result. It also echoes back the received message to the sender, though this is just for debugging purposes and could be removed. 

* simple_client.py: This is just an example of how to send a message via websockets. It creates the connection, sends a message and then waits for an answer from the other side. You can run this process on any machine. You should change the IP of the websocket (e.g. ws://192.168.1.12:8082) to match the IP address of the machine running server.py.

* android_client.py: This is the process running on the Android phone. It creates the websocket connection as in simple_client.py, and then it sends 5 times (with some delay in between) the last known location (using AndroidHelper) of the phone.
