class Hero():
    damage = 1
    def buff(self):
        print(self.damage)
        self.damage *= 2
hero_0 = Hero()
hero_1 = Hero()
hero_0.att = 1
Hero.damage = 2
print(hasattr(hero_0, 'att'))
hero_0.buff()
print(hero_0.damage, hero_1.damage, Hero.damage)