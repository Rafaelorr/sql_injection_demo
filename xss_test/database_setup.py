import sqlite3

con: sqlite3.Connection = sqlite3.connect('database.db')
cur: sqlite3.Cursor = con.cursor()

# Verwijder de comments tabel als die al bestaat
cur.execute('DROP TABLE IF EXISTS comments')

# Maak de comments tabel opnieuw aan
cur.execute('CREATE TABLE comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)')

# Voeg sample data toe
cur.execute('INSERT INTO comments (comment) VALUES ("Hallo, iedereen.")')
cur.execute('INSERT INTO comments (comment) VALUES ("Dit is een leuke blog.")')
cur.execute('INSERT INTO comments (comment) VALUES ("De beste blog ooit.")')

# Sla de veranderingen op
con.commit()

# Sluit de oorspronkelijke verbinding
cur.close()
con.close()
