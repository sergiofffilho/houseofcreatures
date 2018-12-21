from Item import Item

class ItemUsable(Item):

    #Método de criação
    def __init__(self, price, valueRecovery):
        Item.__init__(self, price)
        self._valueRecovery = valueRecovery

    #Métodos getter e setters
    @property
    def valueRecovery(self):
        return self._valueRecovery
    @valueRecovery.setter
    def valueRecovery(self, value):
        self._valueRecovery = value

class Food(ItemUsable):
    #Método de criação
    def __init__(self, price, valueRecovery):
        ItemUsable.__init__(self, price, valueRecovery)


class Brush(ItemUsable):
    #Método de criação
    def __init__(self, price, valueRecovery):
        ItemUsable.__init__(self, price, valueRecovery)

'''
i = Food(400, 10)
print i.price, i.valueRecovery
i.price = 200
i.valueRecovery = 20
print i.price, i.valueRecovery
'''
