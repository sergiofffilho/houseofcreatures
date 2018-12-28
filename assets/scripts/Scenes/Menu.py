import pygame
from setup import setup
from utils import blit_images

class Hall():
    def __init__(self):
        self.images_list = {}
        self.clock = pygame.time.Clock() # Tempo de jogo

    def oppening(self):
        self.crashed = False

        background = pygame.image.load("../../images/background_big.png").convert_alpha()
        background = pygame.transform.scale(background, (screen_width, screen_height))


        self.bubble = pygame.image.load("../../images/icon_bubble.png").convert_alpha()
        self.bubble = pygame.transform.scale(self.bubble, (self.bubble.get_width()/10, self.bubble.get_height()/10))
        self.images_list[self.bubble] = (20,55)

        self.font_ballon = pygame.font.SysFont("Arial", 18)
        self.text_ballon = self.font_ballon.render("Welcome", False, (0,0,0))
        self.text_ballon2 = self.font_ballon.render("tap to continue!", False, (0,0,0))
        self.images_list[self.text_ballon] = (70,90)
        self.images_list[self.text_ballon2] = (50,110)

        self.detective = pygame.image.load("../../images/animal_tutorial_cat.png").convert_alpha()
        self.detective = pygame.transform.scale(self.detective, (self.detective.get_width()/3, self.detective.get_height()/3))
        self.images_list[self.detective] = (screen_width, screen_height - self.detective.get_size()[1])

        self.boxClosed = pygame.image.load("../../images/box_closed.png").convert_alpha()
        self.boxClosed = pygame.transform.scale(self.boxClosed, (self.boxClosed.get_width()/5, self.boxClosed.get_height()/5))

        self.boxOpened = pygame.image.load("../../images/box_opened.png").convert_alpha()
        self.boxOpened = pygame.transform.scale(self.boxOpened, (self.boxOpened.get_width()/5, self.boxOpened.get_height()/5))

        self.firstText = True
        self.finishDialog = False
        self.flagAnimDetective = True
        self.opened = False

        while not self.crashed:
            screen.blit(background,(0,0))

            self.animateDetective()

            if self.finishDialog:
                self.openBox()

            blit_images(screen, self.images_list)

            pygame.display.flip() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

    def animateDetective(self):
            try:
                print self.images_list[self.detective][0]
                if self.images_list[self.detective][0] > 100 and self.flagAnimDetective:
                    self.images_list[self.detective] = \
                    (self.images_list[self.detective][0] - 8, 640 - self.detective.get_size()[1])
                elif self.images_list[self.detective][0] < 290:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if not self.firstText:
                                self.finishDialog = True
                            else:
                                del self.images_list[self.text_ballon], self.images_list[self.text_ballon2]
                                self.text_ballon = self.font_ballon.render("Open the box!", False, (0,0,0))
                                self.images_list[self.text_ballon] = (50,110)
                                self.firstText = False
                        if event.type == pygame.QUIT:
                            self.crashed = True
                    if self.finishDialog:
                        self.images_list[self.detective] = \
                        (self.images_list[self.detective][0] + 8, 640 - self.detective.get_size()[1])
                        self.flagAnimDetective = False
                else:
                    del self.images_list[self.detective], \
                    self.images_list[self.text_ballon], self.images_list[self.bubble]
            except KeyError:
                if not self.opened:
                    self.images_list[self.boxClosed] = (78, 300)

    def openBox(self):
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            try:
                if mouse_pos[0] >= self.images_list[self.boxClosed][0] and \
                 mouse_pos[1] >= self.images_list[self.boxClosed][1] and \
                 mouse_pos[0] <= self.images_list[self.boxClosed][0]+self.boxClosed.get_width() and \
                 mouse_pos[1] <= self.images_list[self.boxClosed][1]+self.boxClosed.get_height():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        del self.images_list[self.boxClosed]
                        pygame.mixer.Sound.play(openBox_sound)
                        self.images_list[self.boxOpened] = (5, 275)

                        self.opened = True
                        self.randomCreature()
            except KeyError:
                pass

            if event.type == pygame.QUIT:
                    self.crashed = True


    def randomCreature(self):
        self.player, self.inventory, self.store = setup()
        blit_images(screen, self.images_list)
        pygame.display.flip() # Mostra frame
        pygame.time.wait(2000)

        del self.images_list[self.boxOpened]

        creatureImage = self.player.creatures.sprites
        creatureImage = pygame.transform.scale(creatureImage, (creatureImage.get_width()/7, creatureImage.get_height()/7))

        self.images_list[creatureImage] = (70,270)

        sorted_x = sorted(self.images_list, key=self.images_list.get, reverse=True)

        print sorted_x





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
        pygame.mixer.music.load ("../../sounds/Ap1.wav")
        pygame.mixer.music.play(-1)

        logo = pygame.image.load("../../images/HOC_logo.png").convert_alpha()
        logo = pygame.transform.scale(logo, (200,200))
        self.images_list[logo] = (80, 120)
        self.button_login = pygame.image.load("../../images/button_login.png").convert_alpha()
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
                        pygame.mixer.Sound.play(play_sound)
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
    pygame.mixer.init()
    play_sound = pygame.mixer.Sound("../../sounds/play.wav")
    openBox_sound = pygame.mixer.Sound("../../sounds/caixa_abre.wav")


    screen = pygame.display.set_mode([360, 640])
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    pygame.display.set_caption("House of Creatures")

    menu = Menu()
    menu.loop()
##    h = Hall()
##    h.oppening()


