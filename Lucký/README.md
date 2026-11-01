# Astro Strike

Jednoducha vesmirna strilecka v Pythonu (pygame).

Shora padaji nepratele a ty je musis sestrelit driv nez doleti dolu.
Kazdych 15 znicenych nepratel zacne dalsi vlna a jsou rychlejsi.
Od 3. vlny chodi i velci fialovi, ti vydrzi 3 zasahy.
Obcas z nepritele vypadne zelene srdce, to prida zivot (max 5).

## Ovladani

- sipky nebo A / D - pohyb
- mezernik - strelba
- P nebo Esc - pauza

## Spusteni

```
pip install -r requirements.txt
python main.py
```

Na Windows staci pustit `instalace.bat`, ten udela `.venv`, nainstaluje pygame a otevre projekt ve VS Code.

Pouzivam pygame-ce, protoze normalni pygame nejde nainstalovat na Python 3.14. V kodu se importuje stejne (`import pygame`).

Zebricek (top 10) se uklada do souboru `skore.json` vedle hry.
