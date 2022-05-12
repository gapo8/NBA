# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#LASTNIKI

def ustvari_tabelo_lastniki():
    cur.execute("""
        CREATE TABLE lastniki (
            ekipa TEXT PRIMARY KEY UNIQUE,
            ime_ekipe TEXT NOT NULL,
            lastniki TEXT NOT NULL,
            upravljalska_entiteta TEXT NOT NULL,
            nakupna_cena TEXT NOT NULL,
            leto_nakupa INTEGER NOT NULL
            
            );
    """)
    conn.commit()

def pobrisi_tabelo_lastniki():
    cur.execute("""
        DROP TABLE lastniki;
    """)
    conn.commit()

def uvozi_podatke_lastniki():
    with open("podatki/lastniki.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO lastniki
                (ekipa, ime_ekipe, lastniki, upravljalska_entiteta, nakupna_cena, leto_nakupa)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

pobrisi_tabelo_lastniki()
ustvari_tabelo_lastniki()
uvozi_podatke_lastniki()