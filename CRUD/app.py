from flask import Flask, render_template, request, redirect, flash
from model import *

app = Flask(__name__, template_folder="templates")
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

model = Model()

@app.route('/') #success
def read():
	row_data = model.read() 
	return render_template('index.html', data=row_data)

@app.route('/create', methods=["POST", "GET"]) #success
def create():
	if request.method == "POST":	
		ID_178 = request.form['user_id']
		Name_178 = request.form['user_name']
		Level_178 = request.form['user_level']
		Classes_178 = request.form['user_classes']
		Build_178 =  ','.join(request.form.getlist('user_build'))
		Bio_178 = request.form['user_bio']

		if model.create(ID_178, Name_178, Level_178, Classes_178, Build_178, Bio_178):
			flash("Data Bertambah")
		else:
			flash("Data tidak bertambah")
		return redirect("/")
	else:	
		return redirect("/")

@app.route('/update', methods=["POST", 'PUT']) #success
def update():
	if request.method == "POST":	
		ID_178 = request.form['user_id']
		Name_178 = request.form['user_name']
		Level_178 = request.form['user_level']
		Classes_178 = request.form['user_classes']
		Build_178 = ','.join(request.form.getlist('user_build'))
		Bio_178 = request.form['user_bio']

		if model.update(ID_178, Name_178, Level_178, Classes_178, Build_178, Bio_178):
			flash("Data Berhasil diUbah")
		else:
			flash("data tidak Berhasil diUbah")
		return redirect("/")
	else:
		return redirect('/')

@app.route('/del/<int:ID_178>', methods=["GET"]) #success
def delete(ID_178):
	if request.method == "GET":
		model.delete(ID_178)
		flash("Berhasil diHapus")
	else:
		flash("Gagal diHapus")	
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)