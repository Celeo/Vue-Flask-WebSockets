#!/usr/bin/env python
from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import eventlet


eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return jsonify({'message': 'Index page'})


@socketio.on('connect')
def socketio_connect():
    print('Client has connected to the backend')
    emit('event', {'message': 'ACK'})


@socketio.on('event')
def socketio_message_event(message):
    print('Received event: ' + str(message))
    emit('response', {'message': 'Copy that'})


@socketio.on('response')
def socketio_message_response(message):
    print('Received response: ' + str(message))


if __name__ == '__main__':
    socketio.run(app, debug=True)
