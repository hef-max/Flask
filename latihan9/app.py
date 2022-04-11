from flask import Flask, render_template, session, request
import mysql.connector as mysql

db = mysql.connect(
	host='localhost',
	user='root',
	password='',
	database='sia_3nimanda'
	)
cursor = db.cursor()

app = Flask(__name__, template_folder='templates')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		key = request.form['password']
		cursor.execute('SELECT * FROM `users` WHERE username_178=%s;',(username,))
		user = cursor.fetchall()

		if len(user) > 0:
			if key == user[0][3]:
				session['user'] = username
				session['password'] = key
				return render_template('home.html', user=user[0][1])
			else:
				return "User id not match!"
		else:
			return "User not found!"
	else:
		return render_template('index.html')

@app.route('/logout')
def logout():
	session.clear()
	cursor.close()
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)