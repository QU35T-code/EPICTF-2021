#encoding=utf8
#EPICTF{lfi_ar3_3a5y_t0_expl01t}

import sys
from flask import Flask, request, url_for, render_template, redirect

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def start():
    return render_template('index.html')


@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    if filename == "":
        filename = "list/default.txt"
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)

if __name__ == "__main__":
    app.run("0.0.0.0")
