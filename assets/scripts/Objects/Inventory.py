# coding=utf-8

from ItemUsable import Food, Brush
from ItemEquipment import Decoration

class Inventory:

    #Método de criação
    def __init__(self, itensUsable = {}, itensEquipment = {}):
        self._itensUsable = itensUsable
        self._itensEquipment = itensEquipment

    #Método para usar item
    def useItem(self, item):
        try:
            self._itensUsable[item] -= 1
            return item.valueRecovery
        except KeyError:
            print "Not in inventory"

    #Método para equipar item
    def equipItem(self, item):
        try:
            self._itensEquipment[item] -= 1
            item.equipped = True
        except KeyError:
            print "Not in inventory"

    #Métodos getters e setters
    @property
    def itensUsable(self):
        return self._itensUsable
    @itensUsable.setter
    def itensUsable(self, value):
        try:
            self._itensUsable[value] += 1
        except KeyError:
            self._itensUsable[value] = 1

    @property
    def itensEquipment(self):
        return self._itensEquipment
    @itensEquipment.setter
    def itensEquipment(self, value):
        try:
            self._itensEquipment[value] += 1
        except KeyError:
            self._itensEquipment[value] = 1


'''
o = Food("osso", 100, 10)
b = Food("bife", 150, 12)
q = Decoration("quadro", 150)
e = Brush("escova", 50, 15)

i = Inventory({o:2, b:5, e:1}, {q:1})

print i.useItem(o)
i.equipItem(q)
print q.equipped
print i.itensUsable.values()
print i.itensEquipment.values()
'''