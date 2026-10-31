from pathlib import Path
import pygame

# najde cestu k adresari pres parent - gamefiles -> assets
ASSETS_DIR = Path(__file__).parent / "assets"

class Menu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        screen_w, screen_h = self.screen.get_size()

        # 1. Nacteni pozadi a roztazeni pozadi
        raw_bg = pygame.image.load(ASSETS_DIR / "menubg.png").convert()  #nacte obrazek a prevede na format pro rychle vykresleni
        self.bg = pygame.transform.scale(raw_bg, (screen_w, screen_h)) #roztahne na pomer okna danny uz v main.py
        """raw = obrazek pred transformaci, self.bg = obrazek po transformaci"""


        # 2. Nacteni textur buttonu a nastaveni na velikost
        btn_w, btn_h = 700, 200
        raw_start = pygame.image.load(ASSETS_DIR / "startbtn.png").convert_alpha() # convert alpha zachovava pruhlednost (bude pridano)
        raw_settings = pygame.image.load(ASSETS_DIR / "settingsbtn.png").convert_alpha()
        raw_exit = pygame.image.load(ASSETS_DIR / "exitbtn.png").convert_alpha()

        self.start_img = pygame.transform.scale(raw_start, (btn_w, btn_h))   # nastavei na tu velikost
        self.settings_img = pygame.transform.scale(raw_settings, (btn_w, btn_h))
        self.exit_img = pygame.transform.scale(raw_exit, (btn_w, btn_h))


        # 3. nastaveni tlacitka na stred a mezera
        center_x = (screen_w - btn_w) // 2  #spocita souradnici aby tlacitko bylo na stredu (sirka okna - sir. tlacitka )
        start_y = 300  # y prvniho tlacitka
        mezera = 30       # mezera

        #tlacitko start
        self.start_rect = self.start_img.get_rect(topleft=(center_x, start_y)) # nastavni podle sirky tlacitka jeho "hitbox" a souradnici

        #tlacitko nastaveni
        self.settings_rect = self.settings_img.get_rect(
            topleft=(center_x, self.start_rect.bottom + mezera)    
        )

        #tlacitko exit
        self.exit_rect = self.exit_img.get_rect(
            topleft=(center_x, self.settings_rect.bottom + mezera)
        )

    #klikani mysi - zpracovani kliknuti a vraceni stavu
    def handle_event(self, event: pygame.event.Event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    #kontorla zda je kliknuto levym tlacitkem mysi
            mouse_pos = event.pos                                          # zjisteni pozice mysi

            if self.start_rect.collidepoint(mouse_pos):
                return "GAME"                               #pokud je kliknuto na start talcitko, vrati se stav GAME a v main se prepne na okno hry

            elif self.settings_rect.collidepoint(mouse_pos):
                return "SETTINGS"                           #pokud tl settings, prepne se na okno nastaveni

            elif self.exit_rect.collidepoint(mouse_pos):
                return "EXIT"                               #pokud tl exit, prepne se na ukonceni hry = vypne se

        return "MENU"       #klik mimo tlacitka = zustane v menu

    def draw(self) -> None: # vykreslovaci funkce, vola se na ni v main.py a vykresluje pozadi a tlacitka
        # Pozadí
        self.screen.blit(self.bg, (0, 0))  #vbykresleni pozadi na souradnici 0 0

        # tlacitka
        self.screen.blit(self.start_img, self.start_rect)   #vykresleni tlacitka start na souradnici podle self.start_rect (predvypocitane v __init__)
        self.screen.blit(self.settings_img, self.settings_rect) #to stejne pro settings
        self.screen.blit(self.exit_img, self.exit_rect) #to stejne pro exit