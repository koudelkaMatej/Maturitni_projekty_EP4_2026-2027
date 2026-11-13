# 1. fáze projektu – Icy Tower 2.0

## 1. Cíl projektu
Vytvoření desktopové hry v Pygame propojené s relační databází MySQL/MariaDB a webovou prezentací (HTML/CSS) obsahující žebříček hráčů a uživatelskou sekci.

## 2. Datové toky
- **Hra -> Databáze:** Po skončení hry se přes SQL příkaz `INSERT` odešle dosažené skóre, ID hráče a ID obtížnosti do tabulky `skore`.
- **Databáze -> Web:** Webová stránka `vysledky.html` načítá data z databáze pomocí SQL dotazu `SELECT` s využitím `JOIN`, čímž dynamicky zobrazuje žebříček nejlepších hráčů.
- **Web -> Databáze:** Registrace a přihlášení uživatelů zapisuje a ověřuje data v tabulce `uzivatele`.

## 3. Návrh databáze a ER diagram
Databáze je normalizovaná a obsahuje následující tabulky:
- `uzivatele` (id_uzivatele, uzivatelske_jmeno, heslo, email)
- `obtiznost` (id_obtiznosti, nazev)
- `skore` (id_skore, id_uzivatele, id_obtiznosti, body, datum)
- `achivementy` (id_achievementu, nazev, popis)
- `uzivatel_achievement` (id_uzivatel_achievement, id_uzivatele, id_achievementu, datum_ziskani)

**Vazby v databázi:**
- `uzivatele` (1) $\rightarrow$ (N) `skore`
- `obtiznost` (1) $\rightarrow$ (N) `skore`
- `uzivatele` $\leftrightarrow$ `achivementy` (vazba M:N přes propojovací tabulku `uzivatel_achievement`)

## 4. Stav implementace (1. fáze)
- **Hra:** Zprovozněné hlavní menu v Pygame, spuštění a ukončení aplikace, vyřešené vykreslování textů a pozadí.
- **Web:** Vytvořená struktura HTML stránek ve složce `web/` (`index.html`, `o-autorovi.html`, `pravidla.html`, `vysledky.html`) a jednotný `style.css`.
- **Databáze:** Připravené kompletní DDL skripty v souboru `database.sql`.
- **Git:** Založený repozitář s průběžnými commity.