from datetime import datetime
from flask import flash, redirect, url_for, request
from flask import render_template
from flask import Flask, g

app = Flask(__name__)

import os
import sqlite3

app.config.update(dict(
    SECRET_KEY = 'bardzosekretnawartosc',
    DATABASE = os.path.join(app.root_path, 'database.sqlite'),
    SITE_NAME = 'My Project Page'
))

def connect_db():
    """Nawiazywanie polaczenia z baza danych okreslona w konfiguracji"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Funkcja pomocnicza tworzaca polaczenie z baza danych"""
    if not hasattr(g, 'db'): # jezeli brak polaczenia, to je tworzymy
        g.db = connect_db()
    return g.db # zwracamy polaczenie z baza

@app.teardown_request
def close_db(error):
    """Zamykanie polaczenia z baza"""
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Glowny widok strony. Obsluguje wyswietlanie i dodawanie zadan."""

    error = None

    if request.method == 'POST':
        if len(request.form['px'])&len(request.form['py'])&len(request.form['pz'])&len(request.form['vx'])&len(request.form['vy'])&len(request.form['vz'])&len(request.form['force']) > 0:
            px = request.form['px']
            py = request.form['py']
            pz = request.form['pz']
            vx = request.form['vx']
            vy = request.form['vy']
            vz = request.form['vz']
            force = request.form['force']
            direction = request.form['direction']
            charge = request.form['charge']
            data_pub = datetime.now()
            db = get_db()
            db.execute('insert into data (px,py,pz,vx,vy,vz,force,direction,charge,data_pub) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                        [px,py,pz,vx,vy,vz,force,direction,charge,data_pub]) #upycha dodane
            db.commit() #potwierdzenie
            flash('New task added.')
            return redirect(url_for('index'))

        error = u'You cannot leave an empty cell!' # komunikat o bledzie

    db = get_db()
    cursor = db.execute('select * from data order by data_pub desc;')
    data = cursor.fetchall()
    
    return render_template('cool.html', data=data, error=error), data


if __name__ == '__main__':
    app.run(debug=True)

#http://zapodaj.net/images/26b8b6a608220.jpg
