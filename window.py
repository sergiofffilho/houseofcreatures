import pygame
from utils import blit_images

pygame.init()

pygame.display.init()

screen = pygame.display.set_mode([360, 640])
pygame.display.set_caption("House of Creatures")

images_list = {}

screen.fill((251, 201, 236))

logo = pygame.image.load("assets/images/HOC_logo.png")
logo = pygame.transform.scale(logo, (200,200))
images_list[logo] = (80, 120)

button_login = pygame.image.load("assets/images/button_login.png")
button_login = pygame.transform.scale(button_login, (200,80))
images_list[button_login] = (80,380)

font_login = pygame.font.SysFont("Arial", 30)
text_login = font_login.render("PLAY", False, (0,0,0))
images_list[text_login] = (145,405)

blit_images(screen, images_list)

clock = pygame.time.Clock() # Tempo de jogo
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if pygame.mouse.get_pos()[0] >= images_list[button_login][0] and pygame.mouse.get_pos()[1] >= images_list[button_login][1] and pygame.mouse.get_pos()[0] <= images_list[button_login][0]+200 and pygame.mouse.get_pos()[1] <= images_list[button_login][1]+80:
            print "aquiii"
            button_login.set_colorkey((0,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "clicou"
##        print(event)
    pygame.display.update() # Mostra frame
    clock.tick(60) # fps

 
pygame.quit()
quit()


