# Část 4: Herní logika, kolize a ukončení smyčky
    elif current_state == STATE_GAME:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
            
        player_y += fall_speed
        
        if player_x < 0: player_x = 0
        if player_x > WIDTH - player_size: player_x = WIDTH - player_size
        
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for obs in obstacles:
            obs_rect = pygame.Rect(obs["x"], obs["y"], obs["w"], obs["h"])
            if player_rect.colliderect(obs_rect):
                current_state = STATE_MENU

        if player_y > HEIGHT:
            seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
            
            conn = sqlite3.connect("dropper.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", ("Hráč", seconds))
            conn.commit()
            conn.close()
            
            current_state = STATE_MENU

        pygame.draw.rect(screen, RED, player_rect)
        for obs in obstacles:
            pygame.draw.rect(screen, BLUE, (obs["x"], obs["y"], obs["w"], obs["h"]))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
