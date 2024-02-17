import sqlite3

con:sqlite3.Connection = sqlite3.connect('database.db')
cur:sqlite3.Cursor = con.cursor()

# verwijder de users table
cur.execute('DROP TABLE users')

# voeg de users table toe
cur.execute('CREATE TABLE users (id INTEGER AUTO INCREMENT PRIMARY KEY, naam TEXT, wachtwoord TEXT)')

# voeg sampel data toe
cur.execute('INSERT into users VALUES(1,"admin","root")')
cur.execute('INSERT into users VALUES(2,"test","test")')
cur.execute('INSERT into users VALUEs(3,"jeff","password123")')
cur.execute('INSERT into users VALUES(4,"john","potatoes")')
cur.execute('INSERT into users VALUES(5,"ayko","tomatoes")')

# save de veranderingen in de database
con.commit()

# close de connetion aan de database
cur.close()
con.close()