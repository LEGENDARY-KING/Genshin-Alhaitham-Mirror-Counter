import configparser
import json
from ctypes import windll, create_unicode_buffer
from time import time
from typing import Optional

import pygame
from pynput.keyboard import Listener as listener_keyboard
from pynput.mouse import Button, Listener as listener_mouse

config = configparser.ConfigParser()
config.read(r'config.ini')

cd_e = 18
cd_q = 18
cd_hold = 14
cd_e_start = 0
cd_q_start = 0
cd_hold_start = 0
mirrors = 0
mirror_refreshed_time = 0
left_button_start = 99999999999
charged_attack_time = 0
alhaitham_on_field = False
mouse_listener = 0
ping = int(config.get("Settings", "avg_ping"))
skill_key = str.lower(config.get("Settings", "skill_key"))
burst_key = str.lower(config.get("Settings", "burst_key"))
alhaitham_key = str.lower(config.get("Settings", "alhaitham_party_key"))
other_party_keys = json.loads(config.get("Settings", "other_party_keys"))
other_party_keys = [x.lower() for x in other_party_keys]
cons = int(config.get("Settings", "constellation"))
game_name = config.get("Settings", "game_name")
if cons >= 1: cd_e = 13

def on_release(key):
    if getForegroundWindowTitle() == game_name:
        try:
            k = str.lower(key.char)  # single-char keys
        except:
            k = str.lower(key.name)
        global alhaitham_on_field, text, cd_e_start, mirrors, cd_q_start, mirror_refreshed_time
        if k == alhaitham_key:
            if alhaitham_on_field: return
            alhaitham_on_field = True
        elif k == skill_key and alhaitham_on_field and time() - cd_e_start > cd_e:
            cd_e_start = time()
            if mirrors < 3:
                if mirrors == 0: mirrors += 1
                mirrors += 1
            mirror_refreshed_time = time()
        elif k == burst_key and alhaitham_on_field and time() - cd_q_start > cd_q:
            cd_q_start = time()
            mirror_refreshed_time = time() + 3.5
            if cons >= 6:
                mirrors = 3
            else:
                mirrors = 3 - mirrors
        elif k in other_party_keys and alhaitham_on_field:
            mirrors = 0
            alhaitham_on_field = False


def on_click(x, y, button, pressed):
    global left_button_start, mirrors, mirror_refreshed_time, cd_hold_start
    if button == Button.left and time() - cd_hold_start > cd_hold and alhaitham_on_field:
        if pressed:
            left_button_start = time()
        else:
            held_for = time() - left_button_start
            if held_for + ping / 1000 > 0.35:
                if mirrors < 3: mirrors += 1
                mirror_refreshed_time = time()
                cd_hold_start = time()


def getForegroundWindowTitle() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    # 1-liner alternative: return buf.value if buf.value else None
    if buf.value:
        return buf.value
    else:
        return None


def text_generator():
    global mirrors, mirror_refreshed_time
    time_left = time() - mirror_refreshed_time;
    if time_left > 4 and mirrors > 0:
        mirrors -= 1
        mirror_refreshed_time = time()
    text = "Mirror Count: " + str(mirrors)
    if mirrors > 0: text += "| Mirror going in: " + str(round(4 - (time() - mirror_refreshed_time), 2))
    return text


listener_keyboard(on_release=on_release).start()
ml = listener_mouse(on_click=on_click)

running = True
pygame.init()
size = (500, 50)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
img = pygame.image.load('./alhaitham.jpg')
pygame.display.set_caption("Alhaitham Mirror Counter");
pygame.display.set_icon(img)
while running:
    if getForegroundWindowTitle() != "Genshin Impact" and listener_mouse.is_alive(ml):
        listener_mouse.stop(ml)
        left_button_start = 99999999999
    elif getForegroundWindowTitle() == "Genshin Impact" and not listener_mouse.is_alive(ml):
        ml = listener_mouse(on_click=on_click)
        ml.start()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            size = event.size
            screen = pygame.display.set_mode((size[0], 50), pygame.RESIZABLE)
        # Clear the screen
    screen.fill((54, 59, 55, 0))
    text = text_generator()
    # Render the text
    font = pygame.font.Font(None, int((size[0]) / 15))
    text_surface = font.render(text, True, (145, 171, 108))
    screen.blit(text_surface, (10, 10))
    clock.tick(60)
    # Update the display
    pygame.display.flip()
