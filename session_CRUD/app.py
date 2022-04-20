from flask import Flask,render_template, request, redirect, session, flash, url_for
from functools import wraps
import mysql.connector as mysql

app=Flask(__name__, template_folder='templates')

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
    )

cur = db.cursor()
 
####################################################### 

#Login
@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["password"]
        cur.execute("SELECT nama FROM `users` WHERE email=%s AND password=%s",(email, pwd, ))
        data = cur.fetchone()
        if data:
            session['logged_in'] = True
            session['username'] = data[0]
            flash('Login Successfully','success')
            return redirect(url_for('index'))
        else:
            flash('Invalid Login. Try Again','danger')
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
        cur.execute("INSERT INTO `users`(password, nama, email) values(%s, %s, %s)",(pwd, name, email, ))
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
   sql = "SELECT * FROM `data_penjualan`;"
   cur.execute(sql)
   results = cur.fetchall()
   return render_template('home.html', data=results)

# untuk membuat form tambah
@app.route('/tambah', methods=['POST'])
def tambah():
   if request.method == 'POST':
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      cur.execute("INSERT INTO `data_penjualan` (nama_barang, harga, stok) VALUES (%s, %s, %s);",(nama, harga, stok, ))
      db.commit()
      return redirect(url_for('index'))
   else:
      return render_template('tambah.html')

# untuk form edit
@app.route('/edit/<int:id_barang>', methods=['POST'])
def update(id_barang):
   cur.execute('SELECT * FROM `data_penjualan` WHERE id_barang=%s', (id_barang, ))
   results = cur.fetchone()
   if request.method == 'POST':
      id_barang = request.form['id_barang']
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      cur.execute("UPDATE `data_penjualan` SET nama_barang=%s, harga=%s, stok=%s WHERE id_barang=%s;",(nama, harga, stok, id_barang, ))
      db.commit()
      return redirect(url_for("index"))
   else:
      return render_template("edit.html", id_data=results[0]) 
      
# untuk menghapus data
@app.route('/hapus/<int:id_barang>', methods=['GET','POST'])
def hapus(id_barang):
   cur.execute('DELETE FROM `data_penjualan` WHERE id_barang=%s',(id_barang, ))
   db.commit()
   return redirect(url_for('index'))

if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)
