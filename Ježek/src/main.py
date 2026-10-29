import sys
import pygame

pygame.init()

# Rozměry okna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Run - Menu")

clock = pygame.time.Clock()
FPS = 60

# Barvy
BG_COLOR = (26, 26, 26)
PANEL_COLOR = (34, 34, 34)
TEXT_COLOR = (240, 240, 240)
MUTED_TEXT = (160, 160, 160)
BTN_DEFAULT = (50, 50, 50)
BTN_HOVER = (92, 184, 92)
BTN_TEXT = (255, 255, 255)
BORDER_COLOR = (70, 70, 70)

# Fonty
font_title = pygame.font.SysFont("Courier New", 42, bold=True)
font_btn = pygame.font.SysFont("Courier New", 26, bold=True)
font_info = pygame.font.SysFont("Courier New", 20)


class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        color = BTN_HOVER if self.is_hovered else BTN_DEFAULT
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, width=2, border_radius=8)

        text_surf = font_btn.render(self.text, True, BTN_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered and self.callback:
                self.callback()


# Stav aplikace
current_view = "menu"  # "menu", "game", "options"
current_jump_key = "SPACE"
available_keys = ["SPACE", "UP ARROW", "W"]
key_index = 0


def action_start():
    global current_view
    current_view = "game"


def action_options():
    global current_view
    current_view = "options"


def action_exit():
    pygame.quit()
    sys.exit()


def action_back():
    global current_view
    current_view = "menu"


def toggle_key():
    global key_index, current_jump_key
    key_index = (key_index + 1) % len(available_keys)
    current_jump_key = available_keys[key_index]


# Tlačítka hlavního menu
btn_w, btn_h = 240, 50
start_x = (SCREEN_WIDTH - btn_w) // 2

menu_buttons = [
    Button("START", start_x, 190, btn_w, btn_h, action_start),
    Button("OPTIONS", start_x, 260, btn_w, btn_h, action_options),
    Button("EXIT", start_x, 330, btn_w, btn_h, action_exit),
]

# Tlačítka podmenu
options_buttons = [
    Button("ZMĚNIT KLÁVESU", start_x, 240, btn_w, btn_h, toggle_key),
    Button("ZPĚT", start_x, 320, btn_w, btn_h, action_back),
]

game_buttons = [
    Button("ZPĚT DO MENU", start_x, 320, btn_w, btn_h, action_back),
]


def render_menu(mouse_pos):
    # Titulek
    title = font_title.render("DINO RUN", True, BTN_HOVER)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)

    subtitle = font_info.render("Hlavní menu", True, MUTED_TEXT)
    sub_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 145))
    screen.blit(subtitle, sub_rect)

    for btn in menu_buttons:
        btn.update(mouse_pos)
        btn.draw(screen)


def render_options(mouse_pos):
    title = font_title.render("OPTIONS", True, BTN_HOVER)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)

    info_text = f"Klávesa pro skok: [ {current_jump_key} ]"
    info = font_info.render(info_text, True, TEXT_COLOR)
    info_rect = info.get_rect(center=(SCREEN_WIDTH // 2, 180))
    screen.blit(info, info_rect)

    for btn in options_buttons:
        btn.update(mouse_pos)
        btn.draw(screen)


def render_game(mouse_pos):
    title = font_title.render("HRA SPUŠTĚNA", True, BTN_HOVER)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 140))
    screen.blit(title, title_rect)

    info = font_info.render(f"Hra se připravuje... (Skok: {current_jump_key})", True, TEXT_COLOR)
    info_rect = info.get_rect(center=(SCREEN_WIDTH // 2, 210))
    screen.blit(info, info_rect)

    for btn in game_buttons:
        btn.update(mouse_pos)
        btn.draw(screen)


def main():
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if current_view != "menu":
                    action_back()
                else:
                    running = False

            # Zpracování kliků podle aktuálního zobrazení
            if current_view == "menu":
                for btn in menu_buttons:
                    btn.handle_event(event)
            elif current_view == "options":
                for btn in options_buttons:
                    btn.handle_event(event)
            elif current_view == "game":
                for btn in game_buttons:
                    btn.handle_event(event)

        screen.fill(BG_COLOR)

        if current_view == "menu":
            render_menu(mouse_pos)
        elif current_view == "options":
            render_options(mouse_pos)
        elif current_view == "game":
            render_game(mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

