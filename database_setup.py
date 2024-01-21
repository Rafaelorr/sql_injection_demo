import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('CREATE TABLE users VALUES(id INTEGER AUTO INCREMENT PRIMARY KEY, naam TEXT, wachtwoord TEXT)')
con.commit()

cur.close()
con.close()
