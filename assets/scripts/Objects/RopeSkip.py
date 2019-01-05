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

        while not crashed:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.jump()

                if event.type == pygame.QUIT:
                    crashed = True

            self.screen.blit(self.background,(0,0))
            blit_images(self.screen, self.images_list)

            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

    def loadImages(self):
        self.background = pygame.image.load("../../images/background_corda.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        self.creatureImage = self.player.creatures.sprites
        self.creatureImage = pygame.transform.scale(self.creatureImage, (self.creatureImage.get_width()/10, self.creatureImage.get_height()/10))
        self.images_list[self.creatureImage] = (120,320)

    def jump(self):
##        pygame.display.update() # Mostra frame
##        self.clock.tick(60) # fps
        jumping = True
        finishJump = False

        while not finishJump:
            if self.images_list[self.creatureImage][1] > 200 and jumping:
                self.images_list[self.creatureImage] = (120, self.images_list[self.creatureImage][1]-5)

            elif self.images_list[self.creatureImage][1] < 320:
                self.images_list[self.creatureImage] = (120, self.images_list[self.creatureImage][1]+10)
                jumping = False

            else:
                finishJump = True

            self.screen.blit(self.background,(0,0))
            blit_images(self.screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps


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
