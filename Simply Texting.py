Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request
... from flask_socketio import SocketIO, send
... 
... app = Flask(Simply Texting)
... app.config['SECRET_KEY'] = 'your_secret_key'
... socketio = SocketIO(app)
... 
... # Store messages for displaying in the chat
... messages = []
... 
... @app.route('/')
... def index():
...     return render_template('chat.html')
... 
... @socketio.on('message')
... def handle_message(msg):
...     global messages
...     print(f"Message received: {msg}")
...     messages.append(msg)
...     send(msg, broadcast=True)  # Broadcast message to all connected clients
... 
... if __Simply Texting__ == '__main__':
...     socketio.run(app, debug=True)
