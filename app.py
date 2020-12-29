from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message from user')
def receive_message_from_user(message):
    print('USER MESSAGE:{}'.format(message))
    #Broadcast to send same message to all clients not only one who wrote message
    emit('from flask',message,broadcast=True)

#This code is creating message on the server side and emits to the clients
@app.route('/orginate')
def originate():
    socketio.emit('server orginated','Something happened on the server')
    return '<h1>Sent</h1>'

if __name__ == "__main__":
    socketio.run(app)
