from flask import Flask, render_template, url_for, request, redirect, session
from pripojeni import *
import mysql.connector
import os

app = Flask(__name__)
# DŮLEŽITÉ: Bez tajného klíče nebude fungovat session (přihlášení)
app.secret_key = 'super_tajne_heslo_123' 

def get_db_connection():
    return mysql.connector.connect(
        host=HOST, user=USER, password=PASSWORD, database=DATABASE
    )

@app.route("/")
def index():
    return redirect(url_for('domu'))

@app.route("/main")
def domu():
    return render_template("index.html")

@app.route("/kontakty")
def kontakty():
    return render_template("kontakty.html")

@app.route("/mechaniky")
def mechaniky():
    return render_template("mechaniky.html")

@app.route("/o_mne")
def o_mne():
    return render_template("o_mne.html")

@app.route("/pravidla")
def pravidla():
    return render_template("pravidla.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Používáme .get(), aby to nespadlo, když klíč chybí
        name = request.form.get('jmeno')
        mail = request.form.get('email')
        psw = request.form.get('psw')

        mydb = get_db_connection()
        mycursor = mydb.cursor()

        mycursor.execute("""CREATE TABLE IF NOT EXISTS Maturita_lips_uzivatele (
            id int AUTO_INCREMENT PRIMARY KEY,
            jmeno varchar(35) NOT NULL,
            email varchar(50) NOT NULL,
            heslo varchar(255) NOT NULL
        );""")
        
        sql = "INSERT INTO Maturita_lips_uzivatele (jmeno, email, heslo) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (name, mail, psw))
        mydb.commit()
        mycursor.close()
        mydb.close()

        return redirect(url_for('login'))

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')

        mydb = get_db_connection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT heslo FROM Maturita_lips_uzivatele WHERE email = %s;", (email,))
        result = mycursor.fetchone()
        mycursor.close()
        mydb.close()

        if result:
            if password == result[0]:
                session['email'] = email
                print("PŘIHLÁŠENÍ ÚSPĚŠNÉ!") # Uvidíš v terminálu
                return redirect(url_for('domu'))
            else:
                error_message = f"Špatné heslo! Zadal jsi: '{password}', v DB je: '{result[0]}'"
        else:
            error_message = f"Uživatel s emailem {email} v databázi neexistuje."

    return render_template("login.html", error=error_message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('domu'))

@app.route('/tabulka')
def tabulka():
    if 'email' not in session:
        return redirect(url_for('login'))  # ochrana stránky

    mydb = mysql.connector.connect(
        host=HOST, user=USER, password=PASSWORD, database=DATABASE
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT jmeno, score FROM Skore_space_invaders ORDER BY score DESC LIMIT 10")
    result = mycursor.fetchall()

    return render_template("statistika.html", email=session.get('email'), items=result)

if __name__ == '__main__':
    app.run(debug=True)