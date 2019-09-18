from flask import Flask, request, render_template, make_response
from flask_socketio import SocketIO, send, emit
import random
import string

token_admin = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(5))
print("ADMIN TOKEN:", token_admin + "\n")

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def user_renderer():
    return render_template('user_index.html')

@app.route('/admin', methods=['POST', 'GET'])
def admin_handler():
    token = request.form.get('token') if request.method == 'POST' else request.cookies.get('token')

    if token == token_admin:
        response = make_response(render_template('index.html', show=True, error=None))

        if request.method == 'POST':
            response.set_cookie('token', token)

        return response
    else:
        response = make_response(render_template('index.html', show=False, error=None if token == None else 'Invalid token'))
        response.set_cookie('token', '', expires=0)

        return response

@socketio.on('msg')
def print_msg(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('msg', json)

@socketio.on('message')
def handle_msg(msg):
    print(msg)

@socketio.on('start')
def start_countdown(data):
    print(data.get("minutes"))
    socketio.emit('start', { "minutes": data.get("minutes"), "seconds": data.get("seconds") })

@socketio.on('stop')
def stop_countdown(self):
    socketio.emit('stop', 'data')

@socketio.on('resume')
def resume_countdown(self):
    socketio.emit('resume', 'data')

@socketio.on('reset')
def reset_countdown(self):
    socketio.emit('reset', 'data')

socketio.run(app, debug = False)
