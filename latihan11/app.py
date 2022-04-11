from flask import Flask, config, render_template, request, jsonify, Response
import mysql.connector as mysql

#config db
db = mysql.connect(
    host = "localhost",
    user= "root",
    password= "",
    database= "sia_178"
)

#config flask
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user', methods=['GET'])
def main():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mhs_178;")
    tabels = cursor.fetchall()
    res = jsonify(tabels)
    res.headers.set('Access-Control-Allow-Origin', '*')
    return res

if __name__ == '__main__':
    app.run(debug=True)

