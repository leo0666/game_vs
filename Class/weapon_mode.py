def Weapon_mode(lang):
    from Trad.trad import load_translation

    messages = load_translation(lang)

    # class

    class WEAPONMODE:
        def __init__(self, name, nb_bullets_fired, percent_damage_reduction):
            self.name = name
            self.nb_bullets_fired = nb_bullets_fired
            self.percent_damage_reduction = percent_damage_reduction

    class SINGLESHOT(WEAPONMODE):
        def __init__(self, name, nb_bullets_fired=1, percent_damage_reduction=1):
            super().__init__(name, nb_bullets_fired, percent_damage_reduction)

    class AUTOMATIC(WEAPONMODE):
        def __init__(self, name, nb_bullets_fired=10, percent_damage_reduction=0.6):
            super().__init__(name, nb_bullets_fired, percent_damage_reduction)

    class BURSTFIRE(WEAPONMODE):
        def __init__(self, name, nb_bullets_fired=3, percent_damage_reduction=0.8):
            super().__init__(name, nb_bullets_fired, percent_damage_reduction)

    # Weapon mode program
    single_shot = SINGLESHOT(messages["name_single_shot"])
    automatic = AUTOMATIC(messages["name_automatic"])
    burst_fire = BURSTFIRE(messages["name_burst_fire"])

    list_sniper = [single_shot]
    list_assault_rifle = [single_shot, automatic, burst_fire]
    list_shotgun = [single_shot]
    list_pistol = [single_shot]

    return list_sniper, list_assault_rifle, list_shotgun, list_pistol
