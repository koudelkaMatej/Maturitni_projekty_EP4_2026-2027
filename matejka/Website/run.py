
# vytvoreni instance a import knihovny
from flask import Flask, render_template

app = Flask(__name__)


#zatím skore jen jako mock data, pozdeji budou z databaze
MOCK_SCORES = [
    ("Jonas", 2500, 2),
    ("Frajet_co_umi_hrat", 1850, 1)
]

#dropdown s vice info
MOCK_ALL_SCORES = {
    "Jonas": [(2500, "24.10.2026 14:30"), (1900, "22.10.2026 10:15")],
    "Frajet_co_umi_hrat": [(1850, "23.10.2026 16:45")] 
}

#domovska stranka
@app.route('/')
def home():
    """Hlavní domovská stránka (Home)."""
    return render_template("indexhome.html")

#registrace
@app.route('/register')
def register():
    """Zobrazí pouze registrační formulář (zatím nic z databáze)."""
    return render_template("register.html", error=None)

#prihlaseni
@app.route('/login')
def login():
    """Zobrazí pouze přihlašovací formulář (zatím nic z databáze)."""
    return render_template("login.html", error=None)

#pri odhlaseni presmerovani nan home
@app.route('/logout')
def logout():
    """Přesměruje rovnou na domovskou stránku."""
    return render_template("indexhome.html")

#tabulka vysledku, zatim s mock daty
@app.route('/leaderboard')
def leaderboard():
    """Zobrazí žebříček výsledků se statickými daty."""
    return render_template(
        "leaderboard.html", 
        scores=MOCK_SCORES, 
        all_scores=MOCK_ALL_SCORES, 
        error=None
    )

#stranka o hre
@app.route('/about')
def about():
    """Stránka O hře."""
    return render_template("about.html")

#kontakty
@app.route('/contact')
def contact():
    """Stránka Kontakty."""
    return render_template("contact.html")

#spusteni webu a debugovani - automaticky restartuje pri zemmne kodu a ukazuje chyby rovnou v prohlizeci
if __name__ == '__main__':
    app.run(debug=True)