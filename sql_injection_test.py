import sqlite3

con = sqlite3.connect('dev.db')
cursor = con.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
gebruikers(id INTEGER PRIMARY KEY, naam TEXT, wachtwoord TEXT)"""

cursor.execute(command1)

# voeg sampel data toe aan database
data = (1,'test_1','test_1')
cursor.execute("INSERT INTO gebruikers VALUES(?, ?, ?)", data)
data = (2,'test_2','test_2')
cursor.execute("INSERT INTO gebruikers VALUES(?, ?, ?)", data)
data = (3,'admin','root')
cursor.execute("INSERT INTO gebruikers VALUES(?, ?, ?)", data)
data = (4,'jefke','patato')
cursor.execute("INSERT INTO gebruikers VALUES(?, ?, ?)", data)
con.commit()

cursor.execute("SELECT * FROM gebruikers")
results = cursor.fetchall()
print(results)
aanval = "'paswoord'); DROP TABLE gebruikers; --"
data = (4548888888, 'test_2',aanval)
cursor.execute("INSERT INTO gebruikers VALUES(?, ?, ?)", data)
con.commit()
# cursor.executescript("INSERT INTO gebruikers VALUES(727,'jefke', " + aanval + "}")
# con.commit()

cursor.execute("SELECT * FROM gebruikers")
results = cursor.fetchall()
print(results)

results = cursor.fetchall()
print(results)
con.close()