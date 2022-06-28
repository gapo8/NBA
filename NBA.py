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


SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)


debug = True

skrivnost = "69253faf553e52b6416804f3f48e0da5cac1f9eefa7daa7bc9c3fda8fc663b1c"

def nastaviSporocilo(sporocilo = None):
    # global napakaSporocilo
    staro = request.get_cookie("sporocilo", secret=skrivnost)
    #if sporocilo is None:
        #response.delete_cookie('sporocilo',  secret=skrivnost)
    #else:
        #response.set_cookie('sporocilo', sporocilo,  secret=skrivnost)
    return staro 







def preveriUporabnika(): 
    uporabnisko_ime = request.get_cookie("uporabnisko_ime", secret=skrivnost)
    if uporabnisko_ime:
  #      cur = baza.cursor()    
        uporabnik = None
        try: 
            cur.execute("SELECT * FROM oseba WHERE uporabnisko_ime = %s", [uporabnisko_ime])
            uporabnik = cur.fetchone()
        except:
            uporabnik = None
        if uporabnik: 
            return uporabnik
    redirect(url=('prijava_get'))



##############################################################################################################################################
#začetna stran 
##############################################################################################################################################
@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

#pred prijavo ali registracijo
@get('/')
def index():
    return template('index.html')

#po prijavi ali registraciji
@get('/zacetna/')
def zacetna():
    return template('zacetna.html')

################################################################################################################################################
#PRIJAVA, REGISTRACIJA, ODJAVA
#################################################################################################################################################

def hashGesla(s):
    m = hashlib.sha256()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

napaka=None

@get('/registracija/')
def registracija_get():
    napaka = None
    return template('registracija.html', napaka=napaka)

@post('/registracija/')
def registracija_post():
    emso = request.forms.emso
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
        redirect(url('registracija_get'))
        return
    oseba = cur 
    uporabnik = None
    try: 
        uporabnik = cur.execute("SELECT * FROM oseba WHERE uporabnisko_ime = %s", [uporabnisko_ime])
    except:
        uporabnik = None
    if uporabnik is not None:
        return template('registracija.html',   napaka="Registracija ni možna")
    if len(geslo) < 4:
        return template('registracija.html',   napaka="Geslo mora imeti vsaj 4 znake.")
    if geslo != geslo2:
        return template('registracija.html',   napaka="Gesli se ne ujemata.")
        
    zgostitev = hashGesla(geslo)
    cur.execute("""INSERT INTO oseba
                (emso,ime,priimek,ulica, hisna_stevilka, email,telefon, uporabnisko_ime, geslo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (emso,ime,priimek,ulica, hisna_stevilka, email, telefon, uporabnisko_ime, zgostitev))
    response.set_cookie('uporabnisko_ime', uporabnisko_ime,  secret=skrivnost)
    redirect(url('zacetna'))


@get('/prijava/')
def prijava_get():
    napaka2 = None
    return template('prijava.html', napaka2=napaka2)

@post('/prijava/')
def prijava_post():
    uporabnisko_ime = request.forms.uporabnisko_ime
    geslo = request.forms.geslo
    if uporabnisko_ime is None or geslo is None:
        redirect(url('prijava_get'))
        return
    oseba = cur   
    hashBaza = None
    try: 
        hashBaza = cur.execute("SELECT geslo FROM oseba WHERE uporabnisko_ime = %s", (uporabnisko_ime, ))
        hashBaza = cur.fetchone()
        hashBaza = hashBaza[0]
    except:
        hashBaza = None
    if hashBaza is None:
        return template('prijava.html',   napaka2="Uporabniško ime ali geslo nista ustrezni")
    if hashGesla(geslo) != hashBaza:
        return template('prijava.html',   napaka2="Uporabniško ime ali geslo nista ustrezni")
    response.set_cookie('uporabnisko_ime', uporabnisko_ime, secret=skrivnost)
    redirect(url('zacetna'))
    
@get('/odjava/')
def odjava_get():
    response.delete_cookie('uporabnisko_ime')
    redirect(url('index'))



#################################################################################################################################################
#TABELE
#################################################################################################################################################


#################################################################################################################################################
#Igralci

@get('/igralci/')
def igralci_get():
    cur.execute("SELECT * FROM igralci_vsi ORDER BY igralec")
    return template('igralci.html', igralci_vsi=cur)

@get('/igralci_statistika_19_20/')
def igralci_statistika_19_20_get():
    cur.execute("SELECT igralec, klub, odigrane_tekme, minute, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri FROM igralci19_20 ORDER BY igralec")
    return template('igralci19_20.html', igralci19_20=cur)

@get('/igralci_statistika_20_21/')
def igralci_statistika_20_21_get():
    cur.execute("SELECT igralec, klub, odigrane_tekme, minute, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri FROM igralci20_21 ORDER BY igralec")
    return template('igralci20_21.html', igralci20_21=cur)

@get('/igralci_statistika_21_22/')
def igralci_statistika_21_22_get():
    cur.execute("SELECT igralec, klub, odigrane_tekme, minute, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri FROM igralci21_22 ORDER BY igralec")
    return template('igralci21_22.html', igralci21_22=cur)


#################################################################################################################################################
#Ekipe

@get('/ekipe/')
def ekipe_get():
    cur.execute("SELECT * FROM ekipe_osnovni_podatki ORDER BY ime")
    return template('ekipe.html', ekipe_osnovni_podatki=cur)


@get('/ekipe_statistika_19_20/')
def ekipe_statistika_19_20_get():
    cur.execute("SELECT ekipa, ime, odigrane_tekme, zmage, porazi, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri FROM ekipe19_20 ORDER BY ekipa")
    return template('ekipe19_20.html', ekipe19_20=cur)


@get('/ekipe_statistika_20_21/')
def ekipe_statistika_20_21_get():
    cur.execute("SELECT ekipa, ime, odigrane_tekme, zmage, porazi, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri FROM ekipe20_21 ORDER BY ekipa")
    return template('ekipe20_21.html', ekipe20_21=cur)


@get('/ekipe_statistika_21_22/')
def ekipe_statistika_21_22_get():
    cur.execute("SELECT ekipa, ime, odigrane_tekme, zmage, porazi, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri FROM ekipe21_22 ORDER BY ekipa")
    return template('ekipe21_22.html', ekipe21_22=cur)


#################################################################################################################################################
#Trenerji

@get('/trenerji/')
def trenerji_get():
    cur.execute("""
    SELECT trenerji.*, ekipe_osnovni_podatki.ime FROM trenerji 
    LEFT JOIN ekipe_osnovni_podatki ON trenerji.ekipa=ekipe_osnovni_podatki.ekipa
    ORDER BY trener""")
    return template('trenerji.html', trenerji=cur)




#################################################################################################################################################
#Lastniki

@get('/lastniki/')
def lastniki_get():
    cur.execute("SELECT * FROM lastniki ORDER BY ime_ekipe")
    return template('lastniki.html', lastniki=cur)



#################################################################################################################################################
#Sponzorji

@get('/sponzorji/')
def sponzorji_get():
    cur.execute("SELECT * FROM sponzorji ORDER BY ekipa")
    return template('sponzorji.html', sponzorji=cur)


@get('/sponzorji/dodaj/')
def dodaj_sponzorja_get():
    return template('sponzorji_dodaj.html')


@post('/sponzorji/dodaj/') 
def dodaj_sponzorja_post():
    ekipa = request.forms.ekipa
    sponzor = request.forms.sponzor
    cur.execute("INSERT INTO sponzorji (ekipa, sponzor) VALUES (%s, %s)", 
         (ekipa, sponzor))
    redirect(url('sponzorji_get'))


@get('/sponzorji/uredi/<ekipa>/<trenutni_sponzor>')
def uredi_sponzorja_get(ekipa, trenutni_sponzor):
    ekipa = ekipa
    trenutni_sponzor = trenutni_sponzor
    return template('sponzorji_uredi.html', ekipa=ekipa, trenutni_sponzor=trenutni_sponzor)


@post('/sponzorji/uredi/<ekipa>/<trenutni_sponzor>')
def uredi_sponzorja_post(ekipa, trenutni_sponzor):
    sponzor = request.forms.sponzor
    ekipa = ekipa
    trenutni_sponzor = trenutni_sponzor
    cur.execute("UPDATE sponzorji SET sponzor=%s WHERE ekipa=%s AND sponzor=%s",
                    (sponzor, ekipa, trenutni_sponzor))
    conn.commit()
    redirect(url('sponzorji_get'))


@get('/sponzorji/izbrisi/<ekipa>/<trenutni_sponzor>')
def izbrisi_sponzorja_get(ekipa, trenutni_sponzor):
    ekipa = ekipa
    trenutni_sponzor = trenutni_sponzor
    return template('sponzorji_izbrisi.html', ekipa=ekipa, trenutni_sponzor=trenutni_sponzor)

@post('/sponzorji/izbrisi/<ekipa>/<trenutni_sponzor>')
def uredi_sponzorja_post(ekipa, trenutni_sponzor):
    ekipa = ekipa
    trenutni_sponzor = trenutni_sponzor
    cur.execute("DELETE FROM sponzorji WHERE ekipa=%s AND sponzor=%s",
                    [ekipa, trenutni_sponzor])
    conn.commit()
    redirect(url('sponzorji_get'))

##########################################################################################################################################################


















######################################################################
# Glavni program
# tu bi se priklopili na bazo

# Poženemo strežnik na portu 8080, glej http://localhost:8080/
# Iz bottle dokumentacije o parametru reloader=True: Every time you edit a module file, 
# the reloader restarts the server process and loads the newest version of your code. 
conn = psycopg2.connect(database='sem2022_gasperp', host='baza.fmf.uni-lj.si', user='javnost', password='javnogeslo', port=DB_PORT)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) # onemogocimo transakcije
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
run(host='localhost', port=SERVER_PORT, reloader=RELOADER)

######################################################################