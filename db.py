import sqlite3

conn = sqlite3.connect('_db.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS admin(login, senha)")
cur.execute("INSERT INTO admin VALUES ('admin', 'admin')")
conn.commit()


def fechar(conn):
    conn.close()

