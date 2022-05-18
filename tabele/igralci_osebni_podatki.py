# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#IGRALCI OSEBNI PODATKI
##############################################################################################################################################


def ustvari_tabelo_igralci_osebni20_21():
    cur.execute("""
        CREATE TABLE igralci_osebni20_21 (
            igralec TEXT PRIMARY KEY UNIQUE,
            klub TEXT NOT NULL,
            starost INTEGER NOT NULL,
            višina TEXT  NOT NULL,
            teža INTEGER NOT NULL,
            univerza TEXT,
            država TEXT NOT NULL,
            leto_nabora TEXT NOT NULL,
            krog_nabora TEXT NOT NULL,
            številka_nabora TEXT NOT NULL
            
            );
    """)
    conn.commit()

def pobrisi_tabelo_igralci_osebni20_21():
    cur.execute("""
        DROP TABLE igralci_osebni20_21;
    """)
    conn.commit()

def uvozi_podatke_igralci_osebni20_21():
    with open("podatki/osebni_podatki20_21.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO igralci_osebni20_21
                (igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()

def popravi_podatke_igralci_osebni20_21():
    cur.execute("""
                UPDATE igralci_osebni20_21
                SET starost = starost + 1
                """)
    conn.commit()

#pobrisi_tabelo_igralci_osebni20_21()
#ustvari_tabelo_igralci_osebni20_21()
#uvozi_podatke_igralci_osebni20_21()
#popravi_podatke_igralci_osebni20_21()
##############################################################################################################################################


def ustvari_tabelo_igralci_osebni19_20():
    cur.execute("""
        CREATE TABLE igralci_osebni19_20 (
            igralec TEXT PRIMARY KEY UNIQUE,
            klub TEXT NOT NULL,
            starost INTEGER NOT NULL,
            višina TEXT  NOT NULL,
            teža INTEGER NOT NULL,
            univerza TEXT,
            država TEXT NOT NULL,
            leto_nabora TEXT NOT NULL,
            krog_nabora TEXT NOT NULL,
            številka_nabora TEXT NOT NULL
            
            );
    """)
    conn.commit()

def pobrisi_tabelo_igralci_osebni19_20():
    cur.execute("""
        DROP TABLE igralci_osebni19_20;
    """)
    conn.commit()

def uvozi_podatke_igralci_osebni19_20():
    with open("podatki/osebni_podatki19_20.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO igralci_osebni19_20
                (igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
    conn.commit()


def popravi_podatke_igralci_osebni19_20():
    cur.execute("""
                UPDATE igralci_osebni19_20
                SET starost = starost + 2
                """)
    conn.commit()

#pobrisi_tabelo_igralci_osebni19_20()
#ustvari_tabelo_igralci_osebni19_20()
#uvozi_podatke_igralci_osebni19_20()
#popravi_podatke_igralci_osebni19_20()
##############################################################################################################################################

def ustvari_tabelo_igralci_vsi():
    cur.execute("""
        CREATE TABLE igralci_vsi (
            igralec TEXT PRIMARY KEY UNIQUE,
            klub TEXT REFERENCES ekipe_osnovni_podatki(ekipa) NOT NULL,
            starost INTEGER NOT NULL,
            višina TEXT  NOT NULL,
            teža INTEGER NOT NULL,
            univerza TEXT,
            država TEXT NOT NULL,
            leto_nabora TEXT NOT NULL,
            krog_nabora TEXT NOT NULL,
            številka_nabora TEXT NOT NULL
            
            );
    """)
    conn.commit()

def pobrisi_tabelo_igralci_vsi():
    cur.execute("""
        DROP TABLE igralci_vsi;
    """)
    conn.commit()


def uvozi_podatke_igralci_vsi():
    with open("podatki/osebni_podatki21_22.csv", encoding='utf8',errors='ignore') as f:
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            cur.execute("""
                INSERT INTO igralci_vsi
                (igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, r)
            conn.commit()



def popravi_tabelo_igralci_vsi():
    cur.execute("""
                INSERT INTO igralci_vsi
                (igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora)
                SELECT DISTINCT igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora
                FROM igralci_osebni20_21
                WHERE igralec NOT IN (SELECT igralec FROM igralci_vsi);
                """)
    conn.commit()
    cur.execute("""
                INSERT INTO igralci_vsi
                (igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora)
                SELECT DISTINCT igralec,klub,starost,višina, teža, univerza, država, leto_nabora, krog_nabora, številka_nabora
                FROM igralci_osebni19_20
                WHERE igralec NOT IN (SELECT igralec FROM igralci_vsi);
                """)
    conn.commit()

def pobrisi_stolpec_igralci_vsi():
    cur.execute("""
        ALTER TABLE igralci_vsi
        DROP COLUMN klub;
    """)
    conn.commit()



#pobrisi_tabelo_igralci_vsi()
#ustvari_tabelo_igralci_vsi()
#uvozi_podatke_igralci_vsi()
#popravi_tabelo_igralci_vsi()
pobrisi_stolpec_igralci_vsi()
#pobrisi_tabelo_igralci_osebni19_20()
#pobrisi_tabelo_igralci_osebni20_21()
#pobrisi_tabelo_igralci_osebni21_22()