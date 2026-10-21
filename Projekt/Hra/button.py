class Button():                                                                  #popis: Definuje třídu tlačítka, která sdružuje jeho vzhled, polohu a chování.
	def __init__(self, image, pos, text_input, font, base_color, hovering_color): #popis: Inicializuje tlačítko z obrázku, souřadnic, textu, fontu a barev.
		self.image = image                                                       #popis: Uloží obrázek tlačítka; může být None, pokud se má použít jen text.
		self.x_pos = pos[0]                                                      #popis: Uloží vodorovnou souřadnici středu tlačítka.
		self.y_pos = pos[1]                                                      #popis: Uloží svislou souřadnici středu tlačítka.
		self.font = font                                                         #popis: Uloží font používaný k vykreslení textu.
		self.base_color, self.hovering_color = base_color, hovering_color       #popis: Uloží běžnou barvu textu a barvu při najetí myší.
		self.text_input = text_input                                             #popis: Uloží text, který se zobrazí na tlačítku.
		self.text = self.font.render(self.text_input, True, self.base_color)     #popis: Vytvoří obraz textu v běžné barvě; True zapíná vyhlazování okrajů.
		if self.image is None:                                                   #popis: Zkontroluje, zda tlačítko nemá vlastní obrázek.
			self.image = self.text                                               #popis: Pokud obrázek chybí, použije jako obraz tlačítka samotný text.
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))         #popis: Vytvoří obdélník tlačítka a umístí jeho střed na zadané souřadnice.
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))     #popis: Vytvoří obdélník textu a zarovná jej na stejný střed.

	def update(self, screen):                                                   #popis: Vykreslí tlačítko a jeho text na zadanou obrazovku.
		if self.image is not None:                                              #popis: Ověří, že existuje obrázek tlačítka k vykreslení.
			screen.blit(self.image, self.rect)                                  #popis: Vykreslí obrázek tlačítka na obrazovku v jeho obdélníku.
		screen.blit(self.text, self.text_rect)                                  #popis: Vykreslí text tlačítka na obrazovku v jeho obdélníku.

	def checkForInput(self, position):                                          #popis: Zjistí, zda zadaná poloha leží uvnitř obdélníku tlačítka.
		if (position[0] in range(self.rect.left, self.rect.right) and           #popis: Ověří x uvnitř vodorovných hranic; pravý okraj se nepočítá.
			position[1] in range(self.rect.top, self.rect.bottom)):              #popis: Ověří y uvnitř svislých hranic; dolní okraj se nepočítá.
			return True                                                         #popis: Vrátí True, pokud poloha spadá dovnitř tlačítka.
		return False                                                            #popis: Vrátí False, pokud je poloha mimo tlačítko.

	def changeColor(self, position):                                            #popis: Nastaví barvu textu podle toho, zda je ukazatel myši nad tlačítkem.
		if (position[0] in range(self.rect.left, self.rect.right) and           #popis: Ověří x uvnitř vodorovných hranic tlačítka.
			position[1] in range(self.rect.top, self.rect.bottom)):              #popis: Ověří y uvnitř svislých hranic tlačítka.
			self.text = self.font.render(self.text_input, True, self.hovering_color) #popis: Znovu vytvoří text v barvě určené pro najetí myší.
		else:                                                                   #popis: Provede následující příkaz, pokud myš není nad tlačítkem.
			self.text = self.font.render(self.text_input, True, self.base_color) #popis: Znovu vytvoří text v běžné barvě.