# uvozimo bottle.py
from bottleext import get, post, run, request, template, redirect, static_file, url, route
from bottle import template, url

# uvozimo ustrezne podatke za povezavo
import auth_public as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import os



#začetna stran 
@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

@get('/')
def index():
    cur.execute("SELECT * FROM ekipe_osnovni_podatki ORDER BY ime")
    return template('ekipe.html', ekipe_osnovni_podatki=cur)

   

@get('/prijava/')
def prijava():
    return template('prijava.html')
















######################################################################
# Glavni program
# tu bi se priklopili na bazo

# Poženemo strežnik na portu 8080, glej http://localhost:8080/
# Iz bottle dokumentacije o parametru reloader=True: Every time you edit a module file, 
# the reloader restarts the server process and loads the newest version of your code. 
conn = psycopg2.connect(database='sem2022_gasperp', host='baza.fmf.uni-lj.si', user='javnost', password='javnogeslo')
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) # onemogocimo transakcije
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
run(host='localhost', port=8080, reloader=True)

######################################################################