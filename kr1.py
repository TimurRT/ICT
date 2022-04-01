import csv

class Weapon:

    def __init__(self, caliber, mass):
        self.caliber = caliber
        self.mass = mass
        self.power = int(caliber) * int(mass)

    def loadthegun(self, cartridge_obj):
        return Clip.add_cartridge(cartridge_obj, self)


class Clip(Weapon):

    def clip(self):
        self.clip = []

    def add_cartridge(self, cartridge_obj):
        return cartridge_obj.clip_weapon(cartridge_obj, self)

    def clip_weapon (self, cartridge):
       self.clip.append(cartridge)

    def write_file(self):
        with open('shells.csv', 'a+') as file:
            weapon_information = (f' Снаряд 1: {self.caliber}, {self.mass}, {self.power} '
                                  f' Снаряд 2: {self.caliber}, {self.mass}, {self.power}'
                                  f' Снаряд 3: {self.caliber}, {self.mass}, {self.power}'
                                  f' Снаряд 4: {self.caliber}, {self.mass}, {self.power}')
            record = csv.writer(file)
            record.writerow([weapon_information])

#clip = Clip()

#projectile_1 = Weapon(5, 7)
#projectile_2 = Weapon(6, 8)
#projectile_3 = Weapon(7,9)
#projectile_4 = Weapon(8,10)

#clip.clip_weapon(projectile_1)
#clip.clip_weapon(projectile_2)
#clip.clip_weapon(projectile_3)
#clip.clip_weapon(projectile_4)

#clip.write_file()