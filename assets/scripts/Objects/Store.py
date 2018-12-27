# coding=utf-8

from ItemUsable import Food, Brush
from ItemEquipment import Decoration

class Store:
    #Método de criação.
    def __init__(self, itens = []):
        self._itens = itens

    #Métodos para comprar item
    #Ex dictionary: 'itens = {"osso": 2}' -> {"nome_item": qtd}
    def buy(self, itens={}):
        purchaseValue = 0
        for item, qtd in itens.items():
            for i in self._itens:
                if i.name == item:
                    purchaseValue += i.price * qtd
        return purchaseValue

    #Método que aprova compra baseada no valor da compra e saldo do jogador.
    def verifyBalance(self, coins, purchaseValue):
        if coins <= purchaseValue:
            return False
        else:
            return True

    #Métodos getters e setters
    @property
    def itens(self):
        return self._itens
    @itens.setter
    def itens(self, value):
        self._itens.append(value)

'''
o = Food("osso", 100, 10)
b = Food("bife", 150, 12)
q = Decoration("quadro", 150)
e = Brush("escova", 50, 15)

s = Store([o, b, q, e])

print s.buy({"bife":3, "escova":1})
print s.verifyBalance(800, s.buy({"bife":3, "escova":1}))
'''

