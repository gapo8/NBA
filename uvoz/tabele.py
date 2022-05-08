# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 


def ustvari_tabelo_igralci21_22():
    cur.execute("""
        CREATE TABLE igralci21_22 (
            igralec TEXT PRIMARY KEY UNIQUE,
            klub TEXT NOT NULL,
            starost NUMERIC NOT NULL,
            odigrane_tekme NUMERIC NOT NULL,
            zmage NUMERIC NOT NULL,
            porazi NUMERIC NOT NULL,
            minute NUMERIC NOT NULL,
            točke NUMERIC NOT NULL,
            skoki NUMERIC NOT NULL,
            podaje NUMERIC NOT NULL,
            izgubljene_žoge NUMERIC NOT NULL,
            ukradene_žoge NUMERIC NOT NULL,
            blokade NUMERIC NOT NULL,
            razlika_ob_igri NUMERIC NOT NULL
            );
    """)
    conn.commit()

def pobrisi_tabelo_igralci21_22():
    cur.execute("""
        DROP TABLE igralci21_22;
    """)
    conn.commit()

def uvozi_podatke_igralci21_22():
    with open("podatki/igralci21_22.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO igralci21_22
                (igralec,klub,starost,odigrane_tekme, zmage, porazi, minute, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

#pobrisi_tabelo_igralci21_22()
#ustvari_tabelo_igralci21_22()
#uvozi_podatke_igralci21_22()
##############################################################################################################################################

def ustvari_tabelo_igralci20_21():
    cur.execute("""
        CREATE TABLE igralci20_21 (
            igralec TEXT PRIMARY KEY UNIQUE,
            klub TEXT NOT NULL,
            starost NUMERIC NOT NULL,
            odigrane_tekme NUMERIC NOT NULL,
            zmage NUMERIC NOT NULL,
            porazi NUMERIC NOT NULL,
            minute NUMERIC NOT NULL,
            točke NUMERIC NOT NULL,
            skoki NUMERIC NOT NULL,
            podaje NUMERIC NOT NULL,
            izgubljene_žoge NUMERIC NOT NULL,
            ukradene_žoge NUMERIC NOT NULL,
            blokade NUMERIC NOT NULL,
            razlika_ob_igri NUMERIC NOT NULL
            );
    """)
    conn.commit()

def pobrisi_tabelo_igralci20_21():
    cur.execute("""
        DROP TABLE igralci20_21;
    """)
    conn.commit()

def uvozi_podatke_igralci20_21():
    with open("podatki/igralci20_21.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO igralci20_21
                (igralec,klub,starost,odigrane_tekme, zmage, porazi, minute, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

#pobrisi_tabelo_igralci20_21()
#ustvari_tabelo_igralci20_21()
#uvozi_podatke_igralci20_21()

##############################################################################################################################################

def ustvari_tabelo_igralci19_20():
    cur.execute("""
        CREATE TABLE igralci19_20 (
            igralec TEXT PRIMARY KEY UNIQUE,
            klub TEXT NOT NULL,
            starost NUMERIC NOT NULL,
            odigrane_tekme NUMERIC NOT NULL,
            zmage NUMERIC NOT NULL,
            porazi NUMERIC NOT NULL,
            minute NUMERIC NOT NULL,
            točke NUMERIC NOT NULL,
            skoki NUMERIC NOT NULL,
            podaje NUMERIC NOT NULL,
            izgubljene_žoge NUMERIC NOT NULL,
            ukradene_žoge NUMERIC NOT NULL,
            blokade NUMERIC NOT NULL,
            razlika_ob_igri NUMERIC NOT NULL
            );
    """)
    conn.commit()

def pobrisi_tabelo_igralci19_20():
    cur.execute("""
        DROP TABLE igralci19_20;
    """)
    conn.commit()

def uvozi_podatke_igralci19_20():
    with open("podatki/igralci19_20.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO igralci19_20
                (igralec,klub,starost,odigrane_tekme, zmage, porazi, minute, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

#pobrisi_tabelo_igralci19_20()
#ustvari_tabelo_igralci19_20()
uvozi_podatke_igralci19_20()

