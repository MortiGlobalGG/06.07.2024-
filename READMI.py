import pygame
import random
import sys
import time


lock = pygame.time.Clock()

pygame.init()


screen_size=[840,480]
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
pygame.display.set_caption("Ecosistem")


white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
blue = (0,0,255)
red = (255,0,0)
purple = (127,0,127)



clock = pygame.time.Clock()
FPS = 30

def main_menu():
    menu_items = {'Start': iformation, 'Settings': settings, 'Exit': exit}
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
    menu_items = {'Songs': songs, 'Back': main_menu}
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
    menu_items = {'On/Off(1)': song1, 'On/Off(2)': song2, "Back":settings}
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

def none():
    return 0

def song1():
    screen_works = True
    while screen_works:
        screen.fill(black)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False
    music = pygame.mixer.Sound("C418 – Moog City.mp3")
    music.play(-1)
    return 0

def song2():
    screen_works = True
    while screen_works:
        screen.fill(black)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False
    music2 = pygame.mixer.Sound("Gippeul Red Sun In The Sky.mp3")
    music2.play(-1)
    return 0

def exit():
    pygame.quit()
    sys.exit()



def iformation():
    menu_items = {'Start': game, 'But youre killing my love, and it will destroy me But youre killing my love, my hearts disappointed Ill love you forever, but please dont say never Ill keep you remembered so deep in my heart': none}
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




def game():
    travo_idne_x_spead = random.randint(-10, 10)
    travo_idne_y_spead = random.randint(-10, 10)

    travo_idne_x_cord = 420
    travo_idne_y_cord = 360
    travo_idne = pygame.draw.rect(screen, blue, (travo_idne_x_cord, travo_idne_y_cord, 20, 20))
    pygame.draw.polygon(screen, red, ((400, 80), (420, 60), (440, 80)))
    trava = pygame.draw.circle(screen, purple, (580, 120), 15)

    num_drops = 100
    drops = []
    rain_spead = 5
    for _ in range(num_drops):
        x = random.randint(0, 840)
        y = random.randint(-480, 0)
        speed = random.randint(2, 5)
        drops.append([x, y, speed])


    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #
    #     screen.fill(black)
    #
    #
    #     for drop in drops:
    #         drop[1] += drop[2]
    #         if drop[1] > 480:
    #             drop[0] = random.randint(0, 840)
    #             drop[1] = random.randint(-480, 0)
    #             drop[2] = random.randint(2, 5)
    #
    #         pygame.draw.line(screen, blue, (drop[0], drop[1]), (drop[0], drop[1] + 10))
    #
    #
    #     pygame.display.flip()
    #
    #
    #     pygame.time.Clock().tick(60)


    # _________________________________________________________________________________





    # animals = []
    # food = []
    # for _ in range(10):
    #     animal = {
    #         'x': random.randint(0, screen_size[0]),
    #         'y': random.randint(0, screen_size[1]),
    #         'color': (0, 255, 0),
    #         'size': 5
    #     }
    #     animals.append(animal)
    #
    # for _ in range(20):
    #     f = {
    #         'x': random.randint(0, screen_size[0]),
    #         'y': random.randint(0, screen_size[1]),
    #         'color': (255, 0, 0),
    #         'size': 10
    #     }
    #     food.append(f)
    #
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #     screen.fill((0, 0, 0))
    #
    #     for animal in animals:
    #         pygame.draw.circle(screen, animal['color'], (animal['x'], animal['y']), animal['size'])
    #
    #
    #         animal['x'] += random.randint(-1, 1)
    #         animal['y'] += random.randint(-1, 1)
    #
    #
    #         if animal['x'] < 0:
    #             animal['x'] = 0
    #         if animal['x'] > screen_size[0]:
    #             animal['x'] = screen_size[0]
    #         if animal['y'] < 0:
    #             animal['y'] = 0
    #         if animal['y'] > screen_size[1]:
    #             animal['y'] = screen_size[1]
    #
    #     for f in food:
    #         pygame.draw.circle(screen, f['color'], (f['x'], f['y']), f['size'])
    #
    #
    #     for animal in animals:
    #         for f in food:
    #             if animal['x'] == f['x'] and animal['y'] == f['y']:
    #                 animal['size'] += 1
    #                 food.remove(f)
    #                 break
    #
    #     pygame.display.flip()
    #     clock.tick(30)

    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 700)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == timer_event:

                travo_idne_x_cord += travo_idne_x_spead
                if travo_idne_x_cord > screen_size[0]:
                    travo_idne_x_cord = 0

        screen.fill(black)

        pygame.draw.rect(screen, blue, (travo_idne_x_cord, travo_idne_y_cord, 20, 20))

        pygame.display.flip()


        pygame.display.flip()
        clock.tick(60)














    screen_works = True


    while screen_works:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False



        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_menu()
