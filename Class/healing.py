def Healing(lang):
    from Trad.trad import load_translation
    import random

    messages = load_translation(lang)

    # class

    class HEALING:
        def __init__(self, name, percent_hp_restore, usage_count):
            self.name = name
            self.percent_hp_restore = percent_hp_restore
            self.usage_count = usage_count

    class SMALLPOTION(HEALING):
        def __init__(self, name, percent_hp_restore=0.05, usage_count=3):
            super().__init__(name, percent_hp_restore, usage_count)

    class MEDIUMPOTION(HEALING):
        def __init__(self, name, percent_hp_restore=0.15, usage_count=3):
            super().__init__(name, percent_hp_restore, usage_count)

    # healing program

    small_potion = SMALLPOTION(messages["name_small_potion"])
    medium_potion = MEDIUMPOTION(messages["name_medium_potion"])

    healing_list = [small_potion, medium_potion]

    random.shuffle(healing_list)

    return healing_list
