def Weapon(lang):
    from Class.ammo_type import Ammo_type
    from Class.weapon_mode import Weapon_mode
    from random import randint
    from Trad.trad import load_translation

    messages = load_translation(lang)

    list_pistol, list_assault_rifle, list_sniper, list_shotgun = Weapon_mode(lang)
    ammo_type_list = Ammo_type(lang)

    # Classes

    class WEAPON:
        def __init__(self, name, damage, ammo_type=None, mode=None):
            self.name = name
            self.damage = damage
            self.ammo_type = ammo_type
            self.mode = mode

        def update_damage(self, AMMOTYPE, WEAPONMODE):
            self.damage *= AMMOTYPE.percent_damage_increase
            self.damage *= WEAPONMODE.percent_damage_reduction
            self.damage *= WEAPONMODE.nb_bullets_fired

    class NOWEAPON(WEAPON):
        def __init__(self, name, damage=0):
            super().__init__(name, damage)

    class PISTOL(WEAPON):
        def __init__(self, name, damage=10):
            super().__init__(name, damage)

    class SNIPER(WEAPON):
        def __init__(self, name, damage=100):
            super().__init__(name, damage)

    class SHOTGUN(WEAPON):
        def __init__(self, name, damage=50):
            super().__init__(name, damage)

    class ASSAULTRIFLE(WEAPON):
        def __init__(self, name, damage=25):
            super().__init__(name, damage)

    class GODRIFLE(WEAPON):
        def __init__(self, name, damage=250):
            super().__init__(name, damage)

    # To do:
    # Galil
    # Desert Eagle
    # M14
    # M4
    # Kalashnikov
    # AK47

    # Weapon program

    no_weapon = NOWEAPON(messages["no_weapon"])
    pistol = PISTOL(messages["name_9mm"])
    sniper = SNIPER(messages["name_barrett_m81"])
    spas12 = SHOTGUN(messages["name_spas12"])
    phamas = ASSAULTRIFLE(messages["name_phamas"])
    god_rifle = GODRIFLE(messages["name_god_rifle"])

    pistol.ammo_type = ammo_type_list[randint(0, len(ammo_type_list) - 1)]
    pistol.mode = list_pistol[randint(0, len(list_pistol) - 1)]
    pistol.update_damage(pistol.ammo_type, pistol.mode)

    sniper.ammo_type = ammo_type_list[randint(0, len(ammo_type_list) - 1)]
    sniper.mode = list_sniper[randint(0, len(list_sniper) - 1)]
    sniper.update_damage(sniper.ammo_type, sniper.mode)

    spas12.ammo_type = ammo_type_list[randint(0, len(ammo_type_list) - 1)]
    spas12.mode = list_shotgun[randint(0, len(list_shotgun) - 1)]
    spas12.update_damage(spas12.ammo_type, spas12.mode)

    phamas.ammo_type = ammo_type_list[randint(0, len(ammo_type_list) - 1)]
    phamas.mode = list_assault_rifle[randint(0, len(list_assault_rifle) - 1)]
    phamas.update_damage(phamas.ammo_type, phamas.mode)

    god_rifle.ammo_type = ammo_type_list[randint(0, len(ammo_type_list) - 1)]
    god_rifle.mode = list_assault_rifle[randint(0, len(list_assault_rifle) - 1)]
    god_rifle.update_damage(phamas.ammo_type, phamas.mode)

    weapon_list = [no_weapon, spas12, pistol, phamas, sniper, god_rifle]

    return weapon_list
