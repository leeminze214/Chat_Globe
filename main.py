from flask import Flask, redirect, render_template, request, url_for, session
from flask_socketio import SocketIO, join_room, leave_room
import sys
import json
sys.path.append('secret_chat\db_tools\methods.py')
from db_tools.methods import db_methods

with open('auth.json') as auth:
    secret = json.load(auth)
#------------------flask routes----------------------#

app = Flask(__name__)
app.config['SECRET_KEY'] = secret['secret_key']
io = SocketIO(app)
execute = db_methods()

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')


#-----------------------socket------------------------#
#handle connection to home page
@io.on('home_connection')
def connect_home():
    session['location'] = 'non-chat'
    print('a client has connected to home')

@io.on('disconnect')
def disconeted():
    print('a client has disconnected')
    
if __name__ == '__main__':
    io.run(app, debug = True)