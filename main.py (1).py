from pygame import *
from keys import draw_keys, create_key_rects
from settings import *
from sounds import *
from buttons import *
init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano")
sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
my_font = font.SysFont("Arial", 24)
pressed_keys=set()
def start_game():
    pass
def open_settings():
    pass
def exit_game:
    quit()
buttons = [Button(60,20,120,40,"Settings", open_settings)]
running = True
while running:
    screen.fill(WHITE)
    for button in buttons:
        button.draw(screen, my_font)

