import pygame

from Player import Player
from Creature import Creature
from ItemUsable import Food, Brush
from ItemEquipment import Decoration
from Inventory import Inventory
from Store import Store

def initiateItens():
    itensList = []
    foodOneStar = Food("Osso", 4, 10)
    itensList.append(foodOneStar)
    foodTwoStars = Food("Osso", 6, 20)
    itensList.append(foodTwoStars)
    foodThreeStars = Food("Osso", 7, 30)
    itensList.append(foodThreeStars)
    foodFourStars = Food("Osso", 8, 40)
    itensList.append(foodFourStars)
    foodFiveStars = Food("Osso", 10, 50)
    itensList.append(foodFiveStars)
    foodGourmet = Food("Osso", 18, 100)
    itensList.append(foodGourmet)

    return itensList

def setup():
    croc_image = pygame.image.load("../images/animal_croc.png")
    croc = Creature("croc", croc_image)
    player = Player(0, croc)
    inventory = Inventory()

    #Itens para a store
    itensStore = initiateItens()
    store = Store(itensStore)

if __name__ == '__main__':
    setup()
