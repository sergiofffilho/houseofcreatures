# coding=utf-8

class Item:

    #Método de criação
    def __init__(self, price):
        self._price = price

    #Métodos getter e setters
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value