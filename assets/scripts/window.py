import pygame
from utils import blit_images

class Hall():
    def __init__(self):
        self.images_list = {}

        self.clock = pygame.time.Clock() # Tempo de jogo

    def oppening(self):
        crashed = False

        background = pygame.image.load("../images/background_big.png").convert_alpha()
        background = pygame.transform.scale(background, (360, 640))
        self.images_list[background] = (0,0)

        detective = pygame.image.load("../images/animal_tutorial_cat.png").convert_alpha()
        detective = pygame.transform.scale(detective, (360, 640))
        self.images_list[detective] = (0,0)

        bubble = pygame.image.load("../images/icon_bubble.png").convert_alpha()
        bubble = pygame.transform.scale(bubble, (200, 200))
        self.images_list[bubble] = (0,50)

        font_ballon = pygame.font.SysFont("Arial", 18)
        text_ballon = font_ballon.render("Tap on the Box", False, (0,0,0))
        self.images_list[text_ballon] = (40,110)

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            blit_images(screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

    def loop(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            blit_images(screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()


class Menu():
    def __init__(self):
        self.images_list = {}

        screen.fill((251, 201, 236))

        logo = pygame.image.load("../images/HOC_logo.png").convert_alpha()
        logo = pygame.transform.scale(logo, (200,200))
        self.images_list[logo] = (80, 120)

        self.button_login = pygame.image.load("../images/button_login.png").convert_alpha()
        self.button_login = pygame.transform.scale(self.button_login, (200,80))
        self.images_list[self.button_login] = (80,380)

        font_login = pygame.font.SysFont("Arial", 30)
        text_login = font_login.render("PLAY", False, (0,0,0))
        self.images_list[text_login] = (145,405)

        self.clock = pygame.time.Clock() # Tempo de jogo


    def loop(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] >= self.images_list[self.button_login][0] and \
                 mouse_pos[1] >= self.images_list[self.button_login][1] and \
                 mouse_pos[0] <= self.images_list[self.button_login][0]+200 and \
                 mouse_pos[1] <= self.images_list[self.button_login][1]+80:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print "clicou"
                        hall = Hall()
                        hall.oppening()

                if event.type == pygame.QUIT:
                    crashed = True

            blit_images(screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

if __name__ == '__main__':
    pygame.init()

    pygame.display.init()

    screen = pygame.display.set_mode([360, 640])
    pygame.display.set_caption("House of Creatures")

    menu = Menu()
    menu.loop()


