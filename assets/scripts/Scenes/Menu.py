#coding=utf-8

import pygame, time
from setup import setup
from utils import blit_images
from HUD import HUD

class Hall():
    def __init__(self):
        self.images_list = {}
        self.clock = pygame.time.Clock() # Tempo de jogo

    def oppening(self):
        self.crashed = False

        self.background = pygame.image.load("../../images/background_big.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

        self.bubble = pygame.image.load("../../images/icon_bubble1.png").convert_alpha()
        self.bubble = pygame.transform.scale(self.bubble, (self.bubble.get_width()/10, self.bubble.get_height()/10))
        self.images_list[self.bubble] = (20,55)

        self.bubble2 = pygame.image.load("../../images/icon_bubble2.png").convert_alpha()
        self.bubble2 = pygame.transform.scale(self.bubble2, (self.bubble2.get_width()/10, self.bubble2.get_height()/10))

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
            screen.blit(self.background,(0,0))

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
                if self.images_list[self.detective][0] > 100 and self.flagAnimDetective:
                    self.images_list[self.detective] = \
                    (self.images_list[self.detective][0] - 8, 640 - self.detective.get_size()[1])
                elif self.images_list[self.detective][0] < 290:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if not self.firstText:
                                self.finishDialog = True
                            else:
                                del self.images_list[self.bubble]
                                self.images_list[self.bubble2] = (20,55)

                                self.firstText = False
                        if event.type == pygame.QUIT:
                            self.crashed = True
                    if self.finishDialog:
                        self.images_list[self.detective] = \
                        (self.images_list[self.detective][0] + 8, 640 - self.detective.get_size()[1])
                        self.flagAnimDetective = False
                else:
                    del self.images_list[self.detective], self.images_list[self.bubble2]
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

        pygame.mixer.Sound.play(somAnimal)

        del self.images_list[self.boxOpened]

        self.creatureImage = self.player.creatures.sprites
        self.creatureImage = pygame.transform.scale(self.creatureImage, (self.creatureImage.get_width()/10, self.creatureImage.get_height()/10))

        self.images_list[self.creatureImage] = (120,300)

        self.loop(self.player)

    def loop(self, player):
        self.player = player

        crashed = False

        self.activePanelInventory = False
        self.activePanelStore = False

        self.font_choice = pygame.font.Font("../../fonts/PORKYS_.ttf", 50)
        self.text_choice = self.font_choice.render("Pick One!", False, (0,0,0))
        self.images_list[self.text_choice] = (80,55)

        self.loadImages()

        while not crashed:
            screen.blit(self.background,(0,0))

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.detectClick(mouse_pos)

                try:

                    if mouse_pos[0] >= self.images_list[self.creatureImage][0] and \
                     mouse_pos[1] >= self.images_list[self.creatureImage][1] and \
                     mouse_pos[0] <= self.images_list[self.creatureImage][0]+self.creatureImage.get_width() and \
                     mouse_pos[1] <= self.images_list[self.creatureImage][1]+self.creatureImage.get_height():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            h = HUD(self, self.player, screen)
                            h.loop()
                except KeyError:
                    pass

                if event.type == pygame.QUIT:
                    crashed = True

            blit_images(screen, self.images_list)

            if self.activePanelInventory:
                screen.blit(self.panelInventory, (0,0))
            elif self.activePanelStore:
                screen.blit(self.panelStore, (0,0))

            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

    def loadImages(self):
        self.btnIventory = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Inventory.png").convert_alpha()
        self.btnIventory = pygame.transform.scale(self.btnIventory, (self.btnIventory.get_width(), self.btnIventory.get_height()))
        self.images_list[self.btnIventory] = (-20, 290)

        self.btnStore = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Store.png").convert_alpha()
        self.btnStore = pygame.transform.scale(self.btnStore, (self.btnStore.get_width(), self.btnStore.get_height()))
        self.images_list[self.btnStore] = (-20, 360)

        self.btnOptions = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Options.png").convert_alpha()
        self.btnOptions = pygame.transform.scale(self.btnOptions, (self.btnOptions.get_width(), self.btnOptions.get_height()))
        self.images_list[self.btnOptions] = (-20, 430)

        #Paineis dos botões
        self.panelInventory = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "MenuContent/Inventory.png").convert_alpha()
        self.panelInventory = pygame.transform.scale(self.panelInventory, (screen_width, screen_height))

        self.panelStore = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "MenuContent/Store.png").convert_alpha()
        self.panelStore = pygame.transform.scale(self.panelStore, (screen_width, screen_height))

    def detectClick(self, mouse_pos):
        if self.activePanelInventory:
            if mouse_pos[0] >= 327 and mouse_pos[1] >= 41 and \
                mouse_pos[0] <= 353 and mouse_pos[1] <= 64:
                    self.activePanelInventory = False
                    self.images_list[self.btnIventory] = (-20, 290)

        elif self.activePanelStore:
            if mouse_pos[0] >= 327 and mouse_pos[1] >= 41 and \
                mouse_pos[0] <= 353 and mouse_pos[1] <= 64:
                    self.activePanelStore = False
                    self.images_list[self.btnStore] = (-20, 360)

        else:
            if mouse_pos[0] >= self.images_list[self.btnIventory][0] and \
                mouse_pos[1] >= self.images_list[self.btnIventory][1] and \
                mouse_pos[0] <= self.images_list[self.btnIventory][0]+self.btnIventory.get_width() and \
                mouse_pos[1] <= self.images_list[self.btnIventory][1]+self.btnIventory.get_height():
                self.images_list[self.btnIventory] = (0, 290)
                self.images_list[self.btnStore] = (-20, 360)
                self.images_list[self.btnOptions] = (-20, 430)
                self.activePanelInventory = True

            elif mouse_pos[0] >= self.images_list[self.btnStore][0] and \
                mouse_pos[1] >= self.images_list[self.btnStore][1] and \
                mouse_pos[0] <= self.images_list[self.btnStore][0]+self.btnStore.get_width() and \
                mouse_pos[1] <= self.images_list[self.btnStore][1]+self.btnStore.get_height():
                self.images_list[self.btnIventory] = (-20, 290)
                self.images_list[self.btnStore] = (0, 360)
                self.images_list[self.btnOptions] = (-20, 430)
                self.activePanelStore = True

            elif mouse_pos[0] >= self.images_list[self.btnOptions][0] and \
                mouse_pos[1] >= self.images_list[self.btnOptions][1] and \
                mouse_pos[0] <= self.images_list[self.btnOptions][0]+self.btnOptions.get_width() and \
                mouse_pos[1] <= self.images_list[self.btnOptions][1]+self.btnOptions.get_height():
                self.images_list[self.btnIventory] = (-20, 290)
                self.images_list[self.btnStore] = (-20, 360)
                self.images_list[self.btnOptions] = (0, 430)

class Menu():
    def __init__(self):
        self.images_list = {}

        self.backgroundsplash = pygame.image.load("../../images/backgroundSplash.png").convert_alpha()
        self.backgroundsplash = pygame.transform.scale(self.backgroundsplash, (screen_width, screen_height))

        self.button_login = pygame.image.load("../../images/playBT.png").convert_alpha()
        self.button_login = pygame.transform.scale(self.button_login, (130,70))
        self.images_list[self.button_login] = (screen_width/2 -65,400)

        pygame.mixer.music.load ("../../sounds/Ap1.wav")
        pygame.mixer.music.play(-1)

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

            screen.blit(self.backgroundsplash, (0, 0))
            blit_images(screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

def runSplash():
    crashed = False
    clock = pygame.time.Clock() # Tempo de jogo

    splashImage = pygame.image.load("../../images/StudioSplash.png").convert()
    splashImage = pygame.transform.scale(splashImage, (screen_width, screen_height))

    time_s = time.time()
    splashImage.set_alpha(35)

    while not crashed:
        if time.time() - time_s > 3:
            crashed = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        pygame.time.delay(30)
        screen.blit(splashImage,(0,0))

        pygame.display.update()
        clock.tick(60) # fps

if __name__ == '__main__':
    pygame.init()

    pygame.display.init()
    pygame.mixer.init()
    play_sound = pygame.mixer.Sound("../../sounds/play.wav")
    openBox_sound = pygame.mixer.Sound("../../sounds/animal_aparece.wav")
    somAnimal = pygame.mixer.Sound("../../sounds/som_animal.wav")

    screen = pygame.display.set_mode([360, 640])
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    pygame.display.set_caption("House of Creatures")

    runSplash()

    menu = Menu()
    menu.loop()