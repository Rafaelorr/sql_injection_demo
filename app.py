from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/create_acount")
def home():
  if request.method == "POST":
    naam = request.form.get('gebruikersnaam')
    wachtwoord = request.form.get('wachtwoord')
    # voeg user toe aan database
    con = sqlite3.connect('drop.db')
    cur = con.cursor()
    cur.executescript("INSERT into users (naam,wachtwoord) VALUES(" + naam + "," + wachtwoord + ")")
    con.commit()
    try:
      cur.execute('SELECT * FROM users')
    except:
      return render_template("succes.html")
    return render_template("home.html")
  return render_template("home.html")

@app.route("/")
def hints():
  return render_template("hints.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)