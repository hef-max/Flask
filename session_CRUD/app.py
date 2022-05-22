from flask import Flask,render_template, request, redirect, session, flash, url_for
from functools import wraps
import mysql.connector as mysql

app=Flask(__name__, template_folder='templates')

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="kuliah"
    )

cur = db.cursor()
cek = []

####################################################### 

#Login
@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["password"]
        cur.execute("SELECT * FROM `users` WHERE email=%s AND pass=%s",(email, pwd, ))
        data = cur.fetchone()
        if data:
            cek.append(1)
            session['logged_in'] = True
            session['username'] = data[0]
            flash('Login Successfully','success')
            return redirect(url_for('index'))
        else:
            flash('Invalid Login. Try Again','danger')
    else:
        return render_template("login.html")
  
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap
  
#Registration  
@app.route('/reg',methods=['POST','GET'])
def reg():
    status=False
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        pwd=request.form["password"]
        cur.execute("INSERT INTO `users` (password, nama) VALUES (%s, %s, %s)",(pwd, name, email ))
        db.commit()
        cur.close()
        flash('Registration Successfully. Login Here...','success')
        return redirect('login')
    return render_template("reg.html",status=status)
    
#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))

###########################################

@app.route('/index')
def index():
    sql = "SELECT * FROM `tbl_mahasiswa`;"
    cur.execute(sql)
    results = cur.fetchall()
    cek.clear()
    return render_template('home.html', data=results)

# untuk membuat form tambah
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        npm = request.form['npm']
        nama = request.form['nama']
        prodi = request.form['prodi']
        cur.execute("INSERT INTO `tbl_mahasiswa` VALUES (%s, %s, %s);",(npm, nama, prodi, ))
        db.commit()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')

# untuk form edit
@app.route('/edit/<int:npm>', methods=['POST', 'GET'])
def update(npm):
    cur.execute('SELECT * FROM `tbl_mahasiswa` WHERE npm=%s',(npm, ))
    results = cur.fetchone()
    # print("npm:",npm,"resuls:", results)
    if request.method == 'POST':
        npm = request.form['npm']
        nama = request.form['nama']
        prodi = request.form['prodi']
        cur.execute("UPDATE `tbl_mahasiswa` SET nama=%s, prodi=%s WHERE npm=%s;",(nama, prodi, npm, ))
        db.commit()
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", id_data=results[0]) 
      
# untuk menghapus data
@app.route('/hapus/<int:npm>', methods=['GET','POST'])
def hapus(npm):
    cur.execute('DELETE FROM `tbl_mahasiswa` WHERE npm=%s',(npm, ))
    db.commit()
    return redirect(url_for('index'))

if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)
