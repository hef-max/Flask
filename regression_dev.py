from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
app = Flask(__name__, template_folder='templates')
@app.route('/')
def student():
   return render_template("home.html")

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(-1,1)
    loaded_model = joblib.dump('model.sav')
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/success/<nilai>')
def success(nilai):
   return render_template('home.html', nilai = nilai)

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    to_predict_list = request.form['BI']
    to_predict_list= list(int(to_predict_list.values()))
    to_predict_list = list(map(float, to_predict_list))
    result = float(ValuePredictor(to_predict_list))

    return redirect(url_for('success', hasil= hasil))

if __name__ == '__main__':
   app.run(debug = True)