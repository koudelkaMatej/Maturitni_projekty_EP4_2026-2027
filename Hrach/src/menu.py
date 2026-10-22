from pathlib import Path
import pygame

ASSETS_DIR = Path(__file__).parent / "assets"

class Menu:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # textura pozadí
        raw_bg = pygame.image.load(ASSETS_DIR / "mainmenu.png").convert()
        self.bg = pygame.transform.scale(raw_bg, (800, 600))

        # textury tlačítek
        self.start_img = pygame.image.load(
            ASSETS_DIR / "start_button.png"
        ).convert_alpha()
        self.options_img = pygame.image.load(
            ASSETS_DIR / "options_button.png"
        ).convert_alpha()
        self.exit_img = pygame.image.load(
            ASSETS_DIR / "exit_button.png"
        ).convert_alpha()

        # pozice tlačítek (mezera 50 px od konce předchozího tlačítka)
        self.start_rect = self.start_img.get_rect(topleft=(60, 400))
        self.options_rect = self.options_img.get_rect(
            topleft=(self.start_rect.right + 50, 400)
        )
        self.exit_rect = self.exit_img.get_rect(
            topleft=(self.options_rect.right + 50, 400)
        )

    # tlacitka - (zatím nic nedělaj)
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            if self.start_rect.collidepoint(mouse_pos):
                pass

            elif self.options_rect.collidepoint(mouse_pos):
                pass

            elif self.exit_rect.collidepoint(mouse_pos):
                pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        # pozadí
        self.screen.blit(self.bg, (0, 0))

        # tlačítka
        self.screen.blit(self.start_img, self.start_rect)
        self.screen.blit(self.options_img, self.options_rect)
        self.screen.blit(self.exit_img, self.exit_rect)