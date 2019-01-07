# coding=utf-8
import time

class Creature:
    __count_creatures = 0

    #Método de criação
    def __init__(self, name, sprites, hapness=100.0, hungry=100.0, hygiene=100.0):
        self._name = name
        self._sprites = sprites
        self._hapness = hapness
        self._hungry = hungry
        self._hygiene = hygiene
        self.__count_creatures += 1

    #Método para animar sprites
    def anime_creature(self):
        pass

    #Métodos para decrementar com o tempo os atributos hapness, hungry, hygiene
    def autoDecreaseHapness(self, time_start, hap):
        self._hapness = hap
        if time.time() - time_start > 0.4:
            self._hapness -= 1
            if self._hapness < 0:
                self._hapness = 0
            elif self._hapness > 100:
                self._hapness = 100
        return self._hapness



    def autoDecreaseHungry(self, time_start, hun):
        self._hungry = hun
        if time.time() - time_start > 0.4:
            self._hungry -= 1
            if self._hungry < 0:
                self._hungry = 0
        return self._hungry

    def autoDecreaseHygiene(self, time_start):
        if time.time() - time_start > 1:
            self._hygiene -= 1
            if self._hygiene < 0:
                self._hygiene = 0
        return self._hygiene

    #Métodos getter e setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sprites(self):
        return self._sprites
    @sprites.setter
    def sprites(self, value):
        self._sprites = value

    @property
    def hapness(self):
        return self._hapness
    @hapness.setter
    def hapness(self, value):
        self._hapness = value
        if self._hapness > 100:
            self._hapness = 100

    @property
    def hungry(self):
        return self._hungry
    @hungry.setter
    def hungry(self, value):
        self._hungry = value
        if self._hungry > 100:
            self._hungry = 100

    @property
    def hygiene(self):
        return self._hygiene
    @hygiene.setter
    def hygiene(self, value):
        self._hygiene = value
        if self._hygiene > 100:
            self._hygiene = 100

    #Métodos de classe
    @classmethod
    def get_count_creatures(cls):
        return cls.__count_creatures



