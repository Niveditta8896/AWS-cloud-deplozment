from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('finalized_model_ckd.sav', 'rb'))

@app.route('/')
def home():
    return render_template('input.html')  # show the input form

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    bp = float(request.form['bp'])
    al = float(request.form['al'])
    su = float(request.form['su'])
    bgr = float(request.form['bgr'])
    bu = float(request.form['bu'])

    input_features = [[age, bp, al, su, bgr, bu]]

    prediction = model.predict(input_features)

    # Make result user-friendly
    if prediction[0] == 1:
        result = "⚠️ You have Chronic Kidney Disease. Please consult a doctor."
    else:
        result = "✅ You are healthy. No signs of Chronic Kidney Disease."

    return render_template('output.html', prediction_text=result)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)