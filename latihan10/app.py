from flask import Flask, request, jsonify
import mysql.connector as mysql
import numpy as np

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="sia_178"
)

cursor = db.cursor()
app = Flask(__name__)

@app.route('/tampil', methods=['GET'])
def user():
    cursor.execute("SELECT * FROM tables;")
    users = cursor.fetchall()
    json = jsonify(users)
    if json.status_code == 200:
        return json
    else:
        return "error 200"

@app.route('/addUser', methods=['POST'])
def addUser():
    _json = request.json
    _nim_178 = _json["mahasiswa"]
    _nama_lengkap_178 = _json["mahasiswa"]
    _tempat_lahir_178 = _json["mahasiswa"]
    _tanggal_lahir_178 = _json["mahasiswa"]
    _gender_178  = _json["mahasiswa"]
    _alamat_178 = _json["mahasiswa"]
    _email_178 = _json["mahasiswa"]

    array = np.array([_nim_178, _nama_lengkap_178, _tempat_lahir_178,
     _tanggal_lahir_178,
     _gender_178,
     _alamat_178,
     _email_178])

    # print(array[0][0])
    # data = []
    # for i in range(0, len(_json['mahasiswa'])):
        # print(array[0][i]['nim_178'])
    #     data.append(array[i]['nim_178'])
    # print(data)

    # print(f"\n\n{_nim_178}\n\n,'{_nama_lengkap_178}','{_tempat_lahir_178}','{_tanggal_lahir_178}','{_gender_178}','{_alamat_178}','{_email_178}'")



    if request.method == 'POST':
        for i in range(0, len(_json['mahasiswa'])):
            cursor.execute(f"INSERT INTO mhs_178 VALUES({array[0][i]['nim_178']},'{array[0][i]['nama_lengkap_178']}','{array[0][i]['tempat_lahir_178']}',DATE '{array[0][i]['tanggal_lahir_178']}','{array[0][i]['gender_178']}','{array[0][i]['alamat_178']}','{array[0][i]['email_178']}');")
            db.commit()
        json = jsonify("User data succesfully inserted")
        if json.status_code == 200:
            return json
        else:
            return "error 200"
    else:
        json = jsonify("user data not inserted")
        return json
        
@app.route('/update', methods=['PUT'])
def update():
    _json = request.json
    _nim_178 = _json['nim_178']
    _nama_lengkap_178 = _json['nama_lengkap_178']
    _tanggal_lahir_178 = _json['tanggal_lahir_178']

    if request.method == 'PUT':
        cursor.execute(f"UPDATE mhs_178 SET nama_lengkap_178='{_nama_lengkap_178}', tanggal_lahir_178='DATE {_tanggal_lahir_178}' WHERE nim_178={_nim_178};")
        db.commit()
        json = jsonify("User data succesfully updated")
        if json.status_code == 200:
            return json
        else:
            return "error 200"
    else:
        json = jsonify("user data not update")
        return json

@app.route('/deleteuser/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute(f"DELETE FROM mhs_178 WHERE nim_178={id}")
    db.commit()
    json = jsonify('User Data Successfully Deleted.')
    if json.status_code == 200:
        return json
    else:
        return "error 200"

if __name__=='__main__':
    app.run(debug=True)