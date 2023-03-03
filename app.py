import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":
        features = []

        age = request.form.get("age")
        features.append(float(age))

        sex = request.form.get("sex")
        features.append(float(sex))

        cp = request.form.get("cp")
        features.append(float(cp))

        trestbps = request.form.get("trestbps")
        features.append(float(trestbps))

        chol = request.form.get("chol")
        features.append(float(chol))

        fbs = request.form.get("fbs")
        features.append(float(fbs))

        restecg = request.form.get("restecg")
        features.append(float(restecg))

        thalach = request.form.get("thalach")
        features.append(float(thalach))

        exang = request.form.get("exang")
        features.append(float(exang))

        oldpeak = request.form.get("oldpeak")
        features.append(float(oldpeak))

        slope = request.form.get("slope")
        features.append(float(slope))

        ca = request.form.get("ca")
        features.append(float(ca))

        thal = request.form.get("thal")
        features.append(float(thal))

    else:
        return render_template('index.html')

    # features = [float(x) for x in request.form.values()]

  

    final_features = [np.array(features)]

    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if output==1:
        return render_template('index.html', prediction_text_yes='According to health report Patient have Heart Disease!')
       
    else:
        return render_template('index.html', prediction_text_no='According to health report Patient does not have Heart Disease!')
    
    # return render_template('index.html')


# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
