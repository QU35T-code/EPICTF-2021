#!/usr/bin/env python3

import sys
from flask import Flask, request, render_template, session
from flask_mysqldb import MySQL
from random import randint

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Temporaire - A changer en localhost au déploiement
app.config["MYSQL_HOST"] = '144.91.117.247'
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 's3cr3tpa55w0rdacc355databa53'
app.config["MYSQL_DB"] = "pokestore"

mysql = MySQL(app)

challName = 'PokeStore V1'
app.secret_key = '5up3rSecretWh1chNo0n3W1llB34bl3ToBruteF0rc3'


def new_token():
    # antisqlmap
    newtoken = str(randint(0, 1000000000))
    if 'tokens' not in session:
        session['tokens'] = [newtoken]
    else:
        tokens = session['tokens']
        # each tokens can be use 10 times
        for _ in range(10):
            tokens.append(newtoken)
        session['tokens'] = tokens
    while (len(session['tokens']) > 50):
        session['tokens'].pop(0)
    return newtoken


def check_token(token):
    # check if token is valid
    if token not in session['tokens']:
        return False
    for i in range(len(session['tokens'])):
        if session['tokens'][i] == token:
            session['tokens'].pop(i)
            return True
    return False


@app.route('/')
def start():
    newtoken = new_token()

    search = ""
    if request.args.get('token') and request.args.get('search'):
        token = str(request.args.get('token'))
        search = request.args.get('search')

        if check_token(token) is False:
            return 'Invalid token'

        sql = f"SELECT * FROM shop WHERE name LIKE '%{search}%'"
    elif request.args.get('min') or request.args.get('max') or request.args.get('type'):
        return 'Not implemented'
    else:
        sql = "SELECT * FROM shop;"

    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', challName=challName, shop=data, token=newtoken, search=search)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9327)

