from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required
from flaskext.mysql import MySQL
import pymysql.cursors

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'db_jwt178'

mysql.init_app(app)

app.config['SECRET_KEY'] = 'super-secret'


class User(object):
    def __init__(self, id_user, nama_user, username_user, password_user, hp_user, alamat_user):
        self.id = id_user
        self.nama = nama_user
        self.username = username_user
        self.password = password_user
        self.hp = hp_user
        self.alamat = alamat_user

        print(self.alamat)

    def __str__(self):
        return "User(id=%s)" % self.id

@app.route('/rest-auth')
@jwt_required()
def get_response():
    return jsonify('Anda Berhasil Masuk')

def authenticate(username, password): 
    if username and password:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_user, nama_user, username_user, password_user, hp_user, alamat_user FROM tb_user_178 WHERE username_user=%s",(username, ))
        row = cursor.fetchone()
        # print(row)
 
        if row:
            if (row['password_user'] == password):
                return User(row['id_user'], row['nama_user'], row['username_user'], row['password_user'], row['hp_user'], row['alamat_user'])
        else:
            return None
    else:
        return None

def identity(payload):
    if payload['identity']:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_user, username_user FROM tb_user_178 WHERE id_user=%s",(payload['identity'], ))
        row = cursor.fetchone()
        print("row2:",row)

        if row:
            return (row['id_user'], row['username_user'])
        else:
            return None
    else:
        return None

jwt = JWT(app, authenticate, identity)

print(jwt.auth_request_callback)

if __name__=='__main__':
    app.run(debug=True)