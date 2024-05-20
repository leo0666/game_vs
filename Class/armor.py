def Armor(lang):
    from Trad.trad import load_translation

    messages = load_translation(lang)

    # class
    class ARMOR:
        def __init__(self, name, percent_hp_increase):
            self.name = name
            self.percent_hp_increase = percent_hp_increase

    class NOARMOR(ARMOR):
        def __init__(self, name, percent_hp_increase=1):
            super().__init__(name, percent_hp_increase)

    class WOOD(ARMOR):
        def __init__(self, name, percent_hp_increase=1.01):
            super().__init__(name, percent_hp_increase)

    class IRON(ARMOR):
        def __init__(self, name, percent_hp_increase=1.03):
            super().__init__(name, percent_hp_increase)

    class GOD(ARMOR):
        def __init__(self, name, percent_hp_increase=100):
            super().__init__(name, percent_hp_increase)

    # to do:
    # Obsidian

    # ARMOR program
    no_armor = NOARMOR(messages["name_no_armor"])
    wood_armor = WOOD(messages["name_wood_armor"])
    iron_armor = IRON(messages["name_iron_armor"])
    god_armor = GOD(messages["name_god_armor"])

    armor_list = [no_armor, wood_armor, iron_armor, god_armor]

    return armor_list
