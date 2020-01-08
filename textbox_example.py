import pygame
from textbox import TextBox

def process_input(id, text):
    print(text)

white = (255, 255, 255)

# This makes it so you can hold down keys
KEY_REPEAT_SETTING = (200,70)

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill(white)

# Set the key repeat setting
pygame.key.set_repeat(*KEY_REPEAT_SETTING)

# Define the textbox object. process_input gets called when the 
# enter key is pressed. 
input = TextBox((100,250,600,30),command=process_input,clear_on_enter=True,inactive_on_enter=False)

run = True

while run:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False
        
        # Send all events to the textbox
        input.get_event(event)
    
    # Check for control+v paste
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]):
        pass #TODO: PASTE FROM CLIPBOARD

    # Update the textbox and redraw it
    input.update()
    input.draw(screen)
    
    pygame.display.update()

pygame.quit()

