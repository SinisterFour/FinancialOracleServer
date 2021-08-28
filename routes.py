from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')
