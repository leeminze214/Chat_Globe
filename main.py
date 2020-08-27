from flask import Flask, redirect, render_template, request, url_for
from flask_socketio import SocketIO
from config import db_conn
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = "(**#HRWOIFHN:LEHIKF(*#YHNL)#&)87293847290834htoirhgh9g8hs098hg"
io = SocketIO(app)
params = db_conn()
conn = psycopg2.connect(**params)
cursor = conn.cursor()

if __name__ == '__main__':
    io.run(app)