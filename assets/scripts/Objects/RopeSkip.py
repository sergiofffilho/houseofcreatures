# coding=utf-8

import pygame
from Minigame import Minigame
from utils import blit_images


class RopeSkip(Minigame):
    def __init__(self, HUD, hall, player, screen, hapnessGain, hungryCost, hygieneCost, score,\
     difficultMultuplier, jumpCounter = 0):
        Minigame.__init__(self, HUD, hall, player, screen, hapnessGain, hungryCost, hygieneCost, score, difficultMultuplier)
        self._jumpCounter = jumpCounter

        if difficultMultuplier == 3:
            self._ropeVelocity = .08
        elif difficultMultuplier == 2:
            self._ropeVelocity = .1
        else:
            self._ropeVelocity = .12

        self.clock = pygame.time.Clock()
        self.images_list = {}

    def update(self):
        crashed = False

        self.loadImages()

        self.playTime = 0
        self.cycleTime = 0
        self.frameRope = 0

        self.creatureRect, self.ropeRect = None, None
        self.collide = False

        while not crashed:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.jump()

                if event.type == pygame.QUIT:
                    crashed = True

            self.updateScreen()

        pygame.quit()
        quit()

    def loadImages(self):
        self.background = pygame.image.load("../../images/background_corda.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        self.creatureImage = self.player.creatures.sprites
        self.creatureImage = pygame.transform.scale(self.creatureImage, (self.creatureImage.get_width()/10, self.creatureImage.get_height()/10))
        self.creaturePos = (120,400)

        self.font_time = pygame.font.Font("../../fonts/PORKYS_.ttf", 42)

        self.ropeGroup = []

        ropeOne = pygame.image.load("../../images/icon_corda.png").convert_alpha()
        ropeOne = pygame.transform.scale(ropeOne, (ropeOne.get_width()/6, ropeOne.get_height()/6))
        self.ropeGroup.append(ropeOne)

        self.ropeCollider = pygame.Surface((40,5))  # the size of your rect
        self.ropeCollider.set_alpha(0)                # alpha level

        ropeTwo = pygame.image.load("../../images/icon_corda_2.png").convert_alpha()
        ropeTwo = pygame.transform.scale(ropeTwo, (ropeTwo.get_width()/6, ropeTwo.get_height()/6))
        self.ropeGroup.append(ropeTwo)

        ropeThree = pygame.image.load("../../images/icon_corda_3.png").convert_alpha()
        ropeThree = pygame.transform.scale(ropeThree, (ropeThree.get_width()/6, ropeThree.get_height()/6))
        self.ropeGroup.append(ropeThree)

        ropeFour = pygame.image.load("../../images/icon_corda_4.png").convert_alpha()
        ropeFour = pygame.transform.scale(ropeFour, (ropeFour.get_width()/6, ropeFour.get_height()/6))
        self.ropeGroup.append(ropeFour)

        ropeFive = pygame.image.load("../../images/icon_corda_5.png").convert_alpha()
        ropeFive = pygame.transform.scale(ropeFive, (ropeFive.get_width()/6, ropeFive.get_height()/6))
        self.ropeGroup.append(ropeFive)

        ropeSix = pygame.image.load("../../images/icon_corda_6.png").convert_alpha()
        ropeSix = pygame.transform.scale(ropeSix, (ropeSix.get_width()/6, ropeSix.get_height()/6))
        self.ropeGroup.append(ropeSix)

        self.ropeGroup.append(ropeFive)
        self.ropeGroup.append(ropeFour)
        self.ropeGroup.append(ropeThree)
        self.ropeGroup.append(ropeTwo)

    def jump(self):
        jumping = True
        finishJump = False

        while not finishJump:
            if self.creaturePos[1] > 300 and jumping:
                self.creaturePos = (120, self.creaturePos[1]-7)

            elif self.creaturePos[1] < 400:
                self.creaturePos = (120, self.creaturePos[1]+10)
                jumping = False

            else:
                if not self.collide:
                    self.score += 1
                finishJump = True

            self.updateScreen()

    def updateScreen(self):
        milliseconds = self.clock.tick(60) # fps
        seconds = milliseconds/1000.0
        self.playTime += seconds
        self.cycleTime += seconds

        self.text_time = self.font_time.render(str(int(21-self.playTime)), False, (255,255,255))
        self.text_score = self.font_time.render(str(self.score), False, (255,0,0))

        if self.playTime > 21:
            self.backHUD()

        if self.cycleTime > self._ropeVelocity:
            self.frameRope += 1
            if self.frameRope >= len(self.ropeGroup):
                self.frameRope = 0

            self.cycleTime = 0

        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.text_time,(160,100))
        self.screen.blit(self.text_score,(160,150))
        if self.frameRope < 6:
            self.creatureRect = self.screen.blit(self.creatureImage, self.creaturePos)
            self.screen.blit(self.ropeGroup[self.frameRope],(20,240))
        else:
            self.screen.blit(self.ropeGroup[self.frameRope],(20,240))
            self.creatureRect = self.screen.blit(self.creatureImage, self.creaturePos)

        if self.frameRope == 0:
            self.ropeRect = self.screen.blit(self.ropeCollider, (160,520))

            if self.creatureRect.colliderect(self.ropeRect):
                self.collide = True
            else:
                self.collide = False

        pygame.display.update() # Mostra frame

    def backHUD(self):
        self.player.coins += self.scoreToCoins(self.score)
        self.player.creatures.hapness += self.hapnessGain
        self.player.creatures.hungry -= self.hungryCost
        self.player.creatures.hygiene -= self.hygieneCost
        self.HUD.__init__(self.hall, self.player, self.screen)
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
