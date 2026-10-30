-- -------------------------------- 
-- databazove schema, zatim neni pripojeno pred mysql connnector, bude pripojeno v dalsi fazi odevzdavani.
-- ---------------------------------------- 
-- Vytvoreni databaze pokud neexistuje, pouziti teto databaze
CREATE DATABASE IF NOT EXISTS maturitni_projekt_db;
USE maturitni_projekt_db;


-- 1. TAB: uzivatel
-- Uchovava prihlasovaci udaje pri registraci.
CREATE TABLE IF NOT EXISTS uzivatel (
    id_uzivatele INT AUTO_INCREMENT PRIMARY KEY,
    uzivatelske_jmeno VARCHAR(50) NOT NULL UNIQUE,
    heslo_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    datum_registrace DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- 2. TAB: hra_relace
-- zaznam jednotlivych her 1:N s tabulkou uzivatel, kazda hra je spojena s jednim uzavtelem
CREATE TABLE IF NOT EXISTS hra_relace (
    id_relace INT AUTO_INCREMENT PRIMARY KEY,
    id_uzivatele INT NOT NULL,
    dosazene_skore INT NOT NULL DEFAULT 0,
    datum_odehrani DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_uzivatele) REFERENCES uzivatel(id_uzivatele) ON DELETE CASCADE
);


-- 3. TABU: uspech
-- uspechy - pr nejake skorePhighscore
CREATE TABLE IF NOT EXISTS uspech (
    id_uspechu INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(100) NOT NULL UNIQUE,
    potrebne_skore INT NOT NULL
);

-- 4. TAB: dokonceny_uspech
-- tabulka pro vztah M:N uzivatel - uspech
CREATE TABLE IF NOT EXISTS dokonceny_uspech (
    id_uzivatele INT NOT NULL,
    id_uspechu INT NOT NULL,
    datum_ziskani DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_uzivatele, id_uspechu),
    FOREIGN KEY (id_uzivatele) REFERENCES uzivatel(id_uzivatele) ON DELETE CASCADE,
    FOREIGN KEY (id_uspechu) REFERENCES uspech(id_uspechu) ON DELETE CASCADE
);