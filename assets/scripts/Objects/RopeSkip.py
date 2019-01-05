# coding=utf-8

import pygame
from Minigame import Minigame

class RopeSkip(Minigame):
    def __init__(self, HUD, player, screen, hapnessGain, hungryCost, hygieneCost, score,\
     difficultMultuplier, jumpCounter = 0, ropeVelocity = 1.0):
        Minigame.__init__(self, HUD, player, screen, hapnessGain, hungryCost, hygieneCost, score, difficultMultuplier)
        self._jumpCounter = jumpCounter
        self._ropeVelocity = ropeVelocity

        self.clock = pygame.time.Clock()

    def update(self):
        crashed = False

        self.loadImages()

        while not crashed:
            self.screen.blit(self.background,(0,0))

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.HUD.__init__(self.player, self.screen)
                    self.HUD.loop()

                if event.type == pygame.QUIT:
                    crashed = True

##            blit_images(self.screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

    def loadImages(self):
        self.background = pygame.image.load("../../images/background_corda.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

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
