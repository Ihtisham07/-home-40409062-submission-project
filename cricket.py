from flask import Flask, url_for, render_template, request, flash, redirect

import sqlite3

conn = sqlite3.connect('users1.db')
print "Opened database successfully";

print "Table created successfully";
conn.close()


app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/livescore")
def livescore():
    return render_template("livescore.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/raheel")
def raheel():
    return render_template("raheel.html")

@app.route('/login/', methods=["GET","POST"])
def login_page():

    error = ''
    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            with sql.connect("users1.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (uid, username, password, email, settings) VALUES(?,?,?,?,?)",(uid, username, password, email, settings))
                con.commit()
                msg = "Inserted Successfully"
            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))

            else:
                error = "Invalid Username/Password. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
            #flash(e)
        return render_template( "login.html", error = error )

@app.route('/register', methods=["GET","POST"])
def register_page():
    try:
        c, conn = connection()
        retun ("OKAY")
    except Exception as e:
        return(str(e))

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/teams")
def teams():
    return render_template("teams.html")

@app.route("/tournaments")
def tournaments():
    return render_template("tournaments.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html")


if __name__ == "__main__":
    app.run(debug=True)
