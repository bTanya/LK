import random
2
class AttackStrategy:

    def select_squad(self, army):
        raise NotImplementedError("You must override the method")


class Random(AttackStrategy):

    def select_squad(self, army):
        squads = army.get_squads
        random_squad = random.randint(0, len(squads) - 1)
        return squads[random_squad]


class Weakest(AttackStrategy):

    def select_squad(self, army):
        squads = army.get_squads
        min_experience = min([i.get_experience for i in squads])
        for i in squads:
            if i.get_experience == min_experience:
                return i
                break
        return None


class Strongest(AttackStrategy):

    def select_squad(self, army):

        squads = army.get_squads
        max_experience = max([i.get_experience for i in squads])
        for i in squads:
            if i.get_experience == max_experience:
                return i
                break
        return None