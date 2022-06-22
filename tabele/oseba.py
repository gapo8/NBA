# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#OSEBE

def ustvari_tabelo_oseba():
    cur.execute("""
        CREATE TABLE oseba (
            emso TEXT PRIMARY KEY,
            ime TEXT NOT NULL,
            priimek TEXT NOT NULL,
            ulica TEXT NOT NULL,
            hisna_stevilka INTEGER NOT NULL,
            email TEXT NOT NULL unique,
            telefon TEXT NOT NULL,
            uporabnisko_ime TEXT UNIQUE,
            geslo TEXT
            
            
            );
    """)
    conn.commit()


def pobrisi_tabelo_oseba():
    cur.execute("""
        DROP TABLE oseba;
    """)
    conn.commit()


pobrisi_tabelo_oseba()
ustvari_tabelo_oseba()