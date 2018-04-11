import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'x'

@app.route('/')
def index():
    if 'rand' not in session:
        session['rand'] = random.randrange(0,101)
	print session['rand']
    response = "Take a guess!"
    return render_template('index.html', response=response)

@app.route('/process', methods=['POST'])
def process():
    action = request.form['action']
    print action
    if int(action) == session['rand']:
        response = "YOU WIN!"
    elif int(action) < session['rand']:
        response = "LOWER!"
    elif int(action) < session['rand']:
        response = "HIGHER!"
    return redirect('/')
app.run(debug=True)
