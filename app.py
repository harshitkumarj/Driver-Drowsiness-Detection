from flask import Flask, request, jsonify, render_template
import main # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    return main.facial_processing()

if __name__ == '__main__':
    app.run(debug=True)