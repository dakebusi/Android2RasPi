import sys
from websocket import create_connection
ws = create_connection("ws://192.168.1.12:8082/websocket")
msg = sys.argv[1]
print 'Sending', msg 
ws.send(msg)
print "Sent"
print 'Receiving...'
result =  ws.recv()
print "Received '%s'" % result
ws.close()

