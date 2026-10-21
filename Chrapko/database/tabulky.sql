-- vytvoření databáze
CREATE DATABASE IF NOT EXISTS flappy;

USE flappy;

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

-- tabulka pro hru (Id, Scóre, Čas)
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

-- spojovací tabulka pro hru a tagy
CREATE TABLE hra_tag (
    hra_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (hra_id, tag_id),
    FOREIGN KEY (hra_id) REFERENCES hra(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id)
);
