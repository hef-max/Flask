from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"
@app.route('/nama')
def index2():
    return "halama nama"
@app.route('/nama/<string:nama>')
def index3(nama):
    return 'nama saya adalah {}'.format(nama)
@app.route('/mahasiswa')
def getmahasiswa():
    nama = 'Hefry'
    kelas = 'D'
    hobi = ['Baca Buku', 'Coding','Observasi']
    return render_template('mahasiswa.html', nama= nama, kelas= kelas, hobi=hobi)


@app.route('/success/<hasil>')
def success(hasil):
   return render_template('kalku.html', hasil=hasil)

@app.route('/kalku', methods= ['POST', 'GET'])
def kalku():
    if request.method == 'POST':
        x = int(request.form['x'])
        y = int(request.form['y'])
        hasil = x + y
        return redirect(url_for('success', hasil = hasil))

    else:
        x = request.args.get('x')
        y = request.args.get('y')
        return redirect(url_for('success', hasil = x))


# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


if __name__ == '__main__':
    app.run(debug=True)