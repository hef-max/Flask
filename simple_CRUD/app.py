from flask import Flask, render_template, request, redirect
import mysql.connector as mysql

db = mysql.connect(
	host="localhost",
	user="root",
	password="",
	database="curdflask"
	)

cursor = db.cursor()

app = Flask(__name__, template_folder="templates")

@app.route('/')
def main():
	query = "SELECT * FROM `computer`"
	cursor.execute(query)
	tabel = cursor.fetchall()
	return render_template('index.html', tabels=tabel)

@app.route('/simpan', methods=['POST'])
def simpan():
	nama = request.form['nama']
	cursor.execute("INSERT INTO `computer`(nama) VALUES (%s)",(nama,))
	db.commit()
	return redirect("/")

@app.route('/update', methods=["PUT"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    cursor.execute("UPDATE `computer` SET nama=%s WHERE id=%s", (nama, id_data,))
    db.commit()
    return redirect("/")

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cursor.execute("DELETE FROM `computer` WHERE id=%s", (id_data,))
    db.commit()
    return redirect("/")

if __name__=='__main__':
	app.run(debug=True)
