CREATE TABLE Hrac (
    id_hrace INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nick VARCHAR(50) NOT NULL,
    nejlepsi_skore INT UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;

CREATE TABLE Ovoce (
    id_ovoce INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(50) NOT NULL,
    body INT NOT NULL DEFAULT 0,
    efekt VARCHAR(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;

CREATE TABLE Herni_partie (
    id_partie INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_hrace INT UNSIGNED NOT NULL,
    datum DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    skore INT UNSIGNED NOT NULL DEFAULT 0,
    delka_hada INT UNSIGNED NOT NULL DEFAULT 1,
    CONSTRAINT fk_herni_partie_hrac
        FOREIGN KEY (id_hrace) REFERENCES Hrac(id_hrace)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;

CREATE TABLE Sebrane_ovoce (
    id_sebraneho_ovoce INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_partie INT UNSIGNED NOT NULL,
    id_ovoce INT UNSIGNED NOT NULL,
    pocet INT UNSIGNED NOT NULL DEFAULT 1,
    CONSTRAINT fk_sebrane_ovoce_partie
        FOREIGN KEY (id_partie) REFERENCES Herni_partie(id_partie)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_sebrane_ovoce_ovoce
        FOREIGN KEY (id_ovoce) REFERENCES Ovoce(id_ovoce)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    UNIQUE KEY uq_sebrane_ovoce_partie_ovoce (id_partie, id_ovoce)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;
