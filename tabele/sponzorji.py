# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#SPONZORJI

def ustvari_tabelo_sponzorji():
    cur.execute("""
        CREATE TABLE sponzorji (
            ekipa TEXT,
            sponzor TEXT NOT NULL    
            );
    """)
    conn.commit()

def pobrisi_tabelo_sponzorji():
    cur.execute("""
        DROP TABLE sponzorji;
    """)
    conn.commit()

def uvozi_podatke_sponzorji():
    with open("podatki/sponzorji.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO sponzorji
                (ekipa, sponzor)
                VALUES (%s, %s)
                """, r)
    conn.commit()

pobrisi_tabelo_sponzorji()
ustvari_tabelo_sponzorji()
uvozi_podatke_sponzorji()