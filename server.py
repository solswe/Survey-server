import os
from flask import Flask, render_template, request, redirect, jsonify, g, url_for, current_app
from urllib.parse import urlencode
import db


app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "GET":
        return render_template("survey.html")
    else:
        topGenre = request.form.get('genre')
        secGenre = request.form.get('secgenre')
        alltitle = request.form.get('favtitle')
        allgenre = request.form.get('favgenre')
        allrate = request.form.get('favrate')
        tastitle = request.form.get('tastitle')
        tasgenre = request.form.get('tasgenre')
        tasrate = request.form.get('tasrate')
        rectitle = request.form.get('rectitle')
        recgenre = request.form.get('recgenre')
        recrate = request.form.get('recrate')
        subscribe = request.form.get('ynstream')
        streaming = request.form.getlist('stream')

        with db.get_db_cursor(True) as cur:
            # current_app.logger.info("Adding")
            cur.execute("INSERT INTO surveyform (ts, topgenre, secgenre, alltimetitle, alltimegenre, alltimerate, tastetitle, tastegenre, tasterate, rectitle, recgenre, recrate, subscribe, services) values (current_timestamp, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (topGenre, secGenre, alltitle, allgenre, allrate, tastitle, tasgenre, tasrate, rectitle, recgenre, recrate, subscribe, streaming,))
        return redirect(url_for("thanks"))

@app.route("/decline")
def decline():
    return render_template("bye.html")

@app.route("/thanks")
def thanks():
    return render_template("thanku.html")

@app.route("/api/results")
def allRes():
    rev = request.args.get("reverse")
    
    with db.get_db_cursor(True) as cur:
        cur.execute("SELECT row_to_json(surveyform) FROM surveyform;")
        rows = [response for response in cur]

    if rev == "true":
        rows.reverse()

    return jsonify(rows)

@app.route("/admin/summary")
def summary():
    with db.get_db_cursor(True) as cur:
        cur.execute("SELECT alltimetitle, alltimegenre FROM surveyform;")
        allrows = [response for response in cur]
        cur.execute("SELECT rectitle, recgenre FROM surveyform;")
        recrows = [response for response in cur]
        cur.execute("SELECT tastetitle, tastegenre FROM surveyform;")
        tasterows = [response for response in cur]
    return render_template("summary.html", allrows = allrows, recrows = recrows, tasterows=tasterows)

if __name__ == '__main__':
  app.run(debug=True)