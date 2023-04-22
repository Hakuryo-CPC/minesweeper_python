import pygame

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

def show_timer():
    # Show clock image
    image_position = (10, 173)
    window.blit(clock_img, image_position)

    # Show timer
    ticks_now = pygame.time.get_ticks()
    mins = int(ticks_now / 1000 / 60)
    secs = int(ticks_now / 1000 % 60)

    # Fill with zero
    timer_mins = ""; timer_secs = ""
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
