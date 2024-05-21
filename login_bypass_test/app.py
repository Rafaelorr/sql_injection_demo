from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def home():
  if request.method == "POST":
    # neem de data van het login form
    naam:str = request.form.get('gebruikersnaam')
    wachtwoord:str = request.form.get('wachtwoord')

    con:sqlite3.Connection = sqlite3.connect('database.db')
    cur:sqlite3.Cursor = con.cursor()

    # select sql statement
    cur.execute("SELECT count(*) FROM users WHERE naam="+ naam +" AND wachtwoord="+ wachtwoord+"")
    database_wachtwoord = cur.fetchone()
    database_wachtwoord = database_wachtwoord[0]

    if database_wachtwoord >= 1:
      return render_template("succes.html")
    elif database_wachtwoord < 0:
      return render_template("faal.html")

    return render_template("login.html")
  return render_template("login.html")

@app.route("/")
def hints():
  return render_template("hints.html")

# maak debug False
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)