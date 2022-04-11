from flask import Flask, request, jsonify
import mysql.connector as mysql
import numpy as np

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="unive"
)

cursor = db.cursor()

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=['GET'])
def show():
    query = """
    SELECT *
    FROM  `mahasiswa` m
    INNER JOIN `prodi` p
    USING(kode_prodi);"""
    cursor.execute(query)
    tables = cursor.fetchall()
    json = jsonify(tables)
    if json.status_code == 200:
        return json
    else:
        return jsonify("error 200")

@app.route("/addUser", methods=['POST'])
def add():
    json = request.json
    nim = json["mahasiswa"]
    nama_lengkap = json["mahasiswa"]
    tanggal_lahir = json["mahasiswa"]
    jenis_kelamin  = json["mahasiswa"]
    prodi  = json["mahasiswa"]
    kode_prodi  = json["mahasiswa"]
    keterangan = json["mahasiswa"]
    array = np.array([nim, nama_lengkap, jenis_kelamin, tanggal_lahir, kode_prodi, prodi, keterangan])
    
    if request.method == 'POST':
        for i in range(0, len(json['mahasiswa'])):
            cursor.execute(f"""
            INSERT INTO `mahasiswa` VALUES(
            '{array[0][i]['nim']}',
            '{array[0][i]['nama_lengkap']}',
            '{array[0][i]['jenis_kelamin']}',
            DATE '{array[0][i]['tanggal_lahir']}',
            '{array[0][i]['kode_prodi']}'
            );""")
            cursor.execute(f"""INSERT INTO `prodi` VALUES(
                '{array[0][i]['kode_prodi']}',
                '{array[0][i]['prodi']}',
                '{array[0][i]['keterangan']}'
            );
            """)
            db.commit()

        json = jsonify("User data succesfully inserted")
        if json.status_code == 200:
            return json
        else:
            return jsonify("error 200")
    else:
        json = jsonify("user data not inserted")
        return json

if __name__ == '__main__':
    app.run(debug=True)
    