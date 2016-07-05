import Unit


class Squad:
    units = None
    health = None

    def __init__(self, **kwargs):
        self.units = [Unit.Solder() for _ in range(1, kwargs['soldiers']+1)]
        self.units += [Unit.Vehicles() for _ in range(1, kwargs['vehicles']+1)]

    @property
    def get_experience(self):
        return sum([i.get_experience for i in self.units])

    @property
    def get_health(self):
        self.health = sum([i.get_health for i in self.units])
        return self.health

    @property
    def do_attack(self):
        return sum([i.do_attack for i in self.units]) / len(self.units)

    def take_damage(self, damage):
        damage /= len(self.units)
        for i in self.units:
            i.take_damage(damage)