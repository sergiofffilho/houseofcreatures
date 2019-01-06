# coding=utf-8

import pygame
from Minigame import Minigame
from utils import blit_images


class RopeSkip(Minigame):
    def __init__(self, HUD, player, screen, hapnessGain, hungryCost, hygieneCost, score,\
     difficultMultuplier, jumpCounter = 0, ropeVelocity = 1.0):
        Minigame.__init__(self, HUD, player, screen, hapnessGain, hungryCost, hygieneCost, score, difficultMultuplier)
        self._jumpCounter = jumpCounter
        self._ropeVelocity = ropeVelocity

        self.clock = pygame.time.Clock()
        self.images_list = {}

    def update(self):
        crashed = False

        self.loadImages()

        self.playTime = 0
        self.cycleTime = 0
        self.interval = .15
        self.frameRope = 0

        while not crashed:
            milliseconds = self.clock.tick(60) # fps
            seconds = milliseconds/1000.0
            self.playTime += seconds
            self.cycleTime += seconds

            self.text_time = self.font_time.render(str(int(21-self.playTime)), False, (255,255,255))

            if self.playTime > 21:
                self.backHUD()

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.jump()

                if event.type == pygame.QUIT:
                    crashed = True

            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.text_time,(160,100))

            if self.cycleTime > self.interval:

                self.frameRope += 1
                if self.frameRope >= len(self.ropeGroup):
                    self.frameRope = 0

                self.cycleTime = 0

            self.screen.blit(self.ropeGroup[self.frameRope],(20,400))

            blit_images(self.screen, self.images_list)

            pygame.display.update() # Mostra frame
        pygame.quit()
        quit()

    def loadImages(self):
        self.background = pygame.image.load("../../images/background_corda.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        self.creatureImage = self.player.creatures.sprites
        self.creatureImage = pygame.transform.scale(self.creatureImage, (self.creatureImage.get_width()/10, self.creatureImage.get_height()/10))
        self.images_list[self.creatureImage] = (120,320)

        self.font_time = pygame.font.Font("../../fonts/PORKYS_.ttf", 42)

        self.ropeGroup = []

        ropeOne = pygame.image.load("../../images/icon_corda.png").convert_alpha()
        ropeOne = pygame.transform.scale(ropeOne, (ropeOne.get_width()/6, ropeOne.get_height()/6))
        self.ropeGroup.append(ropeOne)

        ropeTwo = pygame.image.load("../../images/icon_corda_2.png").convert_alpha()
        ropeTwo = pygame.transform.scale(ropeTwo, (ropeTwo.get_width()/6, ropeTwo.get_height()/6))
        self.ropeGroup.append(ropeTwo)

        ropeThree = pygame.image.load("../../images/icon_corda_3.png").convert_alpha()
        ropeThree = pygame.transform.scale(ropeThree, (ropeThree.get_width()/6, ropeThree.get_height()/6))
        self.ropeGroup.append(ropeThree)

        self.ropeGroup.append(pygame.transform.flip(ropeThree, False, True))
        self.ropeGroup.append(pygame.transform.flip(ropeTwo, False, True))
        self.ropeGroup.append(pygame.transform.flip(ropeOne, False, True))
        self.ropeGroup.append(pygame.transform.flip(ropeTwo, False, True))
        self.ropeGroup.append(pygame.transform.flip(ropeThree, False, True))
        self.ropeGroup.append(ropeThree)
        self.ropeGroup.append(ropeTwo)



    def jump(self):


        jumping = True
        finishJump = False

        while not finishJump:
            milliseconds = self.clock.tick(60) # fps
            seconds = milliseconds/1000.0
            self.playTime += seconds
            self.cycleTime += seconds

            self.text_time = self.font_time.render(str(int(21-self.playTime)), False, (255,255,255))

            if self.playTime > 21:
                self.backHUD()

            if self.images_list[self.creatureImage][1] > 200 and jumping:
                self.images_list[self.creatureImage] = (120, self.images_list[self.creatureImage][1]-5)

            elif self.images_list[self.creatureImage][1] < 320:
                self.images_list[self.creatureImage] = (120, self.images_list[self.creatureImage][1]+10)
                jumping = False

            else:
                finishJump = True

            if self.cycleTime > self.interval:
                self.frameRope += 1
                if self.frameRope >= len(self.ropeGroup):
                    self.frameRope = 0

                self.cycleTime = 0

            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.text_time,(160,100))
            self.screen.blit(self.ropeGroup[self.frameRope],(20,400))

            blit_images(self.screen, self.images_list)
            pygame.display.update() # Mostra frame


    def backHUD(self):
        self.HUD.__init__(self.player, self.screen)
        self.HUD.loop()

    #Métodos getters e setters
    @property
    def jumpCounter(self):
        return self._jumpCounter
    @jumpCounter.setter
    def jumpCounter(self, value):
        self._jumpCounter = value

    @property
    def ropeVelocity(self):
        return self._ropeVelocity
    @ropeVelocity.setter
    def ropeVelocity(self, value):
        self._ropeVelocity = value
