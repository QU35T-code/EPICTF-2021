#encoding=utf8
#VFdWdGJ5QTZDaTBnUVdwdmRYUmxjaUJrWlNCdWIzVjJaV0YxZUNCaGJtbHQ2WE11Q2kwZ1Z1bHlhV1pwWlhJZ2JHVnpJRzFwYzJWeklPQWdhbTkxY2lCa2RTQnphWFJsTGdvdElGSmxaMkZ5WkdWeUlHeGxjeUJ6ZEdGMGFYTjBhWEYxWlhNZ1pHVWdkbWx6YVhSbGN5NEtMU0JCYW05MWRHVnlJSFZ1WlNCd2NtOTBaV04wYVc5dUlFUkVUMU11Q2kwZ1JWQkpRMVJHZTJ4bWFWOWpRVzVmWWpOZlpFRnVNM0l3ZFRWOQ==

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
    app.run(host="0.0.0.0", port=4837)
