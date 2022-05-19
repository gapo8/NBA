# uvozimo ustrezne podatke za povezavo
import auth as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki



conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

##################################################################################################################################################
#PRAVICE


def podeli_pravice():
    cur.execute("""
        GRANT ALL ON DATABASE sem2022_gasperp TO tinema WITH GRANT OPTION;
        GRANT ALL ON SCHEMA public TO tinema WITH GRANT OPTION;
        GRANT CONNECT ON DATABASE sem2022_gasperp TO javnost;
        GRANT USAGE ON SCHEMA public TO javnost;
        GRANT ALL ON ALL TABLES IN SCHEMA public TO tinema WITH GRANT OPTION;
        GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO tinema WITH GRANT OPTION;
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO javnost WITH GRANT OPTION;
    """)
    conn.commit()


podeli_pravice()