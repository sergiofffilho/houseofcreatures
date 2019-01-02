import pygame, random, sys
sys.path.append('../Objects')

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
    creatures = ["croc", "doggy", "kitty", "seal"]

    randomInt = random.randint(0,3)

    creatureImage = pygame.image.load("../../images/animal_"+creatures[randomInt]+".png").convert_alpha()
    randomCreature = Creature(creatures[randomInt], creatureImage)
    player = Player(0, randomCreature)
    inventory = Inventory()

    #Itens para a store
    itensStore = initiateItens()
    store = Store(itensStore)

    return player, inventory, store


