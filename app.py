from flask import Flask, render_template, flash
from form_wtf import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    name = None
    form = SampleForm()
    # Validate form submission
    if form.validate_on_submit():
        name = form.username.data
        form.username.data = ''
        flash('Form submitted successfully!')
    return render_template('form.html', name=name, form=form)

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

if __name__ == '__main__':
    app.run(debug=True)