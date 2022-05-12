# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##############################################################################################################################################
#EKIPE


def ustvari_tabelo_ekipe21_22():
    cur.execute("""
        CREATE TABLE ekipe21_22 (
            ekipa TEXT REFERENCES ekipe_osnovni_podatki(ekipa),
            ime TEXT NOT NULL,
            odigrane_tekme INTEGER NOT NULL,
            zmage INTEGER  NOT NULL,
            porazi INTEGER  NOT NULL,
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


def pobrisi_tabelo_ekipe21_22():
    cur.execute("""
        DROP TABLE ekipe21_22;
    """)
    conn.commit()


def uvozi_podatke_ekipe21_22():
    with open("podatki/ekipe21_22.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO ekipe21_22
                (ekipa,ime,odigrane_tekme, zmage, porazi, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

pobrisi_tabelo_ekipe21_22()
ustvari_tabelo_ekipe21_22()
uvozi_podatke_ekipe21_22()

######################################################################################################################################################


def ustvari_tabelo_ekipe20_21():
    cur.execute("""
        CREATE TABLE ekipe20_21 (
            ekipa TEXT REFERENCES ekipe_osnovni_podatki(ekipa),
            ime TEXT NOT NULL,
            odigrane_tekme INTEGER NOT NULL,
            zmage INTEGER NOT NULL,
            porazi INTEGER NOT NULL,
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


def pobrisi_tabelo_ekipe20_21():
    cur.execute("""
        DROP TABLE ekipe20_21;
    """)
    conn.commit()


def uvozi_podatke_ekipe20_21():
    with open("podatki/ekipe20_21.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO ekipe20_21
                (ekipa,ime,odigrane_tekme, zmage, porazi, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

pobrisi_tabelo_ekipe20_21()
ustvari_tabelo_ekipe20_21()
uvozi_podatke_ekipe20_21()

######################################################################################################################################################

def ustvari_tabelo_ekipe19_20():
    cur.execute("""
        CREATE TABLE ekipe19_20 (
            ekipa TEXT REFERENCES ekipe_osnovni_podatki(ekipa),
            ime TEXT NOT NULL,
            odigrane_tekme INTEGER NOT NULL,
            zmage INTEGER NOT NULL,
            porazi INTEGER NOT NULL,
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


def pobrisi_tabelo_ekipe19_20():
    cur.execute("""
        DROP TABLE ekipe19_20;
    """)
    conn.commit()


def uvozi_podatke_ekipe19_20():
    with open("podatki/ekipe19_20.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO ekipe19_20
                (ekipa,ime,odigrane_tekme, zmage, porazi, točke, skoki, podaje, izgubljene_žoge, ukradene_žoge, blokade, razlika_ob_igri)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

pobrisi_tabelo_ekipe19_20()
ustvari_tabelo_ekipe19_20()
uvozi_podatke_ekipe19_20()
