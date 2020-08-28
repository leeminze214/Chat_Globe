from flask import Flask, redirect, render_template, request, url_for, session
from flask_socketio import SocketIO, join_room, leave_room
from config import db_conn
import psycopg2
import json

with open('auth.json') as auth:
    secret = json.load(auth)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret['secret_key']
io = SocketIO(app)
params = db_conn()
conn = psycopg2.connect(**params)
cursor = conn.cursor()

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')


#-------------------socket handle------------------#
@io.on('home_connection')
def connected():
    session['location'] = 'home'
    print('a client has connected to home')

if __name__ == '__main__':
    io.run(app, debug = True)