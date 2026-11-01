import pygame
import random
import json
import os
from datetime import datetime

pygame.init()

SIRKA = 800
VYSKA = 600
FPS = 60

okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Astro Strike")
hodiny = pygame.time.Clock()

# barvy
CERNA = (0, 0, 0)
BILA = (255, 255, 255)
SEDA = (140, 140, 140)
MODRA = (50, 120, 255)
SVETLE_MODRA = (120, 200, 255)
CERVENA = (230, 50, 50)
ZELENA = (50, 200, 80)
ZLUTA = (255, 220, 0)
FIALOVA = (170, 80, 220)
ORANZOVA = (255, 150, 40)

font_nadpis = pygame.font.Font(None, 90)
font_velky = pygame.font.Font(None, 50)
font_stredni = pygame.font.Font(None, 38)
font_maly = pygame.font.Font(None, 28)

# soubor se zebrickem je ve stejne slozce jako hra
SOUBOR_SKORE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skore.json")

# nazev, rychlost nepratel, kolikrat vic bodu
OBTIZNOSTI = [
    ("Lehká", 0.8, 1),
    ("Normální", 1.0, 2),
    ("Těžká", 1.4, 3),
]


def text(co, font, barva, x, y, zarovnani="stred"):
    obrazek = font.render(str(co), True, barva)
    rect = obrazek.get_rect()
    if zarovnani == "stred":
        rect.center = (x, y)
    elif zarovnani == "vlevo":
        rect.midleft = (x, y)
    else:
        rect.midright = (x, y)
    okno.blit(obrazek, rect)


def nacti_skore():
    if not os.path.exists(SOUBOR_SKORE):
        return []
    try:
        with open(SOUBOR_SKORE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            # nechame jen zaznamy ktere davaji smysl
            return [z for z in data if isinstance(z, dict) and isinstance(z.get("skore"), int)]
    except (OSError, ValueError):
        pass
    # kdyz je soubor rozbity, zacne se znova
    return []


def uloz_skore(seznam):
    try:
        with open(SOUBOR_SKORE, "w", encoding="utf-8") as f:
            json.dump(seznam, f, ensure_ascii=False, indent=2)
    except OSError:
        print("nepodarilo se ulozit skore")


class Hrac:
    def __init__(self):
        self.rect = pygame.Rect(SIRKA // 2 - 25, VYSKA - 60, 50, 32)
        self.rychlost = 6
        self.zivoty = 3
        self.cooldown = 0
        self.nesmrtelnost = 0  # po zasahu chvili blika a nejde zasahnout

    def pohyb(self, klavesy):
        if klavesy[pygame.K_LEFT] or klavesy[pygame.K_a]:
            self.rect.x -= self.rychlost
        if klavesy[pygame.K_RIGHT] or klavesy[pygame.K_d]:
            self.rect.x += self.rychlost
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SIRKA:
            self.rect.right = SIRKA

        if self.cooldown > 0:
            self.cooldown -= 1
        if self.nesmrtelnost > 0:
            self.nesmrtelnost -= 1

    def kresli(self):
        if self.nesmrtelnost > 0 and self.nesmrtelnost % 10 < 5:
            return
        r = self.rect
        # plamen z motoru
        plamen = random.randint(6, 12)
        pygame.draw.polygon(okno, ORANZOVA, [(r.centerx - 6, r.bottom), (r.centerx + 6, r.bottom), (r.centerx, r.bottom + plamen)])
        pygame.draw.polygon(okno, MODRA, [r.midtop, r.bottomleft, r.bottomright])
        pygame.draw.circle(okno, SVETLE_MODRA, (r.centerx, r.centery + 4), 5)


class Strela:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 2, y - 12, 4, 12)

    def pohyb(self):
        self.rect.y -= 10

    def kresli(self):
        pygame.draw.rect(okno, ZLUTA, self.rect)


class Nepritel:
    def __init__(self, rychlost, velky=False):
        self.velky = velky
        if velky:
            self.rect = pygame.Rect(0, 0, 54, 40)
            self.zivoty = 3
            self.body = 25
            self.rychlost = rychlost * 0.7
            self.barva = FIALOVA
        else:
            self.rect = pygame.Rect(0, 0, 40, 30)
            self.zivoty = 1
            self.body = 10
            self.rychlost = rychlost
            self.barva = CERVENA
        self.rect.x = random.randint(0, SIRKA - self.rect.width)
        self.rect.bottom = 0
        self.y = float(self.rect.y)  # rect umi jen cela cisla, tak si pamatuju presnou pozici
        self.zasah = 0

    def pohyb(self):
        self.y += self.rychlost
        self.rect.y = int(self.y)
        if self.zasah > 0:
            self.zasah -= 1

    def kresli(self):
        barva = BILA if self.zasah > 0 else self.barva
        pygame.draw.rect(okno, barva, self.rect)
        # oci
        pygame.draw.rect(okno, CERNA, (self.rect.x + 8, self.rect.y + 8, 7, 7))
        pygame.draw.rect(okno, CERNA, (self.rect.right - 15, self.rect.y + 8, 7, 7))


class Srdce:
    # bonus, ktery obcas vypadne z nepritele, prida zivot
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 10, y - 10, 20, 20)

    def pohyb(self):
        self.rect.y += 3

    def kresli(self):
        x, y = self.rect.x, self.rect.y
        pygame.draw.circle(okno, ZELENA, (x + 5, y + 6), 6)
        pygame.draw.circle(okno, ZELENA, (x + 15, y + 6), 6)
        pygame.draw.polygon(okno, ZELENA, [(x - 1, y + 8), (x + 21, y + 8), (x + 10, y + 20)])


class Hra:
    # jedna rozehrana hra
    def __init__(self, obtiznost):
        self.nazev_obtiznosti, self.nasobic_rychlosti, self.nasobic_bodu = OBTIZNOSTI[obtiznost]
        self.hrac = Hrac()
        self.strely = []
        self.nepratele = []
        self.srdce = []
        self.jiskry = []  # castice vybuchu [x, y, vx, vy, zivot, barva]
        self.skore = 0
        self.zabito = 0
        self.vlna = 1
        self.snimky = 0
        self.casovac = 0
        self.konec = False

    def novy_nepritel(self):
        rychlost = (2 + (self.vlna - 1) * 0.4 + random.uniform(-0.4, 0.4)) * self.nasobic_rychlosti
        velky = self.vlna >= 3 and random.random() < 0.25
        self.nepratele.append(Nepritel(rychlost, velky))

    def vybuch(self, x, y, barva):
        for i in range(15):
            self.jiskry.append([x, y, random.uniform(-4, 4), random.uniform(-4, 4), random.randint(15, 30), barva])

    def update(self, klavesy):
        if self.konec:
            return
        self.snimky += 1

        self.hrac.pohyb(klavesy)
        if klavesy[pygame.K_SPACE] and self.hrac.cooldown == 0:
            self.strely.append(Strela(self.hrac.rect.centerx, self.hrac.rect.top))
            self.hrac.cooldown = 15

        # cim vyssi vlna tim casteji chodi nepratele
        self.casovac += 1
        if self.casovac >= max(18, 60 - (self.vlna - 1) * 5):
            self.casovac = 0
            self.novy_nepritel()

        for s in self.strely:
            s.pohyb()
        for n in self.nepratele:
            n.pohyb()
        for s in self.srdce:
            s.pohyb()
        for j in self.jiskry:
            j[0] += j[2]
            j[1] += j[3]
            j[4] -= 1

        # strela trefila nepritele
        for n in self.nepratele[:]:
            for s in self.strely[:]:
                if n.rect.colliderect(s.rect):
                    self.strely.remove(s)
                    n.zivoty -= 1
                    n.zasah = 5
                    if n.zivoty <= 0:
                        self.nepratele.remove(n)
                        self.zabito += 1
                        self.skore += n.body * self.nasobic_bodu
                        self.vybuch(n.rect.centerx, n.rect.centery, n.barva)
                        if random.random() < 0.05:
                            self.srdce.append(Srdce(n.rect.centerx, n.rect.centery))
                    break

        # nepritel narazil do hrace
        for n in self.nepratele[:]:
            if n.rect.colliderect(self.hrac.rect) and self.hrac.nesmrtelnost == 0:
                self.nepratele.remove(n)
                self.hrac.zivoty -= 1
                self.hrac.nesmrtelnost = 90
                self.vybuch(n.rect.centerx, n.rect.centery, ORANZOVA)

        # sebrani srdce
        for s in self.srdce[:]:
            if s.rect.colliderect(self.hrac.rect):
                self.srdce.remove(s)
                if self.hrac.zivoty < 5:
                    self.hrac.zivoty += 1

        # nepritel proletel dolu = minus zivot
        for n in self.nepratele[:]:
            if n.rect.top > VYSKA:
                self.nepratele.remove(n)
                self.hrac.zivoty -= 1

        self.strely = [s for s in self.strely if s.rect.bottom > 0]
        self.srdce = [s for s in self.srdce if s.rect.top < VYSKA]
        self.jiskry = [j for j in self.jiskry if j[4] > 0]

        self.vlna = 1 + self.zabito // 15

        if self.hrac.zivoty <= 0:
            self.hrac.zivoty = 0
            self.konec = True
            self.vybuch(self.hrac.rect.centerx, self.hrac.rect.centery, MODRA)

    def kresli(self):
        for j in self.jiskry:
            pygame.draw.circle(okno, j[5], (int(j[0]), int(j[1])), 2)
        for n in self.nepratele:
            n.kresli()
        for s in self.strely:
            s.kresli()
        for s in self.srdce:
            s.kresli()
        if not self.konec:
            self.hrac.kresli()

        text("Skóre: " + str(self.skore), font_maly, BILA, 10, 20, "vlevo")
        text("Vlna: " + str(self.vlna), font_maly, BILA, SIRKA // 2, 20)
        text("Životy: " + str(self.hrac.zivoty), font_maly, BILA, SIRKA - 10, 20, "vpravo")


class Program:
    def __init__(self):
        self.stav = "menu"
        self.bezi = True
        self.obtiznost = 1
        self.vyber = 0
        self.jmeno = ""
        self.hra = None
        self.zebricek = nacti_skore()
        self.pozice = -1  # kde je posledni hra v zebricku (-1 = nedostala se tam)
        self.cekani = 0
        # hvezdy v pozadi [x, y, rychlost]
        self.hvezdy = []
        for i in range(80):
            self.hvezdy.append([random.randint(0, SIRKA), random.randint(0, VYSKA), random.choice([1, 2, 3])])

    def polozky_menu(self):
        return ["HRÁT", "OBTÍŽNOST: " + OBTIZNOSTI[self.obtiznost][0], "ŽEBŘÍČEK", "KONEC"]

    def nova_hra(self):
        self.hra = Hra(self.obtiznost)
        self.stav = "hra"

    def konec_hry(self):
        h = self.hra
        zaznam = {
            "jmeno": self.jmeno,
            "skore": h.skore,
            "vlna": h.vlna,
            "zabito": h.zabito,
            "obtiznost": h.nazev_obtiznosti,
            "datum": datetime.now().strftime("%d.%m.%Y"),
        }
        self.zebricek.append(zaznam)
        self.zebricek.sort(key=lambda z: z.get("skore", 0), reverse=True)
        self.zebricek = self.zebricek[:10]
        if zaznam in self.zebricek:
            self.pozice = self.zebricek.index(zaznam)
        else:
            self.pozice = -1
        uloz_skore(self.zebricek)
        self.cekani = 60  # chvili se ignoruji klavesy at to hrac hned nepreskoci
        self.stav = "konec"

    def udalost(self, e):
        if e.type != pygame.KEYDOWN and e.type != pygame.TEXTINPUT:
            return

        if self.stav == "menu":
            if e.type != pygame.KEYDOWN:
                return
            if e.key == pygame.K_UP:
                self.vyber = (self.vyber - 1) % 4
            elif e.key == pygame.K_DOWN:
                self.vyber = (self.vyber + 1) % 4
            elif e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                if self.vyber == 0:
                    self.stav = "jmeno"
                    pygame.key.start_text_input()
                elif self.vyber == 1:
                    self.obtiznost = (self.obtiznost + 1) % len(OBTIZNOSTI)
                elif self.vyber == 2:
                    self.pozice = -1
                    self.stav = "zebricek"
                else:
                    self.bezi = False

        elif self.stav == "jmeno":
            if e.type == pygame.TEXTINPUT:
                if len(self.jmeno) < 12 and e.text.isprintable():
                    self.jmeno += e.text
            elif e.key == pygame.K_BACKSPACE:
                self.jmeno = self.jmeno[:-1]
            elif e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                self.jmeno = self.jmeno.strip()
                if self.jmeno == "":
                    self.jmeno = "Hráč"
                pygame.key.stop_text_input()
                self.nova_hra()
            elif e.key == pygame.K_ESCAPE:
                pygame.key.stop_text_input()
                self.stav = "menu"

        elif self.stav == "hra":
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_p or e.key == pygame.K_ESCAPE):
                self.stav = "pauza"

        elif self.stav == "pauza":
            if e.type != pygame.KEYDOWN:
                return
            if e.key == pygame.K_p:
                self.stav = "hra"
            elif e.key == pygame.K_ESCAPE:
                self.hra = None
                self.stav = "menu"

        elif self.stav == "konec":
            if e.type != pygame.KEYDOWN or self.cekani > 0:
                return
            if e.key == pygame.K_r:
                self.nova_hra()
            elif e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                self.stav = "menu"

        elif self.stav == "zebricek":
            if e.type == pygame.KEYDOWN and e.key in (pygame.K_ESCAPE, pygame.K_RETURN, pygame.K_KP_ENTER):
                self.stav = "menu"

    def update(self):
        if self.stav != "pauza":
            rychlost = 3 if self.stav == "hra" else 1
            for h in self.hvezdy:
                h[1] += h[2] * rychlost * 0.5
                if h[1] > VYSKA:
                    h[0] = random.randint(0, SIRKA)
                    h[1] = 0

        if self.stav == "hra":
            self.hra.update(pygame.key.get_pressed())
            if self.hra.konec:
                self.konec_hry()
        elif self.stav == "konec":
            if self.cekani > 0:
                self.cekani -= 1
            # dohoreni vybuchu
            for j in self.hra.jiskry:
                j[0] += j[2]
                j[1] += j[3]
                j[4] -= 1
            self.hra.jiskry = [j for j in self.hra.jiskry if j[4] > 0]

    def kresli(self):
        okno.fill(CERNA)
        for h in self.hvezdy:
            pygame.draw.circle(okno, (60 * h[2], 60 * h[2], 60 * h[2]), (int(h[0]), int(h[1])), 1)

        if self.stav == "menu":
            text("ASTRO STRIKE", font_nadpis, MODRA, SIRKA // 2, 130)
            for i, polozka in enumerate(self.polozky_menu()):
                if i == self.vyber:
                    text("> " + polozka + " <", font_velky, ZLUTA, SIRKA // 2, 280 + i * 55)
                else:
                    text(polozka, font_velky, BILA, SIRKA // 2, 280 + i * 55)
            text("šipky = výběr, Enter = potvrdit", font_maly, SEDA, SIRKA // 2, 540)

        elif self.stav == "jmeno":
            text("Zadej jméno", font_velky, MODRA, SIRKA // 2, 200)
            pygame.draw.rect(okno, BILA, (SIRKA // 2 - 160, 260, 320, 50), 2)
            kurzor = "|" if pygame.time.get_ticks() // 500 % 2 == 0 else ""
            text(self.jmeno + kurzor, font_velky, BILA, SIRKA // 2, 285)
            text("Enter = začít hru, Esc = zpět", font_maly, SEDA, SIRKA // 2, 360)

        elif self.stav == "hra":
            self.hra.kresli()

        elif self.stav == "pauza":
            self.hra.kresli()
            text("PAUZA", font_nadpis, ZLUTA, SIRKA // 2, 260)
            text("P = pokračovat, Esc = do menu", font_stredni, BILA, SIRKA // 2, 330)

        elif self.stav == "konec":
            for j in self.hra.jiskry:
                pygame.draw.circle(okno, j[5], (int(j[0]), int(j[1])), 2)
            text("KONEC HRY", font_nadpis, CERVENA, SIRKA // 2, 130)
            text(self.jmeno + ": " + str(self.hra.skore) + " bodů", font_velky, BILA, SIRKA // 2, 210)
            text("vlna " + str(self.hra.vlna) + ", zničeno " + str(self.hra.zabito), font_stredni, BILA, SIRKA // 2, 260)
            if self.pozice == 0:
                text("NOVÝ REKORD!", font_velky, ZLUTA, SIRKA // 2, 330)
            elif self.pozice > 0:
                text(str(self.pozice + 1) + ". místo v žebříčku", font_stredni, ZELENA, SIRKA // 2, 330)
            text("R = znovu, Enter = menu", font_stredni, SEDA, SIRKA // 2, 430)

        elif self.stav == "zebricek":
            text("ŽEBŘÍČEK", font_nadpis, MODRA, SIRKA // 2, 70)
            if len(self.zebricek) == 0:
                text("Zatím nikdo nehrál.", font_stredni, SEDA, SIRKA // 2, 300)
            for i, z in enumerate(self.zebricek):
                y = 150 + i * 36
                barva = ZLUTA if i == 0 else BILA
                text(str(i + 1) + ".", font_stredni, barva, 110, y, "vpravo")
                text(z.get("jmeno", "?"), font_stredni, barva, 130, y, "vlevo")
                text(z.get("obtiznost", ""), font_maly, SEDA, 400, y, "vlevo")
                text(z.get("datum", ""), font_maly, SEDA, 540, y, "vlevo")
                text(z.get("skore", 0), font_stredni, barva, 720, y, "vpravo")
            text("Esc = zpět", font_maly, SEDA, SIRKA // 2, 560)

        pygame.display.flip()

    def spust(self):
        while self.bezi:
            hodiny.tick(FPS)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.bezi = False
                else:
                    self.udalost(e)
            self.update()
            self.kresli()
        pygame.quit()


if __name__ == "__main__":
    Program().spust()
