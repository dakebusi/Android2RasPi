#-*-coding:utf8;-*-
#qpy:2
#qpy:console
from websocket import create_connection
import androidhelper
from json import dumps
from time import sleep

droid = androidhelper.Android()

ws = create_connection("ws://192.168.1.12:8080/websocket")
for i in range(5):
    print "Sending position..."
    pos = droid.getLastKnownLocation()
    ws.send(dumps(pos))
    sleep(5)

ws.close()