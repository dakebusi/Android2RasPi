from bottle import request, Bottle, abort
from json import loads

app = Bottle()

@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = wsock.receive()
            wsock.send("Your message was: %r" % message)
            json_msg = loads(message)
            print 'JSON message received', json_msg
        except WebSocketError:
            break
        except ValueError:
            print 'Non JSON message received', message

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
server = WSGIServer(("0.0.0.0", 8082), app,
                    handler_class=WebSocketHandler)
server.serve_forever()
