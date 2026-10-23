import pygame, sys, _mysql_connector                                                                                                          # Načte knihovnu Pygame pro hru a modul sys pro ukončení programu.
from button import Button                                                                                                   # Načte vlastní třídu Button pro vytváření tlačítek.

pygame.init()                                                                                                               # Inicializuje moduly Pygame, které hra potřebuje.

SCREEN = pygame.display.set_mode((1280, 720))                                                                               # Vytvoří herní okno o šířce 1280 a výšce 720 pixelů.
pygame.display.set_caption("Menu - Astrallift")                                                                             # Nastaví text zobrazený v záhlaví okna.

BG = pygame.image.load("Projekt/Hra/assets/images/Background.png")                                                          # Načte obrázek pozadí ze zadaného umístění.

#SQL - Database 
from pripojeni import *

# 1) Připojení k databázi
mydb = mysql.connector.connect(
    host=HOST,          # URL adresa databázového serveru
    user=USER,          # uživatelské jméno
    password=PASSWORD,  # heslo
    database=DATABASE   # název databáze
)

# 2) Vytvoření kurzoru — přes něj posíláme SQL příkazy a čteme výsledky
mycursor = mydb.cursor()

<<<<<<< HEAD
# ... zde budeme později psát SQL dotazy ...
=======
#load images
enemy_image = pygame.image.load("Maturitni_projekty_EP4_2026-2027/Projekt/Hra/assets/images/zombie1.png").convert_alpha()
>>>>>>> 9fbcc37 (a)

# 3) Odpojení — vždy na konci uzavřeme kurzor i spojení
mycursor.close()
mydb.close()

print("✅ Připojení a odpojení proběhlo úspěšně.")

# SQL dotaz v trojitých uvozovkách — umožňuje zápis na více řádků
mycursor.execute("""
    CREATE TABLE hraci (
        id INT,
        jmeno VARCHAR(15),
    )
""")

mycursor.execute("""
    CREATE TABLE hra (
        id INT,
        hrac_id INT,
        skore INT,
        rucne_vytezeno INT,
        stroji_vytezeno INT,
        datum DATETIME,
    )
""")

# commit() potvrdí provedení příkazu (jako stisknutí Enter)
mydb.commit()

#----------------------Konec SQL----------------------

def get_font(size):                                                                                                         # Definuje funkci, která vytvoří herní písmo zadané velikosti.
    return pygame.font.Font("Projekt/Hra/assets/font.ttf", size)                                                            # Načte soubor písma a vrátí jeho verzi dané velikosti.

def play():                                                                                                                 # Definuje funkci zobrazující obrazovku hry.
    while True:                                                                                                             # Opakuje vykreslování této obrazovky, dokud se z ní neodejde.
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             # Zjistí aktuální polohu kurzoru myši.

        SCREEN.fill("black")                                                                                                # Vyplní herní okno černou barvou.

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")                                          # Vytvoří bílý text pro obrazovku hry.
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))                                                                   # Umístí text doprostřed na souřadnice x=640 a y=260.
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)                                                                                   # Vykreslí vytvořený text do herního okna.

        PLAY_BACK = Button(image=None, pos=(640, 460),                                                                      # Vytvoří tlačítko Zpět bez obrázku na zadané pozici.
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")               # Nastaví text, velikost písma a barvy tlačítka.

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)                                                                               # Změní barvu tlačítka podle toho, zda je nad ním kurzor.
        PLAY_BACK.update(SCREEN)                                                                                            # Vykreslí tlačítko Zpět do herního okna.

        for event in pygame.event.get():                                                                                    # Projde všechny události, které Pygame od posledního snímku zaznamenalo.
            if event.type == pygame.QUIT:                                                                                   # Zkontroluje, zda uživatel zavřel okno hry.
                pygame.quit()                                                                                               # Ukončí moduly Pygame.
                sys.exit()                                                                                                  # Ukončí celý Python program.
            if event.type == pygame.MOUSEBUTTONDOWN:                                                                        # Zkontroluje, zda uživatel stiskl tlačítko myši.
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                                                                 # Ověří, zda uživatel klikl na tlačítko Zpět.
                    main_menu()                                                                                             # Zavolá funkci hlavního menu.

        pygame.display.update()                                                                                             # Aktualizuje okno, aby se zobrazily změny z tohoto průchodu smyčkou.

def options():                                                                                                              # Definuje funkci zobrazující obrazovku možností.
    while True:                                                                                                             # Opakuje vykreslování této obrazovky, dokud se z ní neodejde.
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()                                                                          # Zjistí aktuální polohu kurzoru myši.

        SCREEN.fill("white")                                                                                                # Vyplní herní okno bílou barvou.

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")                                    # Vytvoří černý text pro obrazovku možností.
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))                                                             # Umístí text doprostřed na souřadnice x=640 a y=260.
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)                                                                             # Vykreslí vytvořený text do herního okna.

        OPTIONS_BACK = Button(image=None, pos=(640, 460),                                                                   # Vytvoří tlačítko Zpět bez obrázku na zadané pozici.
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")               # Nastaví text, velikost písma a barvy tlačítka.

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)                                                                         # Změní barvu tlačítka podle toho, zda je nad ním kurzor.
        OPTIONS_BACK.update(SCREEN)                                                                                         # Vykreslí tlačítko Zpět do herního okna.

        for event in pygame.event.get():                                                                                    # Projde všechny události, které Pygame od posledního snímku zaznamenalo.
            if event.type == pygame.QUIT:                                                                                   # Zkontroluje, zda uživatel zavřel okno hry.
                pygame.quit()                                                                                               # Ukončí moduly Pygame.
                sys.exit()                                                                                                  # Ukončí celý Python program.
            if event.type == pygame.MOUSEBUTTONDOWN:                                                                        # Zkontroluje, zda uživatel stiskl tlačítko myši.
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):                                                           # Ověří, zda uživatel klikl na tlačítko Zpět.
                    main_menu()                                                                                             # Zavolá funkci hlavního menu.

        pygame.display.update()                                                                                             # Aktualizuje okno, aby se zobrazily změny z tohoto průchodu smyčkou.

def main_menu():                                                                                                            # Definuje funkci hlavního menu hry.
    while True:                                                                                                             # Neustále opakuje vykreslování menu a zpracování uživatelských událostí.
        SCREEN.blit(BG, (0, 0))                                                                                             # Vykreslí obrázek pozadí od levého horního rohu okna.

        MENU_MOUSE_POS = pygame.mouse.get_pos()                                                                             # Zjistí aktuální polohu kurzoru myši.

        MENU_TEXT = get_font(100).render("Hlavní Menu", True, "#b68f40")                                                    # Vytvoří nadpis menu písmem velikosti 100 a zlatavou barvou.
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))                                                                   # Umístí nadpis doprostřed horní části okna.

        PLAY_BUTTON = Button(image=pygame.image.load("Projekt/Hra/assets/images/Play Rect.png"), pos=(640, 250),            # Načte obrázek a vytvoří tlačítko Play na jeho pozici.
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")             # Nastaví text, písmo a barvy tlačítka Play.
        OPTIONS_BUTTON = Button(image=pygame.image.load("Projekt/Hra/assets/images/Options Rect.png"), pos=(640, 400),      # Načte obrázek a vytvoří tlačítko Options na jeho pozici.
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")          # Nastaví text, písmo a barvy tlačítka Options.
        QUIT_BUTTON = Button(image=pygame.image.load("Projekt/Hra/assets/images/Quit Rect.png"), pos=(640, 550),            # Načte obrázek a vytvoří tlačítko Quit na jeho pozici.
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")             # Nastaví text, písmo a barvy tlačítka Quit.

        SCREEN.blit(MENU_TEXT, MENU_RECT)                                                                                   # Vykreslí nadpis hlavního menu do herního okna.

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:                                                           # Projde všechna tři tlačítka hlavního menu.
            button.changeColor(MENU_MOUSE_POS)                                                                              # Nastaví barvu tlačítka podle polohy kurzoru.
            button.update(SCREEN)                                                                                           # Vykreslí tlačítko do herního okna.

        for event in pygame.event.get():                                                                                    # Projde všechny události, které Pygame od posledního snímku zaznamenalo.
            if event.type == pygame.QUIT:                                                                                   # Zkontroluje, zda uživatel zavřel okno hry.
                pygame.quit()                                                                                               # Ukončí moduly Pygame.
                sys.exit()                                                                                                  # Ukončí celý Python program.
            if event.type == pygame.MOUSEBUTTONDOWN:                                                                        # Zkontroluje, zda uživatel stiskl tlačítko myši.
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):                                                               # Ověří, zda uživatel klikl na tlačítko Play.
                    play()                                                                                                  # Otevře obrazovku hry.
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):                                                            # Ověří, zda uživatel klikl na tlačítko Options.
                    options()                                                                                               # Otevře obrazovku možností.
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):                                                               # Ověří, zda uživatel klikl na tlačítko Quit.
                    pygame.quit()                                                                                           # Ukončí moduly Pygame.
                    sys.exit()                                                                                              # Ukončí celý Python program.

        pygame.display.update()                                                                                             # Aktualizuje okno, aby se zobrazily změny z tohoto průchodu smyčkou.

main_menu()                                                                                                                 # Spustí hlavní menu a tím zahájí běh programu.