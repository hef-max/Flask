from flask import Flask, render_template
import mysql.connector as mysql

db  = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="kuliah"
)
cursor = db.cursor()

app = Flask(__name__, template_folder="templates")

@app.route('/mahasiswa')
def main():
    query = 'SELECT * FROM tbl_mahasiswa;'
    cursor.execute(query)
    row = cursor.fetchall()
    id = 'NIM'
    return render_template('index.html', index=id, tables=row)

@app.route('/dosen')
def dosen():
    query = 'SELECT * FROM tbl_dosen;'
    cursor.execute(query)
    row = cursor.fetchall()
    id= 'id'
    return render_template('index.html', index=id, tables=row)

@app.route('/bo')
def bo():
    query = 'SELECT * FROM tbl_bo;'
    cursor.execute(query)
    row = cursor.fetchall()
    id = 'id'
    return render_template('index.html', index=id, tables=row)

cursor.close()
if __name__ == '__main__':
    app.run(debug=True)