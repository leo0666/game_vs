def Ammo_type(lang):
    from Trad.trad import load_translation

    messages = load_translation(lang)

    # class
    class AMMOTYPE:
        def __init__(self, name, percent_damage_increase):
            self.name = name
            self.percent_damage_increase = percent_damage_increase

    class NORMAL(AMMOTYPE):
        def __init__(self, name, percent_damage_increase=1):
            super().__init__(name, percent_damage_increase)

    class EXPLOSIVE(AMMOTYPE):
        def __init__(self, name, percent_damage_increase=1.3):
            super().__init__(name, percent_damage_increase)

    # to do:
    # piercing
    # poisoned
    # incendiary

    # AMMOTYPE program

    normal_ammo = NORMAL(messages["name_normal_ammo"])
    explosive_ammo = EXPLOSIVE(messages["name_explosive_ammo"])

    ammo_type_list = [normal_ammo, explosive_ammo]

    return ammo_type_list
