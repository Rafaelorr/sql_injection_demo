from flask import Flask,render_template,request
import sqlite3

def query_to_string(result:list) -> str:
  result = result[0]
  result = result[1]
  result = str(result)
  return result

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def home():
  if request.method == "POST":
    # neem de data van het login form
    naam = request.form.get('gebruikersnaam')
    wachtwoord = request.form.get('wachtwoord')

    con = sqlite3.connect('/login_bypass_test/database.db')
    cur = con.cursor()

    # select sql statement
    cur.execute("SELECT wachtwoord FROM gebruikers WHERE naam=" + naam +"")
    database_wachtwoord = cur.fetchone()
    database_wachtwoord = query_to_string(database_wachtwoord)

    if wachtwoord == database_wachtwoord:
      return render_template("succes.html")
    elif wachtwoord != database_wachtwoord:
      return render_template("faal.html")

    return render_template("login.html")
  return render_template("login.html")

@app.route("/")
def hints():
  return render_template("hints.html")

# maak debug False
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)