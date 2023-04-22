import pygame
import random

# Constant values
WINDOW_SIZE = (173, 200)
WINDOW_TITLE = "Minesweeper"
MAX_FPS = 30

# Initialize pygame modules
pygame.init()

# Create Clock object
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 25)

# Load images
bomb_img = pygame.image.load("./assets/bomb.png")
clock_img = pygame.image.load("./assets/time.png")

# Color definitions
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# Window configs
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)
pygame.display.set_icon(bomb_img)


class Cell():
    is_bomb = False
    x = 0
    y = 0

    def __init__(self, pos):
        self.pos = pos
        # "Normal" | "Flagged" | "Blank" | "Warn1" to "Warn8" | "Exploded"
        self.flag = "Normal"


def show_timer():
    # Show clock image
    image_position = (10, 173)
    window.blit(clock_img, image_position)

    # Show timer
    ticks_now = pygame.time.get_ticks()
    mins = int(ticks_now / 1000 / 60)
    secs = int(ticks_now / 1000 % 60)

    # Fill with zero
    timer_mins = ""
    timer_secs = ""
    if mins < 10:
        timer_mins = "0" + str(mins)
    else:
        timer_mins = str(mins)
    if secs < 10:
        timer_secs = "0" + str(secs)
    else:
        timer_secs = str(secs)
    timer_time = font.render(timer_mins + ":" + timer_secs, True, black)
    text_position = (30, 173)
    window.blit(timer_time, text_position)


def init_cells():
    for x in range(9):
        for y in range(9):
            cell_pos = (x*17 + 10, y*17 + 10)
            cell_pos_rect = pygame.Rect(cell_pos, (17, 17))
            cell = Cell(cell_pos_rect)
            cell.x = x
            cell.y = y
            cells.append(cell)


def pick_boms(num_boms):
    global num_boms_now
    while num_boms_now < num_boms:
        cells_len = len(cells)
        random_index = random.randrange(cells_len)
        if not cells[random_index].is_bomb:
            cells[random_index].is_bomb = True
            num_boms_now += 1


cells = []
num_boms_now = 0

init_cells()
pick_boms(10)

# Main loop
running = True
while running:
    window.fill(white)

    show_timer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(MAX_FPS)
