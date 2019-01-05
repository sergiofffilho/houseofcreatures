# coding=utf-8

class Minigame:
    #Método de inicialização
    def __init__(self, HUD, player, screen, hapnessGain, hungryCost, hygieneCost, score, difficultMultiplier):
        self._HUD = HUD
        self._player = player
        self._screen = screen
        self._hapnessGain = hapnessGain
        self._hungryCost = hungryCost
        self._hygieneCost = hygieneCost
        self._score = score
        self._difficultMultiplier = difficultMultiplier

    #Método para transformar os scores em coins para o player
    def scoreToCoins(self):
        if self._score % 50 == 0:
             self._player.coins += self._score / 50
        print self._player.coins

    #Métodos getters e setters
    @property
    def HUD(self):
        return self._HUD
    @HUD.setter
    def HUD(self, value):
        self._HUD = value

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, value):
        self._player = value

    @property
    def screen(self):
        return self._screen
    @screen.setter
    def screen(self, value):
        self._screen = value

    @property
    def hapnessGain(self):
        return self._hapnessGain
    @hapnessGain.setter
    def hapnessGain(self, value):
        self._hapnessGain = value

    @property
    def hungryCost(self):
        return self._hungryCost
    @hungryCost.setter
    def hungryCost(self, value):
        self._hungryCost = value

    @property
    def hygieneCost(self):
        return self._hygieneCost
    @hygieneCost.setter
    def hygieneCost(self, value):
        self._hygieneCost = value

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        self._score = value

    @property
    def difficultMultiplier(self):
        return self._difficultMultiplier
    @difficultMultiplier.setter
    def difficultMultuplier(self, value):
        self._difficultMultiplier = value