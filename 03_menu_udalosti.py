# Část 3: Události a vykreslení menu / žebříčku
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if current_state == STATE_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_state = STATE_GAME
                    reset_game()
                    start_ticks = pygame.time.get_ticks()
                elif event.key == pygame.K_2:
                    current_state = STATE_SCORE
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    
        elif current_state == STATE_SCORE or current_state == STATE_GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_state = STATE_MENU

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
