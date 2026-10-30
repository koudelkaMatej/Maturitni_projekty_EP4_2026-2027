# Část 2: Proměnné, stavy a překážky
STATE_MENU = 0
STATE_GAME = 1
STATE_SCORE = 2
current_state = STATE_MENU

player_x = WIDTH // 2
player_y = 50
player_size = 30
player_speed = 6
fall_speed = 4

obstacles = [
    {"x": 100, "y": 200, "w": 400, "h": 20},
    {"x": 50, "y": 400, "w": 350, "h": 20},
    {"x": 150, "y": 600, "w": 350, "h": 20},
]

def reset_game():
    global player_x, player_y
    player_x = WIDTH // 2
    player_y = 50

running = True
start_ticks = 0
