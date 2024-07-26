import pygame
import sys
import random


clock=pygame.time.Clock()
screen_size=[840,480]
pygame.init()
screen=pygame.display.set_mode(screen_size)

# music=pygame.mixer.Sound("")
# music.play(-1)


black=[0,0,0]
white=[255,255,255]
purple=[127,0,127]
gray=[100,100,100]
red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]
light_green = [0,127,0]
light_blue = [0,0,192]







def main_menu():
    menu_items = {'Start': game, 'Settings': settings, 'Exit': exit}
    font = pygame.font.SysFont(None, 40)
    font1 = pygame.font.SysFont(None, 45)
    screen_works = True
    while screen_works:

        screen.fill(black)
        mouse_cord = pygame.mouse.get_pos()
        for i, item in enumerate(menu_items):
            if mouse_cord[1] < screen_size[1]/2 + 50 * i + 20 and mouse_cord[1] > screen_size[1]/2 + 50 * i - 20:
                draw_text(item, font1, purple, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)
            else:
                draw_text(item,font, white, screen, screen_size[0]/2, screen_size[1]/2 + 50*i)

        events = pygame.event.get()
        for event in events:
             if event.type == pygame.QUIT:
                screen_works = False
             if event.type == pygame.MOUSEBUTTONDOWN:
                 for i, item in enumerate(menu_items):
                     if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                         1] / 2 + 50 * i - 20:
                         menu_items[item]()



        pygame.display.flip()
    pygame.quit()
    sys.exit()


def draw_text(text, font, color, screen, x, y):
    points_text = font.render(text, True, color)
    text_fill = points_text.get_rect()
    text_fill.centerx = x
    text_fill.centery = y
    screen.blit(points_text, text_fill)


def settings():
    menu_items = {'Map - Select a map in game': map, 'Songs': songs, 'Back': main_menu}
    font = pygame.font.SysFont(None, 40)
    font1 = pygame.font.SysFont(None, 45)
    screen_works = True
    while screen_works:

        screen.fill(black)
        mouse_cord = pygame.mouse.get_pos()
        for i, item in enumerate(menu_items):
            if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                1] / 2 + 50 * i - 20:
                draw_text(item, font1, purple, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)
            else:
                draw_text(item, font, white, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, item in enumerate(menu_items):
                    if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                        1] / 2 + 50 * i - 20:
                        menu_items[item]()

        pygame.display.flip()
    pygame.quit()
    sys.exit()


def map():
    menu_items = {'USA': settings,'China': settings, 'UA': settings, 'Brazil': settings, 'Back': settings}
    font = pygame.font.SysFont(None, 40)
    font1 = pygame.font.SysFont(None, 45)
    screen_works = True
    while screen_works:

        screen.fill(black)
        mouse_cord = pygame.mouse.get_pos()
        for i, item in enumerate(menu_items):
            if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                1] / 2 + 50 * i - 20:
                draw_text(item, font1, purple, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)
            else:
                draw_text(item, font, white, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, item in enumerate(menu_items):
                    if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                        1] / 2 + 50 * i - 20:
                        menu_items[item]()

        pygame.display.flip()
    pygame.quit()
    sys.exit()



def songs():
    menu_items = {'On': game,}
    font = pygame.font.SysFont(None, 40)
    font1 = pygame.font.SysFont(None, 45)
    screen_works = True
    while screen_works:

        screen.fill(black)
        mouse_cord = pygame.mouse.get_pos()
        for i, item in enumerate(menu_items):
            if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                1] / 2 + 50 * i - 20:
                draw_text(item, font1, purple, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)
            else:
                draw_text(item, font, white, screen, screen_size[0] / 2, screen_size[1] / 2 + 50 * i)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, item in enumerate(menu_items):
                    if mouse_cord[1] < screen_size[1] / 2 + 50 * i + 20 and mouse_cord[1] > screen_size[
                        1] / 2 + 50 * i - 20:
                        menu_items[item]()

        pygame.display.flip()
    pygame.quit()
    sys.exit()




def exit():
    pygame.quit()
    sys.exit()






def game():
    rect = pygame.draw.rect(screen, light_blue, (
        random.randint(100, screen_size[0] - 100), random.randint(100, screen_size[1] - 100), 10, 10))
    circle = pygame.draw.circle(screen, purple,(random.randint(100, screen_size[0] - 100), random.randint(100, screen_size[1] - 100)),10)
    polugon_x = random.randint(100, screen_size[0] - 100)
    polugon_y = random.randint(100, screen_size[1] - 100)
    polugon = pygame.draw.polygon(screen, light_green, ((polugon_x, polugon_y), (polugon_x + 10, polugon_y), (polugon_x + 5, polugon_y - 10)))
    screen_works = True
    game_works = False
    while screen_works:
        # logic will be here
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False

        keys = pygame.key.get_pressed()
        pygame.display.flip()



def game_mode():
    return 0

if __name__ == "__main__":
    main_menu()


