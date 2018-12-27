# coding=utf-8

class Item:

    #Método de criação
    def __init__(self, name, price):
        self._name = name
        self._price = price

    #Métodos getter e setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value