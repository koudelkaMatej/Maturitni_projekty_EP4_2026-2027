# Přehled architektury a rizik

## Struktura kódu
- `Dinosaur`: Třída spravující polohu, skoky a gravitaci postavy.
- `Obstacle`: Generátor zemských překážek s náhodným odstupem.
- `Meteor`: Entita asynchronní pasti padající z vrchní části obrazovky.
- `check_db_traps()`: Funkce provádějící neblokující SQL dotazy do SQLite databáze.

## Datové toky
1. **Web -> DB:** PHP odesílá příkaz `INSERT INTO global_traps` po kliknutí uživatele.
2. **DB -> Hra:** Python každou sekundu volá `SELECT` a zjišťuje přítomnost řádků. Následně provádí `UPDATE` na příznak přečtení.
3. **Hra -> DB:** Po detekci kolize Python zapíše finální skóre pomocí `INSERT INTO games`.

## Rizika a mitigace
- **Riziko: Zamrzání hry při čtení DB.** Pokud by byla databáze přetížená, herní smyčka by čekala na odpověď.
- **Mitigace:** Databázový dotaz je optimalizovaný, provádí se na lokálním odlehčeném souboru SQLite a spouští se pouze jednou za 60 snímků, nikoliv v každém framu.
