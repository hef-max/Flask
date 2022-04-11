from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]
    print(init_features)
    print(final_features[0][0])

    prediction = model.predict(final_features)  # making prediction

    return render_template('index.html',
                           prediction_text='Predicted Class: {}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
