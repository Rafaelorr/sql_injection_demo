from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def home():
  if request.method == "POST":
    # neem de data van het login form
    naam = request.form.get('gebruikersnaam')
    wachtwoord = request.form.get('wachtwoord')

    # voeg user toe aan database
    con = sqlite3.connect('/login_bypass_test/database.db')
    cur = con.cursor()

    # select sql statement
    cur.execute()
    # check dat gebruiker wachtwoord == database wachtwoord
     # als ze gelijk zijn aan elkaar dan return render_template("succes.html")
     # als ze niet gelijk zijn aan elkaar dan return render_template("faal.html")

    return render_template("login.html")
  return render_template("login.html")

@app.route("/")
def hints():
  return render_template("hints.html")

# maak debug False
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)