-- 1. Tabulka pro uživatele
CREATE TABLE uzivatele (
    id_uzivatele INT AUTO_INCREMENT PRIMARY KEY,
    uzivatelske_jmeno VARCHAR(50) NOT NULL UNIQUE,
    heslo VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

-- 2. Tabulka pro obtížnost hry (1:N k tabulce skore)
CREATE TABLE obtiznost (
    id_obtiznosti INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(50) NOT NULL
);

-- 3. Tabulka pro skóre (1:N vztah k uživatelům i obtížnosti)
CREATE TABLE skore (
    id_skore INT AUTO_INCREMENT PRIMARY KEY,
    id_uzivatele INT NOT NULL,
    id_obtiznosti INT NOT NULL,
    body INT NOT NULL,
    datum DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_uzivatele) REFERENCES uzivatele(id_uzivatele) ON DELETE CASCADE,
    FOREIGN KEY (id_obtiznosti) REFERENCES obtiznost(id_obtiznosti)
);

-- 4. Tabulka pro úspěchy/medaile (Pro M:N vztah s uživateli)
CREATE TABLE achivementy (
    id_achievementu INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(100) NOT NULL,
    popis TEXT
);

-- 5. Propojovací tabulka pro M:N vztah (Uživatelé <-> Úspěchy)
CREATE TABLE uzivatel_achievement (
    id_uzivatel_achievement INT AUTO_INCREMENT PRIMARY KEY,
    id_uzivatele INT NOT NULL,
    id_achievementu INT NOT NULL,
    datum_ziskani DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_uzivatele) REFERENCES uzivatele(id_uzivatele) ON DELETE CASCADE,
    FOREIGN KEY (id_achievementu) REFERENCES achivementy(id_achievementu) ON DELETE CASCADE
);