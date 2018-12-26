# coding=utf-8

class Player:

    #Método de criação
    def __init__(self, coins, creatures = []):
        self._coins = coins
        self._creatures = creatures

    #Métodos getters e setters
    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, value):
        self._coins = value

    @property
    def creatures(self):
        return self._creatures
    @creatures.setter
    def creatures(self, value):
        self._creatures = value