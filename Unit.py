import random
import time

class Unit(object):
    __health = 100
    __recharge = None
    __timeLastAtt = None

    def do_attack(self):
        raise NotImplementedError("You must override the method")

    def take_damage(self):
        raise NotImplementedError("You must override the method")

    def check_attack(self):
        # type: () -> object
        now = time.time() * 1000
        if self.get_timeLastAtt() is None:
            return True
        else:
            if self.get_timeLastAtt() + self.__recharge > now:
                return False
            else:
                return True
    @property
    def get_recharge(self):
        return self.__recharge

    def set_recharge(self, recharge):
        self.__recharge = recharge

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_timeLastAtt(self):
        return self.__timeLastAtt

    def set_timeLastAtt(self, timeLastAtt):
        self.__timeLastAtt = timeLastAtt


class Solder(Unit):
    __experience = 0
    def __init__(self):
        self.recharge = random.randint(100,2000)

    def  experienceUp(self):
        self.set_experience(self,self.get_experience()+1)

    def do_attack(self):
        if self.check_attack() and self.get_health() > 0:
            self.set_timeLastAtt(time.time() * 1000)
            self.experienceUp()
            return 0.5 * (1 + self.get_health() / 100) * random.randint(50 + self.get_experience, 100) / 100
        return 0

    def take_damage(self,damage):
        self.set_health(self.get_health()-(damage - 0.05 + self.get_experience / 100))

    @property
    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience


class Vehicles(Unit):

    operators = []

    def __init__(self):
        self.__recharge = random.randint(1000,2000)
        operator_count = random.randint(1,3)
        self.operators = [Solder() for _ in range(0, operator_count)]
        list_operators = [i.get_health for i in self.operators]
        self.set_health(sum(list_operators) / len(list_operators))

    def alive(units):
        for i in units:
            if i.get_health > 0:
                return True
                break
        return False

    def do_attack(self):
        if self.get_health > 0 and self.check_attack() \
                and self.alive(self.operators):
            list_operators = [i.do_attack for i in
                                    self.operators]
            vehicles_attack = 0.5 * (1 + self.get_health / 100) * (
                sum(list_operators) / len(list_operators))
            self.set_timeLastAtt(time.time() * 1000)
            return vehicles_attack
        return 0


    def take_damage(self, damage):
        list_operators = [i.get_experience / 1000 for i in self.operators]
        damage -= 0.1 + sum(list_operators)
        self.set_health(self.get_health - damage * 0.6)
        random_operator = random.randint(0, len(self.operators) - 1)
        current_operator = 0
        while current_operator < len(self.operators):
            if current_operator == random_operator:
                self.operators[current_operator].take_damage(damage * 0.2)
            else:
                self.operators[current_operator].take_damage(damage * 0.1)
                current_operator += 1

