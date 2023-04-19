from flask import Flask, render_template,request,jsonify
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
    return jsonify(db)


db = {'users':{},'messages':[]}


# connected
@socketio.on('connected')
def connect(data):
    print(data)
    sid = request.sid
    user = {'session_id':sid,'userKey':data['userKey']}
    db['messages'].append(data)
    if sid in db['users'].keys():
        print(f'{user} is refused')
        socketio.emit('connected',{'user':user,'connected':False,'because':'same sid user'})
        return False
    else:
        db['users'][user['session_id']] = user
        print(f'{user} is connected!')
        socketio.emit('usersCount',db['users'])
        socketio.emit('connected',{'user':user,'connected':True,'countUsers':len(db['users'])})


#disconnected
@socketio.on('disconnect')
def disconnected():
    user = db['users'][request.sid]
    print(f'{user} is disconnected')
    del db['users'][request.sid]
 
    socketio.emit('usersCount',db['users'])
    socketio.emit('connected',{'user':user,'connected':True,'countUsers':len(db['users'])})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)