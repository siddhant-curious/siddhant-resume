from flask import Flask
from flask import render_template,redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('resume.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))
