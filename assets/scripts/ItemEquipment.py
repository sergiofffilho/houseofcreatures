# coding=utf-8

from Item import Item

class ItemEquipment(Item):
    #Método de criação
    def __init__(self, name, price, equipped=False):
        Item.__init__(self, name, price)
        self._equipped = equipped

    #Métodos getters e setters
    @property
    def equipped(self):
        return self._equipped
    @equipped.setter
    def equipped(self, value):
        self._equipped = value

class Decoration(ItemEquipment):
    #Método de criação
    def __init__(self, name, price, equipped=False):
        ItemEquipment.__init__(self, name, price, equipped)

'''
i = Decoration(400)
print i.price, i.equipped
i.price = 200
i.equipped = True
print i.price, i.equipped
'''
