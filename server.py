import os
from core.app import app
from gevent.pywsgi import WSGIServer
import werkzeug.serving


app.config['PROPAGATE_EXCEPTIONS'] = True

@werkzeug.serving.run_with_reloader
def runServer():
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    print("Gevent serve forever on", 5000)
    http_server.serve_forever()
