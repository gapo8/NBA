# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#EKIPE OSNOVNI PODATKI

def ustvari_tabelo_ekipe_osnovni_podatki():
    cur.execute("""
        CREATE TABLE ekipe_osnovni_podatki (
            ekipa TEXT PRIMARY KEY UNIQUE,
            ime TEXT NOT NULL,
            lokacija TEXT NOT NULL,
            dvorana TEXT NOT NULL,
            kapaciteta TEXT NOT NULL,
            ustanovitev INTEGER NOT NULL,
            konferenca TEXT NOT NULL,
            divizija TEXT NOT NULL
            
            );
    """)
    conn.commit()

def pobrisi_tabelo_ekipe_osnovni_podatki():
    cur.execute("""
        DROP TABLE ekipe_osnovni_podatki CASCADE;
    """)
    conn.commit()

def uvozi_podatke_ekipe_osnovni_podatki():
    with open("podatki/ekipe_osnovni_podatki.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO ekipe_osnovni_podatki
                (ekipa, ime, lokacija, dvorana, kapaciteta, ustanovitev, konferenca, divizija)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

#pobrisi_tabelo_ekipe_osnovni_podatki()
#ustvari_tabelo_ekipe_osnovni_podatki()
uvozi_podatke_ekipe_osnovni_podatki()