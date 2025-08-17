from flask import Flask, render_template, request
from functies import *

app = Flask(__name__)

comments = read_comments_from_db("database.db")

@app.route('/')
def blog_post():
    comments = read_comments_from_db("database.db")

    return render_template('index.html', comments=comments)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form['comment']
    add_comments_to_db("database.db",[comment])

    comments = read_comments_from_db("database.db")

    return render_template('index.html', comments=comments)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)