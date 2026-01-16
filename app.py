import os
from flask import Flask, render_template, flash
from form_wtf import *

app = Flask(__name__)

# Generate a secure secret key from environment or use a default for development
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

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

# Error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)