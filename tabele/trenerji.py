# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#TRENERJI

def ustvari_tabelo_trenerji():
    cur.execute("""
        CREATE TABLE trenerji (
            trener TEXT PRIMARY KEY UNIQUE,
            ekipa TEXT REFERENCES ekipe_osnovni_podatki(ekipa),
            ime_ekipe TEXT NOT NULL,
            leta_pri_ekipi INTEGER NOT NULL,
            leta_kariere INTEGER NOT NULL,
            zmage_v_karieri INTEGER NOT NULL,
            porazi_v_karieri INTEGER NOT NULL
            
            );
    """)
    conn.commit()

def pobrisi_tabelo_trenerji():
    cur.execute("""
        DROP TABLE trenerji;
    """)
    conn.commit()

def uvozi_podatke_trenerji():
    with open("podatki/trenerji21_22.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO trenerji
                (trener, ekipa, ime_ekipe, leta_pri_ekipi, leta_kariere, zmage_v_karieri, porazi_v_karieri)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()


def spremeni_tabelo_trenerji():
    cur.execute("""
        ALTER TABLE trenerji
        DROP COLUMN ime_ekipe;
    """)
    conn.commit()






#pobrisi_tabelo_trenerji()
#ustvari_tabelo_trenerji()
#uvozi_podatke_trenerji()
#spremeni_tabelo_trenerji()
