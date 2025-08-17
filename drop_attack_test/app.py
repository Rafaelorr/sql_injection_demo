from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/create_acount",methods=["GET","POST"])
def home():
  if request.method == "POST":
    naam:str = request.form.get('gebruikersnaam')
    wachtwoord:str = request.form.get('wachtwoord')

    # voeg user toe aan database
    con:sqlite3.Connection = sqlite3.connect('database.db')
    cur:sqlite3.Cursor = con.cursor()

    cur.execute(f"INSERT into users (naam,wachtwoord) VALUES('{naam}','{wachtwoord}')")
    con.commit()

    cur.execute('SELECT * FROM users')
    res = cur.fetchall()

    if res:
      cur.execute('SELECT * FROM users')
      return render_template('faal.html')

    elif res == None:
      return render_template("succes.html")

    else:
      return render_template("home.html")

  return render_template("home.html")

@app.route("/")
def hints():
  return render_template("hints.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=False)