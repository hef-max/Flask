from flask import Flask, render_template, request, redirect
import mysql.connector as mysql

db = mysql.connect(
	host="localhost",
	user="root",
	password="",
	database="learn_rest_api"
	)
cursor = db.cursor()

app = Flask(__name__, template_folder="templates")

@app.route('/')
def main():
	query = "SELECT * FROM `mahasiswa`"
	cursor.execute(query)
	tabel = cursor.fetchall()
	return render_template('index.html', tabels=tabel)


@app.route('/simpan', methods=['POST'])
def simpan():
	nama = request.form['ID']
	query = "INSERT INTO `mahasiswa`(`id`, `nrp`, `nama`, `email`, `jurusan`) VALUES (%d,[value-2],[value-3],[value-4],[value-5])"
	mysql.connection.commit()
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)
