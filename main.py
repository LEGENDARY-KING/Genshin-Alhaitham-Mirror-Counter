from pynput.keyboard import Key, Listener
import pygame
from threading import Thread


def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    if key == '1':
        global alhaitham_on_field, text
        alhaitham_on_field = True
        text = "Alhaitham is on field now"
    print('{0} release'.format(key))

# Main game loop
def overlayFunct():
    running = True
    # Initialize Pygame
    pygame.init()
    pygame.display.init()

    # Set the window size and caption
    size = (250, 100)
    caption = "My Transparent Pygame Window"
    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    screen.set_alpha(0)
    # Create a font for the text
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                size = event.size
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        # Clear the screen
        screen.fill((54, 59, 55, 0))

        # Update the text
        # Render the text
        font = pygame.font.Font(None, int((size[0] + size[1]) / 15))
        text_surface = font.render(text, True, (145, 171, 108))
        screen.blit(text_surface, (10, 10))

        # Update the display
        pygame.display.flip()


def keyboardListener():
    with Listener(on_release=on_release) as listener:
        listener.join()


text = ""
alhaitham_on_field = False
t1 = Thread(target=overlayFunct)
t2 = Thread(target=keyboardListener)

t1.start()
t2.start()
