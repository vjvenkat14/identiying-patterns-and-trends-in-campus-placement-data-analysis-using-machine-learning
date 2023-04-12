import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

with open('Placement_knn.pkl', 'rb') as f:
    data = pickle.load(f)


@app.route('/')
def entry():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/getdata', methods=['post'])
def submit():
    age = request.form['age']
    gender = request.form['gender']
    stream = request.form['stream']
    internships = request.form['internships']
    cgpa = request.form['cgpa']
    hostel = request.form['hostel']
    historyofbacklogs = request.form['historyofbacklogs']
    variables = [[int(age), int(gender), int(stream), int(internships), int(cgpa), int(hostel), int(historyofbacklogs)]]
    result = data.predict(variables)
    result.astype(int)
    if result == 0:
        output = 'Not Placed'
    else:
        output = 'Placed'
    return render_template('submit.html', output=output)


if __name__ == "__main__":
    app.run(debug=True)
