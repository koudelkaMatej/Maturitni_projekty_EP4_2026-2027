-- vytvoření databáze
CREATE DATABASE IF NOT EXISTS dino_run;

USE dino_run;

-- tabulka user (Id, Jméno, Heslo)
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jmeno VARCHAR(50) NOT NULL UNIQUE,
    heslo VARCHAR(255) NOT NULL
);

-- tabulka pro nastavení (Id, Key binds)
CREATE TABLE nastaveni (
    id INT PRIMARY KEY,
    key_binds VARCHAR(50) NOT NULL,
    FOREIGN KEY (id) REFERENCES user(id)
);

-- tabulka pro hru (Id, Skóre, Čas)
CREATE TABLE hra (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    score INT NOT NULL,
    cas INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
    
);

-- tag tabulka
CREATE TABLE tag (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(50) NOT NULL UNIQUE
);
