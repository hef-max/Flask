from flask import Flask, jsonify, render_template
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="unive"
)

app  = Flask(__name__, template_folder="templates")

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/tables', methods=['GET'])
def tables():
    cursor = db.cursor()
    cursor.execute("""
                    SELECT *
                    FROM mahasiswa m INNER JOIN prodi p 
                    USING(kode_prodi);
                    """)
    tabels = cursor.fetchall()
    res = jsonify(tabels)
    res.headers.set('Access-Control-Allow-Origin', '*')
    return res