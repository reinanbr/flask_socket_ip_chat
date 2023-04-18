from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

'''the scoketio init'''
socketio = SocketIO(app,cors_allowed_origins="*",async_mode=None)

@app.route('/')
def index():
    return 'on'

# connected
@socketio.on('connected')
def connect(data):
    print(data)


#disconnected
@socketio.on('disconnect')
def disconnected(data_):
    print(data_)
    socketio.on('disconnect',data_)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)