import random
from datetime import datetime

class Unit(object):
    health = 100
    recharge = None
    #def __init__(self):
    def do_attack(self):
        raise NotImplementedError("You must override the method")


    def take_damage(self):
        raise NotImplementedError("You must override the method")


class Solder(Unit):
    experience = 0
    timeLastAtt = 0
    def __init__(self):
        self.recharge = random.randint(100,2000)
    def  experienceUp(self):
        self.experience += 1
    def do_attack(self):
        now = datetime.now()
        if ((self.timeLastAtt - now).seconds)/60 < self.recharge:
            self.timeLastAtt = datetime.now()
            self.experienceUp()
            return 0.5 * (1 + self.health / 100) * random.randint(50 + self.experience, 100) / 100
        return 0
    def take_damage(self,damage):
        self.health -= damage - 0.05 + self.experience / 100



class Vehicles(Unit):
    countOperators = None
    operators = []

    def __init__(self):
        self.recharge = random.randint(1000,2000)
        self.countOperators = random.randint(1,3)
        self.health *= self.countOperators
        for x in self.countOperators:
            self.operators.append(Solder())

    def do_attack(self):
        now = datetime.now()
        if ((self.timeLastAtt - now).seconds) / 60 < self.recharge:
            #нужно решть время повышения уровня
            totalAttak = 0
            for x in self.operators:
                x.experienceUp
                totalAttak +=
            self.timeLastAtt = datetime.now()
            return 0.5 * (1 + self.health / 100) * gavg(operators.attack_success)





