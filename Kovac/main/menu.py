import sys
import pygame

# --- Nastavení ---
WIDTH, HEIGHT = 800, 300
FPS = 60


BG_COLOR = (247, 247, 247)
TEXT_COLOR = (83, 83, 83)
BUTTON_COLOR = (83, 83, 83)
BUTTON_HOVER = (120, 120, 120)
BUTTON_TEXT = (247, 247, 247)


class Button:
    """Třída pro jedno tlačítko v menu."""

    def __init__(self, text, center, size=(180, 50)):
        self.text = text                          # text, který bude na tlačítku
        self.rect = pygame.Rect(0, 0, *size)      # obdélník tlačítka se zadanou velikostí
        self.rect.center = center                 # umístění středu tlačítka na zadanou pozici

    def draw(self, screen, font):
        """Vykreslí tlačítko na obrazovku."""
        # zjistí, jestli je kurzor myši nad tlačítkem
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        # pokud ano, použije světlejší barvu (efekt najetí myší)
        color = BUTTON_HOVER if hovered else BUTTON_COLOR
        # nakreslí obdélník tlačítka se zaoblenými rohy
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        # vytvoří obrázek textu a vykreslí ho doprostřed tlačítka
        label = font.render(self.text, True, BUTTON_TEXT)
        screen.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        """Vrátí True, pokud uživatel klikl levým tlačítkem myši na toto tlačítko."""
        return (event.type == pygame.MOUSEBUTTONDOWN      # událost je stisk tlačítka myši
                and event.button == 1                     # jde o levé tlačítko myši
                and self.rect.collidepoint(event.pos))    # kliknutí bylo uvnitř tlačítka


def main_menu(screen, clock):
    """Zobrazí hlavní menu. Po stisku Start se vrátí, po stisku Exit ukončí program."""
    # písma pro nadpis a pro text tlačítek
    title_font = pygame.font.SysFont("arial", 48, bold=True)
    button_font = pygame.font.SysFont("arial", 28)

    # vytvoření tlačítek Start a Exit pod sebou uprostřed okna
    start_button = Button("Start", (WIDTH // 2, 160))
    exit_button = Button("Exit", (WIDTH // 2, 230))

    # hlavní smyčka menu – běží, dokud uživatel nezvolí Start nebo Exit
    while True:
        # zpracování všech událostí (klávesy, myš, zavření okna)
        for event in pygame.event.get():
            # zavření okna křížkem nebo kliknutí na Exit ukončí program
            if event.type == pygame.QUIT or exit_button.is_clicked(event):
                pygame.quit()
                sys.exit()
            # kliknutí na Start ukončí menu a přejde se do hry
            if start_button.is_clicked(event):
                return
            # hru lze spustit i mezerníkem nebo Enterem (jako u dino hry)
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                return

        # vymazání obrazovky barvou pozadí
        screen.fill(BG_COLOR)
        # vykreslení nadpisu hry nahoře uprostřed
        title = title_font.render("dinosaurus", True, TEXT_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 70)))
        # vykreslení obou tlačítek
        start_button.draw(screen, button_font)
        exit_button.draw(screen, button_font)

        pygame.display.flip()   # zobrazí nově vykreslený snímek
        clock.tick(FPS)         # omezí rychlost smyčky na 60 snímků za sekundu


def game(screen, clock):
    """Zatím jen místo pro samotnou hru. Klávesa ESC vrátí hráče do menu."""
    font = pygame.font.SysFont("arial", 28)

    # herní smyčka – sem se později doplní dinosaurus, překážky a skóre
    while True:
        for event in pygame.event.get():
            # zavření okna ukončí program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # klávesa ESC ukončí hru a vrátí se do menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        # vykreslení dočasného textu místo hry
        screen.fill(BG_COLOR)
        text = font.render("Zatím nic (ESC = back to menu)", True, TEXT_COLOR)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        clock.tick(FPS)


def main():
    """Hlavní funkce – připraví okno a střídá menu a hru."""
    pygame.init()                                       # spuštění knihovny pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))   # vytvoření okna hry
    pygame.display.set_caption("dinosaurus")              # nastavení titulku okna
    clock = pygame.time.Clock()                         # hodiny pro řízení rychlosti (FPS)

    # nekonečné střídání: menu -> hra -> menu -> hra ...
    while True:
        main_menu(screen, clock)
        game(screen, clock)


if __name__ == "__main__":
    main()