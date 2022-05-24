# uvozimo bottle.py
from bottleext import get, post, run, request, template, redirect, static_file, url, route
from bottle import template, url
from bottleext import *
# uvozimo ustrezne podatke za povezavo
import auth_public as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import os
import hashlib


skrivnost = "69253faf553e52b6416804f3f48e0da5cac1f9eefa7daa7bc9c3fda8fc663b1c"

def nastaviSporocilo(sporocilo = None):
    # global napakaSporocilo
    staro = request.get_cookie("sporocilo", secret=skrivnost)
#    if sporocilo is None:
#        bottle.Response.delete_cookie(key='sporocilo', path='/', secret=skrivnost)
#    else:
#        bottle.Response.set_cookie(key='sporocilo', value=sporocilo, path="/", secret=skrivnost)
    return staro 




def preveriUporabnika(): 
    uporabnisko_ime = request.get_cookie("uporabnisko_ime", secret=skrivnost)
    if uporabnisko_ime:
       # cur = baza.cursor()    
        uporabnik = None
        try: 
            cur.execute("SELECT * FROM oseba WHERE uporabnisko_ime = %s", [uporabnisko_ime])
            uporabnik = cur.fetchone()
        except:
            uporabnik = None
        if uporabnik: 
            return uporabnik
    redirect('/prijava/')



##############################################################################################################################################
#začetna stran 
##############################################################################################################################################
@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

@get('/')
def index():
    return template('index.html')

################################################################################################################################################
#PRIJAVA, REGISTRACIJA, ODJAVA
#################################################################################################################################################

def hashGesla(s):
    m = hashlib.sha256()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

@get('/registracija/')
def registracija_get():
    napaka = nastaviSporocilo()
    return template('registracija.html', napaka=napaka)

@post('/registracija/')
def registracija_post():
    id = request.forms.id
    ime = request.forms.ime
    priimek = request.forms.priimek
    ulica = request.forms.ulica
    hisna_stevilka = request.forms.hisna_stevilka
    email = request.forms.email
    telefon = request.forms.telefon
    uporabnisko_ime = request.forms.uporabnisko_ime
    geslo = request.forms.geslo
    geslo2 = request.forms.geslo2
    if uporabnisko_ime is None or geslo is None or geslo2 is None:
        nastaviSporocilo('Registracija ni možna') 
        redirect('/registracija/')
        return
    oseba = cur 
    uporabnik = None
    try: 
        uporabnik = cur.execute("SELECT * FROM oseba WHERE uporabnisko_ime = %s", [uporabnisko_ime])
    except:
        uporabnik = None
    if uporabnik is not None:
        nastaviSporocilo('Registracija ni možna') 
        redirect('/registracija/')
        return
    if len(geslo) < 4:
        nastaviSporocilo('Geslo mora imeti vsaj 4 znake.') 
        redirect('/registracija/')
        return
    if geslo != geslo2:
        nastaviSporocilo('Gesli se ne ujemata.') 
        redirect('/registracija/')
        return
    zgostitev = hashGesla(geslo)
    cur.execute("""INSERT INTO oseba
                (id,ime,priimek,ulica, hisna_stevilka, email,telefon, uporabnisko_ime, geslo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (id,ime,priimek,ulica, hisna_stevilka, email, telefon, uporabnisko_ime, zgostitev))
    bottle.Response.set_cookie(key='uporabnisko_ime', value=uporabnisko_ime, path='/', secret=skrivnost)
    redirect('/osebe/')


@get('/prijava/')
def prijava_get():
    return template('prijava.html')

@post('/prijava/')
def prijava_post():
    uporabnisko_ime = request.forms.uporabnisko_ime
    geslo = request.forms.geslo
    if uporabnisko_ime is None or geslo is None:
        nastaviSporocilo('Uporabniško ima in geslo morata biti neprazna') 
        redirect('/prijava/')
        return
    oseba = cur   
    hashBaza = None
    try: 
        hashBaza = cur.execute("SELECT geslo FROM oseba WHERE uporabnisko_ime = %s", [uporabnisko_ime])
        hashBaza = hashBaza[0]
    except:
        hashBaza = None
    if hashBaza is None:
        nastaviSporocilo('Uporabniško geslo ali ime nista ustrezni') 
        redirect('/prijava/')
        return
    if hashGesla(geslo) != hashBaza:
        nastaviSporocilo('Uporabniško geslo ali ime nista ustrezni') 
        redirect('/prijava/')
        return
    bottle.Response.set_cookie(key='uporabnisko_ime', value=uporabnisko_ime, secret=skrivnost)
    redirect('/igralci/')
    
@get('/odjava/')
def odjava_get():
    bottle.Response.delete_cookie(key='uporabnisko_ime')
    redirect('/prijava/')



#################################################################################################################################################
#TABELE
#################################################################################################################################################
@get('/igralci/')
def igralci_get():
    cur.execute("SELECT * FROM igralci_vsi ORDER BY igralec")
    return template('igralci.html', igralci_vsi=cur)


@get('/ekipe/')
def ekipe_get():
    cur.execute("SELECT * FROM ekipe_osnovni_podatki ORDER BY ime")
    return template('ekipe.html', ekipe_osnovni_podatki=cur)


@get('/osebe/')
def osebe_get():
    cur.execute("SELECT * FROM oseba ORDER BY id")
    return template('osebe.html', oseba=cur)

















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