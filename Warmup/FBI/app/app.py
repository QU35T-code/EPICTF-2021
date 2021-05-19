#encoding=utf8
import sys
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def start():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4657)
