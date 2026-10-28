
-- vytvoření databáze a přepnutí do ní
CREATE DATABASE IF NOT EXISTS dino_run
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_czech_ci;
USE dino_run;

-- tabulka hráčů
CREATE TABLE hrac (
    id         INT AUTO_INCREMENT PRIMARY KEY,      -- primární klíč, čísluje se automaticky
    username   VARCHAR(50)  NOT NULL UNIQUE,        -- jméno hráče, nesmí se opakovat
    heslo      VARCHAR(255) NOT NULL,               -- zahashované heslo (nikdy ne v čitelné podobě)
    highscore  INT NOT NULL DEFAULT 0               -- nejlepší skóre hráče
);

-- tabulka odehraných her
CREATE TABLE hra (
    id         INT AUTO_INCREMENT PRIMARY KEY,      -- primární klíč hry
    id_hrac    INT NOT NULL,                        -- cizí klíč: kdo hru odehrál
    score      INT NOT NULL DEFAULT 0,              -- dosažené skóre v této hře
    FOREIGN KEY (id_hrac) REFERENCES hrac(id)
        ON DELETE CASCADE                           -- smazáním hráče se smažou i jeho hry
);