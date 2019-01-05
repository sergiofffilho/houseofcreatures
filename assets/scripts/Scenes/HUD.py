#coding=utf-8


import pygame, time
from utils import blit_images

class HUD():
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        self.images_list = {}

        self.clock = pygame.time.Clock()

        self.hapness = player.creatures.hapness
        self.hungry = player.creatures.hungry
        self.hygiene = player.creatures.hygiene
        self.timeHap = time.time()
        self.timeHun = time.time()
        self.timeHig = time.time()

    def loop(self):
        crashed = False

        self.loadImages()

        while not crashed:
            self.screen.blit(self.background,(0,0))

            self.mountHUD()

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.detectClick(mouse_pos)
                if event.type == pygame.QUIT:
                    crashed = True

            blit_images(self.screen, self.images_list)
            pygame.display.update() # Mostra frame
            self.clock.tick(60) # fps
        pygame.quit()
        quit()

    def loadImages(self):
        self.background = pygame.image.load("../../images/background_base.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        self.creatureImage = self.player.creatures.sprites
        self.creatureImage = pygame.transform.scale(self.creatureImage, (self.creatureImage.get_width()/7, self.creatureImage.get_height()/7))
        self.images_list[self.creatureImage] = (120,270)

        #Imagens barra hapness
        self.barHapEmpty = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/happiness_EMPTY.png").convert_alpha()
        self.barHapEmpty = pygame.transform.scale(self.barHapEmpty, (self.barHapEmpty.get_width()/2, self.barHapEmpty.get_height()/2))

        self.barHap30 = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/happiness_33%.png").convert_alpha()
        self.barHap30 = pygame.transform.scale(self.barHap30, (self.barHap30.get_width()/2, self.barHap30.get_height()/2))

        self.barHap60 = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/happiness_66%.png").convert_alpha()
        self.barHap60 = pygame.transform.scale(self.barHap60, (self.barHap60.get_width()/2, self.barHap60.get_height()/2))

        self.barHapFull = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/happiness_FULL.png").convert_alpha()
        self.barHapFull = pygame.transform.scale(self.barHapFull, (self.barHapFull.get_width()/2, self.barHapFull.get_height()/2))
        self.old_key_hap = self.barHapFull
        self.images_list[self.barHapFull] = (10, 10)

        #Imagens barra hungry
        self.barHunEmpty = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/food_EMPTY.png").convert_alpha()
        self.barHunEmpty = pygame.transform.scale(self.barHunEmpty, (self.barHunEmpty.get_width()/2, self.barHunEmpty.get_height()/2))

        self.barHun30 = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/food_33%.png").convert_alpha()
        self.barHun30 = pygame.transform.scale(self.barHun30, (self.barHun30.get_width()/2, self.barHun30.get_height()/2))

        self.barHun60 = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/food_66%.png").convert_alpha()
        self.barHun60 = pygame.transform.scale(self.barHun60, (self.barHun60.get_width()/2, self.barHun60.get_height()/2))

        self.barHunFull = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/food_FULL.png").convert_alpha()
        self.barHunFull = pygame.transform.scale(self.barHunFull, (self.barHunFull.get_width()/2, self.barHunFull.get_height()/2))
        self.old_key_hun = self.barHunFull
        self.images_list[self.barHunFull] = (10, 35)

        #Imagens barra hygiene
        self.barHigEmpty = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/Higiene_EMPTY.png").convert_alpha()
        self.barHigEmpty = pygame.transform.scale(self.barHigEmpty, (self.barHigEmpty.get_width()/2, self.barHigEmpty.get_height()/2))

        self.barHig30 = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/Higiene_33%.png").convert_alpha()
        self.barHig30 = pygame.transform.scale(self.barHig30, (self.barHig30.get_width()/2, self.barHig30.get_height()/2))

        self.barHig60 = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/Higiene_66%.png").convert_alpha()
        self.barHig60 = pygame.transform.scale(self.barHig60, (self.barHig60.get_width()/2, self.barHig60.get_height()/2))

        self.barHigFull = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "ResourcesUI/Higiene_FULL.png").convert_alpha()
        self.barHigFull = pygame.transform.scale(self.barHigFull, (self.barHigFull.get_width()/2, self.barHigFull.get_height()/2))
        self.old_key_hig = self.barHigFull
        self.images_list[self.barHigFull] = (10, 60)

        #Imagens dos botões do Menu

        self.btnAchievements = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Achievements.png").convert_alpha()
        self.btnAchievements = pygame.transform.scale(self.btnAchievements, (self.btnAchievements.get_width(), self.btnAchievements.get_height()))
        self.images_list[self.btnAchievements] = (-25, 150)

        self.btnGrooming = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Grooming.png").convert_alpha()
        self.btnGrooming = pygame.transform.scale(self.btnGrooming, (self.btnGrooming.get_width(), self.btnGrooming.get_height()))
        self.images_list[self.btnGrooming] = (-20, 220)

        self.btnIventory = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Inventory.png").convert_alpha()
        self.btnIventory = pygame.transform.scale(self.btnIventory, (self.btnIventory.get_width(), self.btnIventory.get_height()))
        self.images_list[self.btnIventory] = (-20, 290)

        self.btnStore = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Store.png").convert_alpha()
        self.btnStore = pygame.transform.scale(self.btnStore, (self.btnStore.get_width(), self.btnStore.get_height()))
        self.images_list[self.btnStore] = (-20, 360)

        self.btnHome = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Home.png").convert_alpha()
        self.btnHome = pygame.transform.scale(self.btnHome, (self.btnHome.get_width(), self.btnHome.get_height()))
        self.images_list[self.btnHome] = (-20, 430)

        self.btnOptions = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/Options.png").convert_alpha()
        self.btnOptions = pygame.transform.scale(self.btnOptions, (self.btnOptions.get_width(), self.btnOptions.get_height()))
        self.images_list[self.btnOptions] = (-20, 500)

        #Imagens para coins
        self.coinsImage = pygame.image.load("../../images/UI_Houseofcreatures/"+\
            "Buttons/PawCoin.png").convert_alpha()
        self.coinsImage = pygame.transform.scale(self.coinsImage, (self.coinsImage.get_width()/43, self.coinsImage.get_height()/43))
        self.images_list[self.coinsImage] = (230, 550)

        self.font_coins = pygame.font.Font("../../fonts/PORKYS_.ttf", 42)
        self.text_coins = self.font_coins.render(str(self.player.coins), False, (255,255,255))
        self.images_list[self.text_coins] = (280,545)

    def mountHUD(self):
        new_key_hap = self.checkHapness()
        if new_key_hap != self.old_key_hap:
            del self.images_list[self.old_key_hap]
            self.old_key_hap = new_key_hap
        self.images_list[new_key_hap] = (10,10)

        new_key_hun = self.checkHungry()
        if new_key_hun != self.old_key_hun:
            del self.images_list[self.old_key_hun]
            self.old_key_hun = new_key_hun
        self.images_list[new_key_hun] = (10,35)

        new_key_hig = self.checkHygiene()
        if new_key_hig != self.old_key_hig:
            del self.images_list[self.old_key_hig]
            self.old_key_hig = new_key_hig
        self.images_list[new_key_hig] = (10,60)

    def checkHapness(self):
        new_h = self.player.creatures.autoDecreaseHapness(self.timeHap)

        if self.hapness > new_h:
            self.hapness = new_h
            self.timeHap = time.time()

        if new_h >= 66:
            return self.barHapFull
        elif new_h >= 33 and new_h < 66:
            return self.barHap60
        elif new_h > 0 and new_h < 33:
            return self.barHap30
        else:
            return self.barHapEmpty

    def checkHungry(self):
        new_h = self.player.creatures.autoDecreaseHungry(self.timeHun)

        if self.hungry > new_h:
            self.hungry = new_h
            self.timeHun = time.time()

        if new_h >= 66:
            return self.barHunFull
        elif new_h >= 33 and new_h < 66:
            return self.barHun60
        elif new_h > 0 and new_h < 33:
            return self.barHun30
        else:
            return self.barHunEmpty

    def checkHygiene(self):
        new_h = self.player.creatures.autoDecreaseHygiene(self.timeHig)

        if self.hygiene > new_h:
            self.hygiene = new_h
            self.timeHig = time.time()

        if new_h >= 66:
            return self.barHigFull
        elif new_h >= 33 and new_h < 66:
            return self.barHig60
        elif new_h > 0 and new_h < 33:
            return self.barHig30
        else:
            return self.barHigEmpty

    def detectClick(self, mouse_pos):
        if mouse_pos[0] >= self.images_list[self.btnAchievements][0] and \
            mouse_pos[1] >= self.images_list[self.btnAchievements][1] and \
            mouse_pos[0] <= self.images_list[self.btnAchievements][0]+self.btnAchievements.get_width() and \
            mouse_pos[1] <= self.images_list[self.btnAchievements][1]+self.btnAchievements.get_height():
            self.images_list[self.btnAchievements] = (0, 150)
            self.images_list[self.btnGrooming] = (-20, 220)
            self.images_list[self.btnIventory] = (-20, 290)
            self.images_list[self.btnStore] = (-20, 360)
            self.images_list[self.btnHome] = (-20, 430)
            self.images_list[self.btnOptions] = (-20, 500)

        elif mouse_pos[0] >= self.images_list[self.btnGrooming][0] and \
            mouse_pos[1] >= self.images_list[self.btnGrooming][1] and \
            mouse_pos[0] <= self.images_list[self.btnGrooming][0]+self.btnGrooming.get_width() and \
            mouse_pos[1] <= self.images_list[self.btnGrooming][1]+self.btnGrooming.get_height():
            self.images_list[self.btnAchievements] = (-20, 150)
            self.images_list[self.btnGrooming] = (0, 220)
            self.images_list[self.btnIventory] = (-20, 290)
            self.images_list[self.btnStore] = (-20, 360)
            self.images_list[self.btnHome] = (-20, 430)
            self.images_list[self.btnOptions] = (-20, 500)
        elif mouse_pos[0] >= self.images_list[self.btnIventory][0] and \
            mouse_pos[1] >= self.images_list[self.btnIventory][1] and \
            mouse_pos[0] <= self.images_list[self.btnIventory][0]+self.btnIventory.get_width() and \
            mouse_pos[1] <= self.images_list[self.btnIventory][1]+self.btnIventory.get_height():
            self.images_list[self.btnAchievements] = (-20, 150)
            self.images_list[self.btnGrooming] = (-20, 220)
            self.images_list[self.btnIventory] = (0, 290)
            self.images_list[self.btnStore] = (-20, 360)
            self.images_list[self.btnHome] = (-20, 430)
            self.images_list[self.btnOptions] = (-20, 500)
        elif mouse_pos[0] >= self.images_list[self.btnStore][0] and \
            mouse_pos[1] >= self.images_list[self.btnStore][1] and \
            mouse_pos[0] <= self.images_list[self.btnStore][0]+self.btnStore.get_width() and \
            mouse_pos[1] <= self.images_list[self.btnStore][1]+self.btnStore.get_height():
            self.images_list[self.btnAchievements] = (-20, 150)
            self.images_list[self.btnGrooming] = (-20, 220)
            self.images_list[self.btnIventory] = (-20, 290)
            self.images_list[self.btnStore] = (0, 360)
            self.images_list[self.btnHome] = (-20, 430)
            self.images_list[self.btnOptions] = (-20, 500)
        elif mouse_pos[0] >= self.images_list[self.btnHome][0] and \
            mouse_pos[1] >= self.images_list[self.btnHome][1] and \
            mouse_pos[0] <= self.images_list[self.btnHome][0]+self.btnHome.get_width() and \
            mouse_pos[1] <= self.images_list[self.btnHome][1]+self.btnHome.get_height():
            self.images_list[self.btnAchievements] = (-20, 150)
            self.images_list[self.btnGrooming] = (-20, 220)
            self.images_list[self.btnIventory] = (-20, 290)
            self.images_list[self.btnStore] = (-20, 360)
            self.images_list[self.btnHome] = (0, 430)
            self.images_list[self.btnOptions] = (-20, 500)
        elif mouse_pos[0] >= self.images_list[self.btnOptions][0] and \
            mouse_pos[1] >= self.images_list[self.btnOptions][1] and \
            mouse_pos[0] <= self.images_list[self.btnOptions][0]+self.btnOptions.get_width() and \
            mouse_pos[1] <= self.images_list[self.btnOptions][1]+self.btnOptions.get_height():
            self.images_list[self.btnAchievements] = (-20, 150)
            self.images_list[self.btnGrooming] = (-20, 220)
            self.images_list[self.btnIventory] = (-20, 290)
            self.images_list[self.btnStore] = (-20, 360)
            self.images_list[self.btnHome] = (-20, 430)
            self.images_list[self.btnOptions] = (0, 500)






