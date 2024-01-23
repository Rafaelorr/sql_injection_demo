import sqlite3

con = sqlite3.connect('drop.db')
cur = con.cursor()

cur.execute('DROP TABLE users')
con.commit()

# voeg sampel data toe
cur.execute('CREATE TABLE users (id INTEGER AUTO INCREMENT PRIMARY KEY, naam TEXT, wachtwoord TEXT)')
con.commit()

cur.execute('INSERT into users VALUES(1,"admin","root")')
con.commit()

cur.execute('INSERT into users VALUES(2,"test","test")')
con.commit()

cur.execute('INSERT into users VALUEs(3,"jeff","password123")')
con.commit()

cur.execute('INSERT into users VALUES(4,"john","potatoes")')
con.commit()

cur.execute('INSERT into users VALUES(5,"ayko","tomatoes")')
con.commit()

cur.close()
con.close()