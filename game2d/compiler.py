import pygame
import random

# --- Cấu hình cơ bản ---
TILE_SIZE = 32
MAP_WIDTH = 20
MAP_HEIGHT = 15
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD  = (255, 215, 0)
GRAY  = (100, 100, 100)

# --- Map (0: floor, 1: wall, 2: trap, 3: treasure) ---
dungeon_map = [
    [1]*MAP_WIDTH
] + [
    [1] + [0]*(MAP_WIDTH-2) + [1] for _ in range(MAP_HEIGHT-2)
] + [
    [1]*MAP_WIDTH
]

# Add traps and treasure
for _ in range(10):
    x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
    dungeon_map[y][x] = 2  # trap
for _ in range(5):
    x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
    dungeon_map[y][x] = 3  # treasure

# --- Player ---
player_pos = [1,1]
player_hp = 10
score = 0

# --- Quái vật ---
monsters = [[MAP_WIDTH-2, MAP_HEIGHT-2]]

# --- Pygame setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

def draw_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            tile = dungeon_map[y][x]
            color = WHITE
            if tile == 1:
                color = GRAY
            elif tile == 2:
                color = RED
            elif tile == 3:
                color = GOLD
            pygame.draw.rect(screen, color, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

def move_monsters():
    for m in monsters:
        # simple random move
        dx, dy = random.choice([[0,1],[0,-1],[1,0],[-1,0],[0,0]])
        new_x, new_y = m[0]+dx, m[1]+dy
        if dungeon_map[new_y][new_x] != 1:
            m[0], m[1] = new_x, new_y

running = True
while running:
    screen.fill(BLACK)
    draw_map()

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_pos[0]*TILE_SIZE, player_pos[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # Draw monsters
    for m in monsters:
        pygame.draw.rect(screen, RED, (m[0]*TILE_SIZE, m[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = 0, 0
            if event.key == pygame.K_LEFT: dx = -1
            elif event.key == pygame.K_RIGHT: dx = 1
            elif event.key == pygame.K_UP: dy = -1
            elif event.key == pygame.K_DOWN: dy = 1
            new_x, new_y = player_pos[0]+dx, player_pos[1]+dy
            if dungeon_map[new_y][new_x] != 1:
                player_pos[0], player_pos[1] = new_x, new_y
                # Check traps
                if dungeon_map[new_y][new_x] == 2:
                    player_hp -= 1
                    print(f"Trap! HP = {player_hp}")
                # Check treasure
                elif dungeon_map[new_y][new_x] == 3:
                    score += 10
                    dungeon_map[new_y][new_x] = 0
                    print(f"Treasure! Score = {score}")

    # Monster moves
    move_monsters()

    # Check collision with monsters
    for m in monsters:
        if m == player_pos:
            player_hp -= 1
            print(f"Attacked by monster! HP = {player_hp}")

    # Check game over
    if player_hp <= 0:
        print("Game Over!")
        running = False

    pygame.display.flip()
    clock.tick(5)  # FPS

pygame.quit()
