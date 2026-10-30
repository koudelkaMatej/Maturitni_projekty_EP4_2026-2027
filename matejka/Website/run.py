from flask import Flask, render_template

app = Flask(__name__)

MOCK_SCORES = [
    ("Jonas", 2500, 2),
    ("Frajet_co_umi_hrat", 1850, 1) #zatim jen pro ukazani
]

MOCK_ALL_SCORES = {
    "Jonas": [(2500, "24.10.2026 14:30"), (1900, "22.10.2026 10:15")],
    "Frajet_co_umi_hrat": [(1850, "23.10.2026 16:45")] #dropdown menu, rovnez bude upraveno
}


@app.route('/')
def home():
    """Hlavní domovská stránka (Home)."""
    return render_template("indexhome.html")


@app.route('/register')
def register():
    """Zobrazí pouze registrační formulář (zatím nic nezpracovává)."""
    return render_template("register.html", error=None)


@app.route('/login')
def login():
    """Zobrazí pouze přihlašovací formulář (zatím nic nezpracovává)."""
    return render_template("login.html", error=None)


@app.route('/logout')
def logout():
    """Přesměruje rovnou na domovskou stránku."""
    return render_template("indexhome.html")


@app.route('/leaderboard')
def leaderboard():
    """Zobrazí žebříček výsledků se statickými daty."""
    return render_template(
        "leaderboard.html", 
        scores=MOCK_SCORES, 
        all_scores=MOCK_ALL_SCORES, 
        error=None
    )


@app.route('/about')
def about():
    """Stránka O hře."""
    return render_template("about.html")


@app.route('/contact')
def contact():
    """Stránka Kontakty."""
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)