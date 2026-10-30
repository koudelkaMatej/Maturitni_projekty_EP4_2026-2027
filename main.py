import pygame
import sqlite3
import sys

# Inicializace hry
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maturitní projekt - Dropper")
clock = pygame.time.Clock()

# Základní barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 100, 200)
GREEN = (50, 200, 50)

font = pygame.font.SysFont(None, 36)
font_large = pygame.font.SysFont(None, 60)

# Inicializace databáze pro skóre
def init_db():
    conn = sqlite3.connect("dropper.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Stavy hry (menu, hra, žebříček)
STATE_MENU = 0
STATE_GAME = 1
STATE_SCORE = 2
current_state = STATE_MENU

# Hráč a překážky
player_x = WIDTH // 2
player_y = 50
player_size = 30
player_speed = 6
fall_speed = 4

# Seznam překážek (x, y, šířka, výška)
obstacles = [
    {"x": 50, "y": 200, "w": 200, "h": 20},   # mezera vpravo
    {"x": 350, "y": 400, "w": 200, "h": 20},  # mezera vlevo
    {"x": 200, "y": 600, "w": 200, "h": 20},  # mezera po stranách
]

def reset_game():
    global player_x, player_y
    player_x = WIDTH // 2
    player_y = 50

# Hlavní herní smyčka
running = True
start_ticks = 0

while running:
    screen.fill(BLACK)

    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_state == STATE_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Start hry
                    current_state = STATE_GAME
                    reset_game()
                    start_ticks = pygame.time.get_ticks()
                elif event.key == pygame.K_2:  # Žebříček
                    current_state = STATE_SCORE
                elif event.key == pygame.K_ESCAPE:
                    running = False

        elif current_state == STATE_SCORE or current_state == STATE_GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_state = STATE_MENU

    # Logika a vykreslování podle stavu
    if current_state == STATE_MENU:
        title = font_large.render("DROPPER GAME", True, WHITE)
        m1 = font.render("Stiskni 1 - Start hry", True, GREEN)
        m2 = font.render("Stiskni 2 - Žebříček", True, BLUE)
        m3 = font.render("Stiskni ESC - Konec", True, RED)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, 200))
        screen.blit(m1, (WIDTH//2 - m1.get_width()//2, 350))
        screen.blit(m2, (WIDTH//2 - m2.get_width()//2, 410))
        screen.blit(m3, (WIDTH//2 - m3.get_width()//2, 470))

    elif current_state == STATE_SCORE:
        title = font_large.render("ZEBRICEK", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        # Načtení skóre z DB
        conn = sqlite3.connect("dropper.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, score FROM scores ORDER BY score ASC LIMIT 5")
        rows = cursor.fetchall()
        conn.close()

        y_offset = 250
        for i, row in enumerate(rows):
            txt = font.render(f"{i+1}. {row[0]} - {row[1]} s", True, WHITE)
            screen.blit(txt, (WIDTH//2 - txt.get_width()//2, y_offset))
            y_offset += 50

        back = font.render("ESC pro navrat do menu", True, RED)
        screen.blit(back, (WIDTH//2 - back.get_width()//2, 700))

    elif current_state == STATE_GAME:
        # Ovládání šipkami nebo A/D
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed

        # Pád hráče dolů
        player_y += fall_speed

        # Omezení pohybu v rámci okna
        if player_x < 0: player_x = 0
        if player_x > WIDTH - player_size: player_x = WIDTH - player_size

        # Kolize s překážkami
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for obs in obstacles:
            obs_rect = pygame.Rect(obs["x"], obs["y"], obs["w"], obs["h"])
            if player_rect.colliderect(obs_rect):
                # Při nárazu hra končí a vrací do menu
                current_state = STATE_MENU

        # Výhra - doletění na dno obrazovky
        if player_y > HEIGHT:
            seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)

            # Uložení výsledku do databáze
            conn = sqlite3.connect("dropper.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", ("Hráč", seconds))
            conn.commit()
            conn.close()

            current_state = STATE_MENU

        # Vykreslení hráče a překážek
        pygame.draw.rect(screen, RED, player_rect)
        for obs in obstacles:
            pygame.draw.rect(screen, BLUE, (obs["x"], obs["y"], obs["w"], obs["h"]))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
