from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

##bisa juga seperti ini untuk membuat database
class User(db.Model): #nama tabel yang dibuat
    id = db.Column(db.Integer, primary_key=True) #atribut	
    name = db.Column(db.String(128)) #atribut

    def __repr__(self):
        return f"<User: {self.name}>"

####################################

sql = sqlite3.connect("app.db")
cursor = sql.cursor()

def create():
    cursor.execute("INSERT INTO `user` (name) VALUES ('hefry a');")
    sql.commit()
    return "success"

def read():
    cursor.execute("SELECT * FROM `user`;")
    for x in cursor.fetchall():
        print(x)
