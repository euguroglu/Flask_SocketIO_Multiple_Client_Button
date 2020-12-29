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
    emit('from flask',message)

if __name__ == "__main__":
    socketio.run(app)
