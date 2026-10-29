# Technická dokumentace projektu

## Účel projektu
Účelem tohoto maturitního projektu je vytvoření modifikované síťové podoby klasické arkády Dino Run, která v reálném čase asynchronně komunikuje přes databázový most SQLite s webovou aplikací.

## Použité technologie
- **Hra:** Python 3.x, framework Pygame 2.x
- **Web:** PHP 8.x (čisté procedurální skripty bez externích frameworků), HTML5, CSS3
- **Databáze:** SQLite 3 (zajišťuje nulové nároky na konfiguraci serveru ve školní učebně VT6)
- **Verzování:** Git

## Struktura projektu
- `/databaze` - SQL inicializační schémata a DML data.
- `/docs` - Uživatelské a technické textové podklady.
- `/src` - Zdrojové kódy hry v Pythonu a jednotkové testy.
- `/web` - Webové rozhraní a stylové šablony.

## Spuštění a závislosti
1. V terminálu nainstalujte závislost hry: `pip install pygame`
2. Spusťte hru: `python src/main.py`
3. Pro spuštění webu v učebně VT6 využijte integrovaný PHP server příkazem: `php -S localhost:8000 -t web/` a otevřete prohlížeč na adrese `http://localhost:8000`
